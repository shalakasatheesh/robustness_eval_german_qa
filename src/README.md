# Run evaluation experiments

## Create and activate conda environment

    conda env create --name env_name --file environment.yml
    conda activate env_name

## Run evaluation on GermanQuAD test data

    python -m main \
    --model_name deepset/xlm-roberta-base-squad2 \
    --path_to_dataset <path_name> \
    --folder_to_save_results <path_name> \
    --data_type german_quad

## Run evaluation on perturbed data

    python -m main \
    --model_name deepset/xlm-roberta-base-squad2 \
    --path_to_dataset <path_name> \
    --folder_to_save_results <path_name> \
    --data_type delete_chara_verb

# To create perturbed data

1. [Create](./qa_perturb/README.md) desired pertubation by editing `perturb.py`

2. Run the edited file to apply desired perturbation on data

        python -m perturb

3. Convert file to SQuAD format. File type will be `.jsonl`.

        python convert_to_jsonl.py \
        --input_filename <path_name>
        