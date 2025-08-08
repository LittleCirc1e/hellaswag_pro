import tqdm
import dashscope
from http import HTTPStatus
import dashscope
import os
import random
import ast
import json
import fire

dashscope.api_key=''

def main(
        total: int = 800,
        model_name: str = "qwen-max",  
        selected_type: str = "sentence_sorting_short",
        broad_type: str = "short",
):
    example = json.dumps({'context': 'The man walked into the room and saw the mess. He wanted to clean it up, so he picked up a broom and started sweeping. He',
    'choices': ['started to clean up the clutter on the table and threw the garbage into the trash can.',
    'picked up a cat and started cleaning the floor, hoping the cat could help him.',
    'started to use the vacuum cleaner but forgot to plug it in.',
    'asked his friends to help with the cleaning, but they kept chatting.']}, ensure_ascii=False)

    example_output = json.dumps({"0":10, "1":1, "2":6, "3":6}, ensure_ascii=False)
    
    example1 = json.dumps({
    'context': 'The man walked into the room and saw the mess. He wanted to clean it up, so he picked up a broom and started sweeping. He',
    'choices': [
    'started to clean up the clutter on the table and threw the garbage into the trash can.',
    'picked up a cat and started cleaning the floor, hoping the cat could help him.',
    'started to use the vacuum cleaner but forgot to plug it in.',
    'asked his friends to help with the cleaning, but they kept chatting.',
    'Brought a dog to help pick up fallen items. ',
    'Picked up a hair dryer and tried to use the wind to blow away the dust on the ground. ',
    'Picked up a toy plane and tried to use it to push the debris. ',
    'Looked for tools to fix the tangled wires. ',
    'Considered calling a neighbor to borrow a cordless vacuum cleaner. ',
    'Walked around the room, but just stared at the ceiling. '
  ]}, ensure_ascii=False)

    example_output1 = json.dumps({"0":10, "1":2, "2":5, "3":4,"4":1, "5":2, "6":1, "7":5,"8":7, "9":3}, ensure_ascii=False)



    original_cases_dir = f"./original_case/{broad_type}/{broad_type}_test.jsonl"
    with open(original_cases_dir, 'r', encoding='utf-8') as file:
        original_cases = [json.loads(line) for line in file]
        print("original case loaded")

    #generate
    output_dir = f"./results_final/{selected_type}/{broad_type}/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cases_dir = f"./in_context_learning/{selected_type}/initial_cases.json"
    with open(cases_dir, 'r', encoding="utf8") as file:
        initial_cases = json.load(file)
        print("initial cases loaded")

    templates_dir = f"./in_context_learning/{selected_type}/in_context_learning.json"
    with open(templates_dir, 'r', encoding="utf8") as file:
        template = json.load(file)[0]
 

    max_new_result_scene=[]
    with tqdm.tqdm(range(total)) as pbar:
        while len(max_new_result_scene) < total:
            original_case_chosen=random.sample(original_cases, 1)

            prompt = template.format(*initial_cases,original_case_chosen[0]['context'],original_case_chosen[0]['choices'],original_case_chosen[0]['label'])
            #print(prompt)
            #generate
            messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content':prompt}]
            
            response = dashscope.Generation.call(
                model=model_name,
                messages=messages,
                result_format='message',  # set the result to be "message" format.
                top_p=0.95,
                temperature=0.95,
                repetition_penalty=1.1
            )
            
            if response.status_code == HTTPStatus.OK:
                result=response.output.choices[0].message['content'].replace('```json','').replace('```','').strip()
                try:
                    result1=ast.literal_eval(result)
                except:
                    print('\033[1;31m' + f"error when ast.literal_eval" + '\033[0m')
                    continue

                result1['original_context'] = original_case_chosen[0]['context']
                result1['original_choices'] = original_case_chosen[0]['choices']
                result1['original_label'] = original_case_chosen[0]['label']
                result1['activity_label']= original_case_chosen[0]['activity_label']

                if selected_type == "problem_reparagraphing":
                    result1['choices'] = original_case_chosen[0]['choices'][:original_case_chosen[0]['label']]+[result1['choices'][original_case_chosen[0]['label']]]+original_case_chosen[0]['choices'][(original_case_chosen[0]['label']+1):]
                #print("result1",result1)
                if selected_type == "negative_testing":
                    result1['label'] = 0

                #choice正确性检查
                result2 = {
                        'context':result1['context'],
                        'choices':result1['choices'],  #generate
                        }
                if selected_type == "problem_reparagraphing":
                    try:
                        messages = [{'role': 'system', 'content': 'You are a teacher with rigorous logic and rich common sense. You can judge which choices are more reasonable and give them high scores, and give low scores to sentences that are obviously contrary to common sense.'},
                                    {'role': 'user', 'content': 'Please determine which of the four options in the json I provided is more suitable to be connected after the context, and output the specific score of each option in json format, with scores ranging from 1 to 10, with 10 being the highest. For example,'+example+',its output is'+example_output+',You only need to output json, no need to output other things. For example,'+example_output+'\nPlease judge this case below\n'+json.dumps(result2)}]
                        response = dashscope.Generation.call(
                            model=model_name,
                            messages=messages,
                            result_format='message',  # set the result to be "message" format.
                        )

                        if response.status_code == HTTPStatus.OK:
                            try:
                                model_label = json.loads(response.output.choices[0].message['content'])
                            except Exception as e:
                                print('choice正确性检查格式错误')
                                print(e)
                                continue
                            if model_label[str(result1['label'])]<9:
                                print('问题重述第1个答案不对')
                                continue
                            jobj = {
                            'original_context': result1['original_context'],
                            'original_choices': result1['original_choices'],
                            'original_label': result1['original_label'],
                            'perturbation_type':result1['perturbation_type'],
                            'context': result1['context'],
                            'choices': result1['choices'],
                            'label': result1['label'],
                            'explanation':result1['explanation'],
                            'activity_label': result1['activity_label'],
                             }
                        else:
                            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (response.request_id, response.status_code,response.code, response.message))
                            continue
                    except Exception as e:
                        print('choice正确性失败') 
                        print(e) 
                        continue
                
                elif selected_type == "abductive_reasoning":
                    try:
                        messages = [{'role': 'system', 'content': 'You are a teacher with rigorous logic and rich common sense. You can judge which choices are more reasonable and give them high scores, and give low scores to sentences that are obviously contrary to common sense.'},
                                        {'role': 'user', 'content': 'Please determine which of the ten options in the json I provided is more suitable to be connected after the context, and output the specific score of each option in json format, with scores ranging from 1 to 10, with 10 being the highest. For example,'+example1+',its output is'+example_output1+',You only need to output json, no need to output other things. For example,'+example_output1+'\nPlease judge this case below\n'+json.dumps(result2)}]
                        response = dashscope.Generation.call(
                            model=model_name,
                            messages=messages,
                            result_format='message',  # set the result to be "message" format.
                        )

                        if response.status_code == HTTPStatus.OK:
                            input_dict= {'label':response.output.choices[0].message['content'], 'context':result1['context'], 'choices':result1['choices']}
                        else:
                            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                            response.request_id, response.status_code,
                            response.code, response.message
                        ))
                            continue
                    except Exception as e:
                        print(e) 
                        continue
                    
                    try:
                        label = json.loads(input_dict['label'].replace('"0"', '"0"'))
                    except Exception as e:
                        print('label格式错误')
                        print(e)
                        continue
                    # 获取 10 分和 5-7 分的选项
                    high_scores = [i for i, score in label.items() if score == 10]
                    # 获取2-8分的item
                    mid_scores_item = [(i, score) for i, score in label.items() if 2 <= score <= 8]
                    # 按分数从高到低排序
                    sorted_mid_scores = sorted(mid_scores_item, key=lambda x: x[1], reverse=True)
                    mid_scores =  [item[0] for item in sorted_mid_scores]

                    # 检查是否满足条件
                    if len(high_scores) >= 1 and len(mid_scores) >= 5:
                        # 选择一个 10 分选项和五个 6-8 分选项，加排序
                        selected_high = high_scores[0]
                        selected_mid =  mid_scores[:5]
                        
                        selected_indices = [int(selected_high)] + [int(i) for i in selected_mid]
                        try:
                            new_choices = [input_dict['choices'][i] for i in selected_indices]
                            new_label = {str(i): label[str(i)] for i in selected_indices}
                            jobj = {
                                'original_context': result1['original_context'],
                                'original_choices': result1['original_choices'],
                                'original_label': result1['original_label'],
                                'perturbation_type':result1['perturbation_type'],
                                'context': input_dict['context'],
                                'choices': new_choices,
                                'label_score': new_label,
                                'label': 0,
                                'explanation':result1['explanation'],
                                'activity_label': result1['activity_label'],

                            }
                        except Exception as e:
                            print('最终数据格式错误')
                            print(e)
                            continue
                    else:
                        jobj = {
                            'original_context': result1['original_context'],
                            'original_choices': result1['original_choices'],
                            'original_label': result1['original_label'],
                            'perturbation_type':result1['perturbation_type'],
                            'context': input_dict['context'],
                            'choices': input_dict['choices'],
                            'label_score': input_dict['label'],
                            'label': 0,
                            'explanation':result1['explanation'],
                            'activity_label': result1['activity_label'],
                        }
                        with open(output_dir+"bad_cases.jsonl", 'w', encoding="utf8") as file:  #generate
                                json.dump(
                                    jobj,
                                    file,
                                    ensure_ascii=False
                                )
                                file.write("\n")
                        print('6选4bad case')
                        continue
                
                elif selected_type == "reverse_conversion":
                    try:
                        messages = [{'role': 'system', 'content': 'You are a teacher with rigorous logic and rich common sense. You can judge which choices are more reasonable and give them high scores, and give low scores to sentences that are obviously contrary to common sense.'},
                                        {'role': 'user', 'content': 'Please determine which of the ten options in the json I provided is more suitable to be connected after the context, and output the specific score of each option in json format, with scores ranging from 1 to 10, with 10 being the highest. For example,'+example1+',its output is'+example_output1+',You only need to output json, no need to output other things. For example,'+example_output1+'\nPlease judge this case below\n'+json.dumps(result2)}]
                        response = dashscope.Generation.call(
                            model=model_name,
                            messages=messages,
                            result_format='message',  # set the result to be "message" format.
                        )

                        if response.status_code == HTTPStatus.OK:
                            input_dict= {'label':response.output.choices[0].message['content'], 'context':result1['context'], 'choices':result1['choices']}
                        else:
                            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                            response.request_id, response.status_code,
                            response.code, response.message
                        ))
                            continue
                    except Exception as e:
                        print(e) 
                        continue
                    
                    try:
                        label = json.loads(input_dict['label'].replace('"0"', '"0"'))
                    except Exception as e:
                        print('label格式错误')
                        print(e)
                        continue
                    # 获取2-8分的item

                    first_key = "0"
                    first_value = label[first_key]

                    # 筛选出值小于first_value的键值对
                    filtered = {k: v for k, v in label.items() if v < first_value}

                    # 按值从大到小排序
                    sorted_items = sorted(filtered.items(), key=lambda item: item[1], reverse=True)

                    # 获取前5个键
                    top5_keys = [k for k, v in sorted_items[:5]]
                    selected_high = 0
                    selected_indices = [int(selected_high)] + [int(i) for i in top5_keys]
                    try:
                        new_choices = [input_dict['choices'][i] for i in selected_indices]
                        new_label = {str(i): label[str(i)] for i in selected_indices}
                        jobj = {
                            'original_context': result1['original_context'],
                            'original_choices': result1['original_choices'],
                            'original_label': result1['original_label'],
                            'perturbation_type':result1['perturbation_type'],
                            'context': input_dict['context'],
                            'choices': new_choices,
                            'label_score': new_label,
                            'label': 0,
                            'explanation':result1['explanation'],
                            'activity_label': result1['activity_label'],

                        }
                    except Exception as e:
                        print(e)
                        jobj = {
                            'original_context': result1['original_context'],
                            'original_choices': result1['original_choices'],
                            'original_label': result1['original_label'],
                            'perturbation_type':result1['perturbation_type'],
                            'context': input_dict['context'],
                            'choices': input_dict['choices'],
                            'label_score': input_dict['label'],
                            'label': 0,
                            'explanation':result1['explanation'],
                            'activity_label': result1['activity_label'],
                        }
                        with open(output_dir+"bad_cases.jsonl", 'w', encoding="utf8") as file:  #generate
                                json.dump(
                                    jobj,
                                    file,
                                    ensure_ascii=False
                                )
                                file.write("\n")
                        print('6选4bad case')
                        continue
                else:
                    try:
                        jobj = {
                                'original_context': result1['original_context'],
                                'original_choices': result1['original_choices'],
                                'original_label': result1['original_label'],
                                'perturbation_type':result1['perturbation_type'],
                                'context': result1['context'],
                                'choices': result1['choices'],
                                'label': result1['label'],
                                'explanation':result1['explanation'],
                                'activity_label':result1['activity_label'],
                            }
                    except Exception as e:
                        print(e)
                        print('bad case最终数据格式错误')
                        continue


                max_new_result_scene.append(jobj)

                if len(max_new_result_scene)%1 ==0:
                    with open(output_dir+"transformed_cases.jsonl", 'w', encoding="utf8") as file:  #generate
                        for line in max_new_result_scene:
                            json.dump(
                                line,
                                file,
                                ensure_ascii=False
                            )
                            file.write("\n")
                pbar.update(1)
                original_cases.remove(original_case_chosen[0])
            else:
                print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))
    


if __name__ == "__main__":
    fire.Fire(main)


