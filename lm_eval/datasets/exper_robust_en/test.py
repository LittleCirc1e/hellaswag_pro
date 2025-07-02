import json
def filter_choices_not_four_to_file(input_filename, output_filename):
    """
    读取文件的每一行，将choices不是四个元素的条目写入新文件
    
    :param input_filename: 输入JSON Lines文件的路径
    :param output_filename: 输出文件的路径
    """
    with open(input_filename, 'r', encoding='utf-8') as infile, \
         open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            entry = json.loads(line)
            if len(entry.get('choices', [])) != 4:
                outfile.write(json.dumps(entry, ensure_ascii=False) + '\n')

# 使用示例
input_filename = '/cpfs01/user/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/exper_robust_en/data/reverse_conversion1.jsonl'  # 替换为你的输入文件路径
output_filename = '/cpfs01/user/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/exper_robust_en/data/reverse_conversion2.jsonl'  # 替换为你的输出文件路径
filter_choices_not_four_to_file(input_filename, output_filename)