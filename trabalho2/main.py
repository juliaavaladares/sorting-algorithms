
from index import *


if __name__ == "__main__":
    keywords = input("Informe as palavras chaves: ").split()
    filename = input(
        "Informe o arquivo a ser testado. Lembrado que deve estar dentro da pasta testes: ")

    L = len(keywords[0])

    avl_tree, hash_table = create_index(keywords, L)
    avl_tree.export_to_graphviz("resultados/avl_tree.dot")
    hash_table.display()

    with open("testes/"+filename, "r") as file:
        linha = 0
        dict_keywords = {}
        for line in file:
            linha = linha + 1
            for word in line.split():
                if avl_tree.search(word) is not None:
                    if word not in dict_keywords:
                        dict_keywords[word] = []
                    dict_keywords[word].append(linha)

    myKeys = list(dict_keywords.keys())
    myKeys.sort()
    sorted_dict = {i: dict_keywords[i] for i in myKeys}
    print(sorted_dict)
    # export_result(sorted_dict)
