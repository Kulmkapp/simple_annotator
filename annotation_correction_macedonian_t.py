#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import re
# import sys
"""
words = dict()
count = 0
with open("corpus_s") as f:
    for line in f.readlines():
        things = line.split("\t")
        words[count] = things
        count += 1

the script processes the input file where:

the first column (index 0) is the original text (with the underscore) - FULL
the second column (index 1) is the diplomatic transcript - DIPLOMATIC
the third column (index 2) is the morphological tag - TAG
the fourth column (index 3) is for PoS - POS
the fifth column (index 4) is for comments - COMMENT
the sixth column (index 5) is the lemma - LEMMA

Example:
"""
print("Please enter the name of the file for correction (with the extension) and press enter:\t")
stfile = input("")

new_entry = True

while new_entry:
    print("\n\n")
    text_file_output = codecs.open("Output_tmp.txt", "w", "utf-8")
    stinput = codecs.open(stfile, "r", "utf-8")
    print("Please enter keyword from the diplomatic column and press enter:\t")
    diplomatic_word = input("")
    print("Please enter word for replacement in morphological tag and press enter:\t")
    morph_tag = input("")
    print("Please enter word for replacement in POS and press enter:\t")
    POS_tag = input("")
    print("Please enter word for replacement in lemma and press enter:\t")
    lemma = input("")

    for line in stinput:
        if len(line) > 0:
            items = line.split("\t")
            if len(items) > 4:
                # if the word you typed matches the word in the diplomatic column it creates a new output line
                # with the words you corrected
                if items[1] == diplomatic_word:
                    line_output = items[0] + '\t' + items[1] + '\t' + morph_tag + '\t' + items[2] + '\t' + POS_tag \
                                  + '\t' + items[3] + '\t' + lemma
                    print(line_output)
                # all the other lines, eg. if the word does not match the diplomatic, it outputs the line unchanged
                else:
                    line_output = line
            else:
                line_output = line
            line_output: str = re.sub('\r\n', "", line_output)
            line_output = re.sub("\n", "", line_output)
            line_output += "\r\n"
            text_file_output.write(line_output)

    text_file_output.close()
    stinput.close()

    os.remove(stfile)
    os.rename("Output_tmp.txt", stfile)
    tmp_var = input("New entry? enter 0 for No, anything else for Yes>\t")
    if tmp_var != '0':
        new_entry = True
    else:
        new_entry = False

# print line.encode('utf-8')
# if re.match('4', line):
# 	count +=1
# print count
