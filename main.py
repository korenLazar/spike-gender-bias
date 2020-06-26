import pandas as pd
import numpy as np
from glob import glob
from functools import reduce
from django.utils.text import slugify


def find_filenames_by_suffix(suffix='tsv'):
    return [file for file in glob(f"results/*.{suffix}")]


def find_filenames_by_prefix(prefix):
    return [file for file in glob(f"results/{prefix}*")]


def get_sentences_indices(df):
    return df['sentence_id'].values


if __name__ == '__main__':
    sents_indices = list()
    # tsv_filenames = find_filenames_by_prefix("'the-e1etnnnnplawyer")
    tsv_filenames = find_filenames_by_suffix()
    for filename in tsv_filenames:
        df = pd.read_csv(filename, sep='\t')
        indices = get_sentences_indices(df)
        print(f"The number of sentences in {str(filename)} is {len(np.unique(indices))}")
        sents_indices.append(indices)
    union_of_indices = reduce(np.union1d, sents_indices)
    print(f"The total number of sentences that were found in all queries is {union_of_indices.shape[0]}")
