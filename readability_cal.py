'''
@author: wanzeyu

@contact: wan.zeyu@outlook.com

@file: readability_cal.py

@time: 2018/1/24 17:57
'''
import pickle

from textstat.textstat import textstat
from helper import get_parse

# acceptable = ["[NN]", "[VBD]", "[VBZ]", "[VBG]", "[VB]", "[NNP]", "[JJ]", "[JJR]", "[JJS]"]
acceptable = []
dict_file = open("repla_dict_v2.pkl", "rb")
repl_dict = pickle.load(dict_file)
uni_penny_mapping_target = open("uni_penny_mapping.pkl", "rb")
uni_penny_mapping = pickle.load(uni_penny_mapping_target)
for key in uni_penny_mapping:
    acceptable.append("[" + key + "]")
file_name = "beam_size_4_residual.txt"
parse_result = "parse.pkl"

dict_file.close()
uni_penny_mapping_target.close()

automatic_readability_index = 0
flesch_kincaid_readability = 0
automatic_readability_index_processed = 0
flesch_kincaid_readability_processed = 0


def get_replacement(sent):
    sent = sent.split()
    res = []
    for word in sent:
        if word in repl_dict:
            res.append(repl_dict[word][2])
        else:
            res.append(word)
    return " ".join(res)


def get_lexical_replacement(sent, parse_info):
    for lexical in repl_dict:
        try:
            position = sent.split().index(lexical.split()[0])
            items = repl_dict[lexical]
            for item in items:
                syntactic_category, paraphrase_score, simplification_score, output = item
                if float(paraphrase_score) >= 4.0 and syntactic_category in acceptable:
                    if syntactic_category.strip("[]") in uni_penny_mapping:
                        mapping = uni_penny_mapping[syntactic_category.strip("[]")]
                        uni_pos_tag = mapping[0]
                        uni_morph = mapping[1]
                        try:
                            sent_parse = parse_info[position]
                            if uni_pos_tag == sent_parse[3] and uni_morph in sent_parse[5]:
                                print(mapping)
                                print(sent_parse)
                                sent = sent.replace(lexical, output)
                                try:
                                    parse_info = get_parse(sent)
                                except Exception as e:
                                    print("network time out")
                                print("original:" + lexical)
                                print("repla:" + output)
                                print("==================")
                            elif syntactic_category in ["[VBD]", "[VBZ]", "[VBG]", "[VB]", "[NNP]", "[JJ]", "[JJR]",
                                                        "[JJS]"]:
                                pass
                                # print("===== unmatched result===")
                                # print(mapping)
                                # print(sent_parse)
                                # print("===== unmatched result===")
                        except IndexError:
                            print("out of index")
        except ValueError:
            pass
    return sent


line_count = 0
parse_list = pickle.load(open(parse_result, "rb"))
with open("replaced.txt", "w", encoding="utf8") as writer:
    with open(file_name, "r", encoding="utf8") as fp:
        for line in fp:
            # if line_count == 500:
            #     break
            automatic_readability_index += textstat.automated_readability_index(line)
            flesch_kincaid_readability += textstat.dale_chall_readability_score(line)
            replaced = get_lexical_replacement(line, parse_list[line_count])
            writer.write(replaced)
            writer.write("\n")
            automatic_readability_index_processed += textstat.automated_readability_index(replaced)
            flesch_kincaid_readability_processed += textstat.dale_chall_readability_score(replaced)
            line_count += 1
automatic_readability_index_avg_score = automatic_readability_index / line_count
flesch_kincaid_readability_avg_score = flesch_kincaid_readability / line_count
automatic_readability_index_processed_avg_score = automatic_readability_index_processed / line_count
flesch_kincaid_readability_processed_avg_score = flesch_kincaid_readability_processed / line_count
print(automatic_readability_index_avg_score)
print(flesch_kincaid_readability_avg_score)
print(automatic_readability_index_processed_avg_score)
print(flesch_kincaid_readability_processed_avg_score)
