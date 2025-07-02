"""
Take in a YAML, and output all other splits with this YAML
"""

import argparse
import os

import yaml
from tqdm import tqdm

from lm_eval.utils import eval_logger


SUBJECTS = {
    "abductive_reasoning": "",
    "critical_thinking": "",
    "negative_testing": "",
    "problem_reparagraphing": "",
    "reverse_conversion": "",
    "scene_transition": "",
    "sentence_sorting": "",
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_yaml_path",  default="_default_template_yaml")
    parser.add_argument("--save_prefix_path", default="exper_robust_en")
    parser.add_argument("--cot_prompt_path", default=None)
    parser.add_argument("--task_prefix", default="")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    # get filename of base_yaml so we can `"include": ` it in our other YAMLs.
    base_yaml_name = os.path.split(args.base_yaml_path)[-1]
    with open(args.base_yaml_path, encoding="utf-8") as f:
        base_yaml = yaml.full_load(f)

    if args.cot_prompt_path is not None:
        import json

        with open(args.cot_prompt_path, encoding="utf-8") as f:
            cot_file = json.load(f)

    for subject_eng, subject_zh in tqdm(SUBJECTS.items()):
        yaml_dict = {
            "include": base_yaml_name,
            "task": f"exper_robust_en_{args.task_prefix}_{subject_eng}"
            if args.task_prefix != ""
            else f"exper_robust_en_{subject_eng}",
            "dataset_name": subject_eng,
        }

        file_save_path = args.save_prefix_path + f"_{subject_eng}.yaml"
        eval_logger.info(f"Saving yaml for subset {subject_eng} to {file_save_path}")
        with open(file_save_path, "w", encoding="utf-8") as yaml_file:
            yaml.dump(
                yaml_dict,
                yaml_file,
                width=float("inf"),
                allow_unicode=True,
                default_style='"',
            )

    # write group config out

    group_yaml_dict = {
        "group": "exper_robust_en",
        "task": [
            (
                f"exper_robust_en_{args.task_prefix}_{subject_eng}"
                if args.task_prefix != ""
                else f"exper_robust_en_{subject_eng}"
            )
            for subject_eng in SUBJECTS.keys()
        ],
        "aggregate_metric_list": [
            {"metric": "acc", "aggregation": "mean", "weight_by_size": True},
            {"metric": "acc_norm", "aggregation": "mean", "weight_by_size": True},
        ],
        "metadata": {"version": 0.0},
    }

    file_save_path = "_" + args.save_prefix_path + ".yaml"

    with open(file_save_path, "w", encoding="utf-8") as group_yaml_file:
        yaml.dump(
            group_yaml_dict,
            group_yaml_file,
            width=float("inf"),
            allow_unicode=True,
            default_style='"',
        )
