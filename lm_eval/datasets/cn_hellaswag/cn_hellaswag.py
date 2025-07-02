import json
import datasets

class CnHellaswagzhongjiConfig(datasets.BuilderConfig):
    def __init__(self, script_path=None, **kwargs):
        super().__init__(**kwargs)
        self.script_path = script_path

class CnHellaswagzhongji(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        CnHellaswagzhongjiConfig(
            name="education_short",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="education_medium",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="education_long",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="home_short",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="home_medium",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="home_long",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="traffic_short",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="traffic_medium",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="traffic_long",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="leisure_short",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="leisure_medium",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="leisure_long",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="work_short",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="work_medium",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="work_long",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="health_short",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="health_medium",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="health_long",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="social_short",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="social_medium",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="social_long",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="shopping_short",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="shopping_medium",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
        CnHellaswagzhongjiConfig(
            name="shopping_long",
            version=datasets.Version("1.0.0"),
            script_path="/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/cn_hellaswag.py"
        ),
    ]

    def _split_generators(self, dl_manager):
        base_path = "/mnt/data/lanlin.lxy/lm-evaluation-harness/lm_eval/datasets/cn_hellaswag/data"
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
                    "id": id_,
                    "context": data["context"],
                    "choices": data["choices"],
                    "label": data["label"],
                    "broad_type": data["broad_type"],
                    "detailed_type": data["detailed_type"],
                }
    def _info(self):
        return datasets.DatasetInfo(
            description=self.config.description,
            features=datasets.Features(
                {
                    "id": datasets.Value("int32"),
                    "context": datasets.Value("string"),
                    "choices": datasets.Sequence(datasets.Value("string")),
                    "label": datasets.Value("int32"),
                    "broad_type": datasets.Value("string"),
                    "detailed_type": datasets.Value("string"),
                }
            ),
            supervised_keys=None,
        )


