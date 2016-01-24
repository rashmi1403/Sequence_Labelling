"""hw3_corpus_tools.py: CSCI544 Homework 3 Corpus Code

USC Computer Science 544: Applied Natural Language Processing

Provides two functions and two data containers:
get_utterances_from_file - loads utterances from an open csv file
get_utterances_from_filename - loads utterances from a filename
DialogUtterance - A namedtuple with various utterance attributes
PosTag - A namedtuple breaking down a token/pos pair

This code is provided for your convenience. You are not required to use it.
Feel free to import, edit, copy, and/or rename to use in your assignment.
Do not distribute."""

__author__ = "Christopher Wienberg"
__email__ = "cwienber@usc.edu"

from collections import namedtuple
import csv
import glob
import os
from sys import argv
from os import walk

def get_utterances_from_file(dialog_csv_file):
    """Returns a list of DialogUtterances from an open file."""
    reader = csv.DictReader(dialog_csv_file)
    return [_dict_to_dialog_utterance(du_dict) for du_dict in reader]

def get_utterances_from_filename(dialog_csv_filename):
    """Returns a list of DialogUtterances from an unopened filename."""
    with open(dialog_csv_filename, "r") as dialog_csv_file:
        return get_utterances_from_file(dialog_csv_file)

DialogUtterance = namedtuple(
    "DialogUtterance", ("act_tag", "speaker", "pos", "text"))

DialogUtterance.__doc__ = """\
An utterance in a dialog. Empty utterances are None.

act_tag - the dialog act associated with this utterance
speaker - which speaker made this utterance
pos - a list of PosTag objects (token and POS)
text - the text of the utterance with only a little bit of cleaning"""

PosTag = namedtuple("PosTag", ("token", "pos"))

PosTag.__doc__ = """\
A token and its part-of-speech tag.

token - the token
pos - the part-of-speech tag"""

def _dict_to_dialog_utterance(du_dict):
    """Private method for converting a dict to a DialogUtterance."""

    # Remove anything with 
    for k, v in du_dict.items():
        if len(v.strip()) == 0:
            du_dict[k] = None

    # Extract tokens and POS tags
    if du_dict["pos"]:
        du_dict["pos"] = [
            PosTag(*token_pos_pair.split("/"))
            for token_pos_pair in du_dict["pos"].split()]
    return DialogUtterance(**du_dict)


################## My Program ######################################

inputf1 = argv[1]       #input file

utterances = get_utterances_from_filename(inputf1)

i = 1
prev_speaker = ""
for utterance in utterances:
    output_str = ""
    speaker = ""
    
    dict_uttr = {}
    dict_uttr = utterance

    
        

    #Appending the dialogue act 
    if(dict_uttr[0] != None):
        output_str += dict_uttr[0] + "\t"
    else:
        output_str += "UNK" + "\t"
    speaker = dict_uttr[1]

    #Checking if its the first utterance
    if(i == 1):
        output_str += "FIRST_UTR" + "\t"
        i = i + 10
    else:   
        #Checking if the speaker has changed       
        if(str(speaker) != str(prev_speaker)):
            output_str += "SPEAKER_CHANGED" + "\t"  

    #For tokens and pos
    if(dict_uttr[2] != None and dict_uttr[3] != None):
        pos_list = []
        pos_list = dict_uttr[2]
        for lst in pos_list:
            dict_pos = {}
            dict_pos = lst
            #print(dict_pos[0] + " " + dict_pos[1])
            if(dict_pos[0] == ":"):
                output_str += "TOKEN_COLON" + "\t"
            elif(dict_pos[0] == "\\"):
                output_str += "TOKEN_BACKSLASH" + "\t"
            else:
                output_str += "TOKEN_" + dict_pos[0] + "\t"
            
            if(dict_pos[1] == ":"):
                output_str += "POS_COLON" + "\t"
            elif(dict_pos[1] == "\\"):
                output_str += "POS_BACKSLASH" + "\t"
            else:
                output_str += "POS_"   + dict_pos[1] + "\t"
            

    #For tokens only 
    if(dict_uttr[2] == None and dict_uttr[3] != None):
        sentence = dict_uttr[3]
        tkn_lst = sentence.split(" ")
        for word in tkn_lst:
            output_str += "TOKEN_" + word + "\t"
        


    #assigning prev speaker before the iteration ends
    prev_speaker = speaker

    print(output_str)
print("")


#print("Finished Processing!")












