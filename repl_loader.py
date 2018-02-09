'''
@author: wanzeyu

@contact: wan.zeyu@outlook.com

@file: repl_loader.py

@time: 2018/1/24 17:38
'''
import string
import pickle
import collections
from helper import get_parse


def replace_loader_v1():
    """
    load original simplification list
    :return:
    """
    res = {}
    with open("replacement.txt", "r", encoding="utf8") as fp:
        for line in fp:
            items = line.split("	")
            if items[0] not in string.ascii_letters:
                res[items[0].strip()] = items[1].strip().split(",")
    with open("repla_dict.pkl", "wb") as writer:
        pickle.dump(res, writer)


def replace_loader_v2():
    """
    load simple ppdb
    :return:
    """
    res = collections.defaultdict(list)
    with open("simplification-dictionary", "r") as fp:
        for line in fp:
            paraphrase_score, simplification_score, syntactic_category, input_phrase, output_phrase = line.split("\t")
            # res[input_phrase, syntactic_category] = (paraphrase_score, simplification_score, output_phrase.strip())
            res[input_phrase].append(
                (syntactic_category, paraphrase_score, simplification_score, output_phrase.strip()))
    with open("repla_dict_v2.pkl", "wb") as writer:
        pickle.dump(res, writer)


def get_all_parse():
    """
    get all syntaxnet parse result and save
    :return:
    """
    res = []
    with open("beam_size_4_residual.txt", "r", encoding="utf8") as fp:
        for line in fp:
            try:
                tmp = get_parse(line.strip())
            except:
                tmp = "null"
            res.append(tmp)
    with open("parse.pkl", "wb") as writer:
        pickle.dump(res, writer)


def load_mapping():
    """
    load universal denpendency to penny mapping and save
    :return:
    """
    res_dict = {}
    with open("uni_penny_mapping.txt", "r", encoding="utf8") as fp:
        for line in fp:
            items = line.split("\t")
            penny_tag, uni_tag, uni_morph = items[0], items[2], items[3]
            res_dict[penny_tag] = (uni_tag, uni_morph)
    with open("uni_penny_mapping.pkl", "wb") as writer:
        pickle.dump(res_dict, writer)


if __name__ == "__main__":
    replace_loader_v2()
    load_mapping()
