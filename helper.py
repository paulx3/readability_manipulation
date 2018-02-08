'''
@author: wanzeyu

@contact: wan.zeyu@outlook.com

@file: helper.py

@time: 2018/1/30 22:28
'''
import requests
import json


def parse_result(text):
    res = []
    lines = text.strip().split("\n")
    for line in lines:
        line_id, form, lemma, upos_tag, x_pos_tag, feats, head, deprel, deps, misc = line.split()
        res.append((line_id, form, lemma, upos_tag, x_pos_tag, feats, head, deprel, deps, misc))
    return res


def get_parse(sent):
    print(sent)
    r = requests.post("http://syntaxnet.askplatyp.us/v1/parsey-universal-full",
                      data=json.dumps(sent))
    return parse_result(r.text)


if __name__ == "__main__":
    test_sent = "a bike with a clock hanging on the seat of the seat seat is attached half into a parking lot with a plane on his and a bicycle"
    print(get_parse(test_sent))
