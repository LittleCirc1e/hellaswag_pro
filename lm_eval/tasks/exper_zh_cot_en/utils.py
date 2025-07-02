from functools import partial


choices = [
    "A",
    "B",
    "C",
    "D",
]


def format_cot_example(example, including_answer=True):
    prompt = "问题：\n"
    question = example["context"]
    options = example["choices"]
    prompt += question + "\n"
    prompt += "选项：\n"
    for i, opt in enumerate(options):
        prompt += "{}. {}\n".format(choices[i], opt)
    if including_answer:
        prompt += example["cot_content"] + "\n\n"
    else:
        prompt += "答案：让我们一步步思考。"
    return prompt


doc_to_text = partial(format_cot_example, including_answer=False)
fewshot_to_text = partial(format_cot_example, including_answer=True)


def process_docs(dataset, subject):
    return dataset.filter(lambda x: x["perturbation_type"] == subject)


process_abductive_reasoning = partial(process_docs, subject="abductive_reasoning")
process_critical_thinking = partial(process_docs, subject="critical_thinking")
process_negative_testing = partial(process_docs, subject="negative_testing")
process_problem_reparagraphing = partial(process_docs, subject="problem_reparagraphing")
process_reverse_conversion = partial(process_docs, subject="reverse_conversion")
process_scene_transition = partial(process_docs, subject="scene_transition")
process_sentence_sorting = partial(process_docs, subject="sentence_sorting")
