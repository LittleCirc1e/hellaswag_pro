# HellaSwag-Pro: Official Repository for Evaluating the Robustness of LLMs in Commonsense Reasoning

[![Paper](https://img.shields.io/badge/paper-arXiv:2405.11393-red)](https://arxiv.org/abs/2405.11393)


## Introduction

This is the official repository for the paper **[HellaSwag-Pro: A Large-Scale Bilingual Benchmark for Evaluating the Robustness of LLMs in Commonsense Reasoning](https://arxiv.org/abs/2405.11393)**.

Large Language Models (LLMs) have demonstrated remarkable capabilities on standard commonsense reasoning benchmarks. However, it remains unclear whether this performance stems from a genuine understanding of commonsense knowledge or from memorizing superficial patterns in their training data.

To investigate this, we introduce **HellaSwag-Pro**, a large-scale, bilingual (Chinese and English) benchmark designed to systematically evaluate the robustness of LLMs. This repository provides:
1.  Scripts for loading and evaluating models on the **HellaSwag-Pro** benchmark.
2.  The **Chinese HellaSwag** dataset, a new high-quality dataset with 12,000 instances for Chinese commonsense reasoning.
3.  A comprehensive framework to reproduce the evaluation of 41 LLMs as reported in our paper.

## ✨ Key Features

*   **Large-Scale Bilingual Benchmark**: HellaSwag-Pro contains 11,200 high-quality, human-verified evaluation instances in both Chinese and English.
*   **Systematic Robustness Evaluation**: Features 7 meticulously designed question variants to challenge a model's reasoning capabilities from different cognitive angles.
*   **High-Quality Chinese Dataset**: Introduces **Chinese HellaSwag**, a new dataset covering 56 fine-grained categories, addressing the lack of such resources in Chinese.
*   **Comprehensive Model Support**: Built on the `lm-evaluation-harness`, our framework is easily extensible and supports evaluation for a wide range of open-source and proprietary models.
*   **Reproducible Experiments**: Provides all necessary scripts and detailed instructions to reproduce the findings from our paper.

## 📊 The HellaSwag-Pro Benchmark

HellaSwag-Pro tests whether a model truly grasps the underlying commonsense knowledge by presenting the same core problem in 7 different reasoning formats.

| Variant Type                  | Core Capability Tested                                           |
| ----------------------------- | ---------------------------------------------------------------- |
| **Problem Restatement**       | Understanding of surface-level textual variations                |
| **Reverse Conversion**        | Abductive reasoning (inferring cause from effect)                |
| **Causal Inference**          | Understanding of the underlying causality of events              |
| **Sentence Ordering**         | Grasp of logical and temporal event sequences                    |
| **Scenario Refinement**       | Counterfactual reasoning                                         |
| **Negative Transformation**   | Understanding of negation (selecting the *least* plausible option) |
| **Critical Testing**          | Critical thinking and the ability to abstain when info is lacking|

## 🚀 Quick Start

### 3. Model Evaluation

We use the `lm-evaluation-harness` for evaluation. 

#### Example

```bash
python lm_eval --model vllm --model_args pretrained=YOUR_MODEL_PATH,parallelize=True --tasks exper_zh_cot_en_abductive_reasoning --batch_size 8 --log_samples --num_fewshot 0 --output_path YOUR_OUTPUT_PATH

```


#### Supported Tasks (`--tasks`)

*   `cn_hellaswag`: Base evaluation on the Chinese HellaSwag dataset.
*   `exper_original_cn/exper_original_en`: Evaluate on the original problem of HellaSwag-Pro using the direct prompt.
*   `exper_robust_cn/exper_robust_en`: Evaluate on the transformed problem of HellaSwag-Pro using the direct prompt.
*   `exper_zh_cot/exper_zh_cot_en`: Evaluate on the transformed problem of HellaSwag-Pro using the Chinese CoT prompt.
*   `exper_en_cot/exper_en_cot_en`: Evaluate on the transformed problem of HellaSwag-Pro using the English CoT prompt.
*   `exper_en_xlt/exper_zh_xlt`: Evaluate on the transformed problem of HellaSwag-Pro using the translation (XLT) prompt.


## Citation

If you use our work in your research, please cite our paper:

```bibtex
@misc{li2024hellaswagpro,
      title={HellaSwag-Pro: A Large-Scale Bilingual Benchmark for Evaluating the Robustness of LLMs in Commonsense Reasoning}, 
      author={Xiaoyuan Li and Moxin Li and Rui Men and Yichang Zhang and Keqin Bao and Wenjie Wang and Fuli Feng and Dayiheng Liu and Junyang Lin},
      year={2024},
      eprint={2405.11393},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
