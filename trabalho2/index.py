from avlTree import *
from hashTable import *
import pandas as pd


def create_index(keywords, L):
    avl_tree = AVLTree()
    hash_table = HashTable(10)

    for keyword in keywords:
        keyword = keyword.strip().ljust(L, " ")

        avl_tree.insert(keyword)
        hash_table.insert(keyword)

    return avl_tree, hash_table


def export_result(dict):
    df = pd.DataFrame.from_dict([dict])
    df.to_csv('resultados/result_avl.txt', header=False, index=True, mode='a')
