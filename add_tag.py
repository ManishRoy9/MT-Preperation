#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Decoding the translation prediction
# Command: python3 desubword.py <target_model_file> <target_pred_file>


import sys
import sentencepiece as spm


source_model = sys.argv[1]
tag_model = sys.argv[2]
target_decodeded = source_model + ".en"


#sp = spm.SentencePieceProcessor()
#sp.load(target_model)


with open(source_model) as pred, open(target_decodeded, "w+") as pred_decoded:
    for line in pred:
        line = "<" + tag_model + "> " + line
        #line = sp.decode_pieces(line)
        pred_decoded.write(line)
        
print("Done desubwording! Output:", target_decodeded)
