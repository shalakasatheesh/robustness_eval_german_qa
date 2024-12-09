import random
from datasets import load_dataset
import json
import pandas as pd
import os 
import argparse

from qa_perturb.chara_perturb import InsertChara, DeleteChara, RepeatChara, ReplaceChara, \
    SwapChara, DeletePunctuation, ChangeCase, ReplaceUmlaute, KeyboardTypo, InsertPunctuation
from qa_perturb.word_perturb import RepeatWord, DeleteWord, SplitWord, Synonym, SwapWords
from qa_perturb.sentence_perturb import BackTranslate, RepeatSentence

def main(max_perturbs=1, folder='delete_chara'):
    random.seed(42)
    
    # load data
    data = load_dataset("deepset/germanquad", split="test")

    # perturb data
    max_perturbs = int(max_perturbs)
    folder = folder
    data_field = 'context'
    Perturbation =  InsertChara(data, data_field=data_field, 
                                max_perturbs=max_perturbs, max_words=1, 
                                length_of_word_to_perturb=2,  
                                pos_tag=None) 
    output = Perturbation.insert_chara()
    
    # path to save output file with perturbations
    PARENT_DIR = 'path_name' # write the path to your parent directory here
    DIRECTORY = 'path_name' # write the path to results directory
    FILE_NAME = Perturbation.name+'_'+Perturbation.data_field+'_'+str(max_perturbs)+'_charas.json' 
    DIR_PATH = os.path.join(PARENT_DIR, DIRECTORY)

    try:
        os.mkdir(DIR_PATH)
    except OSError:
        pass 
    PATH = os.path.join(DIR_PATH, FILE_NAME)
    with open(PATH, "w", encoding='utf8') as f:
        f.write(json.dumps(output[0], ensure_ascii=False))

    print("Saved perturbed data at "+PATH)

    # unaltered questions/contexts
    print(output[1])

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument('--max_perturbs', help='enter max perturbs name', default=1, required=False)
   parser.add_argument('--folder', help='enter folder name', default="delete_chara", required=False)
   args = parser.parse_args()
   main(args.max_perturbs, args.folder)