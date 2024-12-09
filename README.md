# Robustness Evaluation of the German Extractive Question Answering Task

Authors: Shalaka Satheesh, Katharina Beckh, Katrin Klug, Héctor Allende-Cid, Sebastian Houben, Teena Hassan

# Paper Abstract

To ensure reliable performance of Question Answering (QA) systems, evaluation of robustness is crucial.  Common evaluation benchmarks only include predictive performance metrics, such as Exact Match and the F1 score. However, these benchmarks overlook critical factors for the deployment of QA systems. This oversight can result in systems vulnerable to minor perturbations in the input such as typographical errors. While several methods have been proposed to test the robustness of QA models, there has been minimal exploration of these approaches for languages other than English. This study focuses on the robustness evaluation of German language QA models, extending methodologies previously applied primarily to English. The objective is to nurture the development of robust models by defining an evaluation method specifically tailored for the German language. We assess the applicability of perturbations used in English QA models for German and perform a comprehensive experimental evaluation with eight models. The results show that all models are vulnerable to character level perturbations. Additionally, the comparison of monolingual and multilingual models suggest that the former models are less affected by character and word level perturbations. 

## In this repository:

Code to run the experiments listed in the paper. See [README.md](./src/README.md) for instructions on how to run the experiments. 

    .
    ├── README.md
    └── src
        ├── convert_to_jsonl.py
        ├── environment.yml
        ├── main.py
        ├── perturb.py
        ├── qa_inference
        │   ├── compute_scores.py
        │   ├── __init__.py
        │   ├── predict.py
        │   └── utils.py
        ├── qa_perturb
        │   ├── chara_perturb
        │   │   ├── change_case.py
        │   │   ├── delete_chara.py
        │   │   ├── delete_punct.py
        │   │   ├── __init__.py
        │   │   ├── insert_chara.py
        │   │   ├── insert_punct.py
        │   │   ├── keyboard_typo.py
        │   │   ├── new_peturb.py
        │   │   ├── README.md
        │   │   ├── repeat_chara.py
        │   │   ├── replace_chara.py
        │   │   ├── replace_umlaute.py
        │   │   └── swap_chara.py
        │   ├── __init__.py
        │   ├── README.md
        │   ├── sentence_perturb
        │   │   ├── back_translate.py
        │   │   ├── __init__.py
        │   │   ├── new_peturb.py
        │   │   ├── README.md
        │   │   └── repeat_sentence.py
        │   └── word_perturb
        │       ├── delete_word.py
        │       ├── __init__.py
        │       ├── new_peturb.py
        │       ├── README.md
        │       ├── repeat_word.py
        │       ├── split_word.py
        │       ├── swap_words.py
        │       └── synonym.py
        ├── README.md
        ├── squad
        │   ├── app.py
        │   ├── compute_score.py
        │   ├── README.md
        │   ├── requirements.txt
        │   └── squad.py
        └── utils
            ├── get_tokens.py
            ├── initialise_models.py
            └── __init__.py

    8 directories, 47 files


# Code References:
1. Tunstall, L. & Chaumond, J. (May 2022). SQuAD metric. [HuggingFace Spaces](https://huggingface.co/spaces/evaluate-metric/squad/blob/main/squad.py).
2.  Kumar, R. (Sep 2022). typo. [GitHub](https://github.com/ranvijaykumar/typo)
3. Yorke, A. (Dec 2016). butter-fingers. [GitHub](https://github.com/alexyorke/butter-fingers/blob/master/butterfingers/butterfingers.py)

# Citation:
Please cite our paper as below:
```
@InProceedings{ 
title={Robustness Evaluation of the German Extractive Question Answering Task},
author={Shalaka Satheesh and Katharina Beckh and Katrin Klug and Héctor Allende-Cid and Sebastian Houben and Teena Hassan},
}
```
