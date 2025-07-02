import json
import datasets

class exper_robust_zhConfig(datasets.BuilderConfig):
    def __init__(self, script_path=None, **kwargs):
        super().__init__(**kwargs)
        self.script_path = script_path

class exper_robust_zh(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        exper_robust_zhConfig(
            name="abductive_reasoning",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/exper_robust_zh/exper_robust_zh.py"
        ),
        exper_robust_zhConfig(
            name="critical_thinking",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/exper_robust_zh/exper_robust_zh.py"
        ),
        exper_robust_zhConfig(
            name="negative_testing",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/exper_robust_zh/exper_robust_zh.py"
        ),
        exper_robust_zhConfig(
            name="scene_transition",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/exper_robust_zh/exper_robust_zh.py"
        ),
        exper_robust_zhConfig(
            name="sentence_sorting",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/exper_robust_zh/exper_robust_zh.py"
        ),
        exper_robust_zhConfig(
            name="reverse_conversion",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/exper_robust_zh/exper_robust_zh.py"
        ),
        exper_robust_zhConfig(
            name="problem_reparagraphing",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/exper_robust_zh/exper_robust_zh.py"
        ),

    ]

    def _split_generators(self, dl_manager):
        base_path = "/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/exper_robust_zh/data"
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={
                    "filepath": f"{base_path}/{self.config.name}.jsonl",
                },
            ),
        ]

    def _generate_examples(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            for id_, line in enumerate(f):
                data = json.loads(line)
                
                yield id_, {
                    "uid": id_,
                    "id": data["id"],
                    "original_context": data["original_context"],
                    "original_choices": data["original_choices"],
                    "original_label": data["original_label"],
                    "context": data["context"],
                    "choices": data["choices"],
                    "label": data["label"],
                    "perturbation_type":data["perturbation_type"],
                }
    def _info(self):
        return datasets.DatasetInfo(
            features=datasets.Features(
                {
                    "uid": datasets.Value("int32"),
                    "id": datasets.Value("int32"),
                    "original_context": datasets.Value("string"),
                    "original_choices": datasets.Sequence(datasets.Value("string")),
                    "original_label": datasets.Value("int32"),
                    "context": datasets.Value("string"),
                    "choices": datasets.Sequence(datasets.Value("string")),
                    "label": datasets.Value("int32"),
                    "perturbation_type": datasets.Value("string"),
                }
            ),
            supervised_keys=None,
        )


