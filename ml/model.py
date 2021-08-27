import pandas as pd
from sklearn.metrics import pairwise_distances
import numpy as np
import pickle
import os


def bag_of_words(doc_id, num_results):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    data = pd.read_csv(dir_path + "\\data.csv")

    with open(dir_path + '\\title_features.pickle', 'rb') as file:
        title_features = pickle.load(file)

    pairwise_dist = pairwise_distances(title_features, title_features[doc_id])

    indices = np.argsort(pairwise_dist.flatten())[0:num_results]

    return indices


def avg_w2v_model(doc_id, num_results):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    data = pd.read_csv(dir_path + "\\data.csv")

    with open(dir_path + '\\arr.npy', 'rb') as file:
        w2v_title = np.load(file)

    pairwise_dist = pairwise_distances(w2v_title, w2v_title[doc_id].reshape(1, -1))

    indices = np.argsort(pairwise_dist.flatten())[0:num_results]

    pdists = np.sort(pairwise_dist.flatten())[0:num_results]

    df_indices = list(data.index[indices])

    return df_indices

# print(avg_w2v_model(10, 10))
