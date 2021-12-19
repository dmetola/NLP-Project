import spacy
import json, jsonmerge
from jsonmerge import merge
import collections
from collections import Counter

nlp = spacy.load('en_core_web_lg')

file_name = "Beowulf-translated-tolkien.txt"
text = open(file_name).read()
doc = nlp(text)

def word_frequency():
    """Returns 100 most frequent words, and unique word cases"""
    words = [token.text for token in doc if not token.is_stop if not token.tag_ in ["CD", "_SP"] and not token.is_punct]
    word_freq = Counter(words)
    common_words = word_freq.most_common(100)
    unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
    with open("word-frequency.txt", "w") as file:
        file.write(str(common_words))
        file.write("\n" + str(unique_words))

def ents_pos():
    """Recognises NER from text file and outputs it into JSON"""
    ents_file = open("Beowulf-ents.json", "w")
    ents = [{"TOKEN":ent.text, "LABEL":ent.label_, "DEF":spacy.explain(ent.label_)} for ent in doc.ents]
    json.dump(ents, ents_file, indent=6)
    pos_file = open("Beowulf-pos.json", "w")
    pos = [{"POS":token.pos_, "TAG":token.tag_, "STOPWORD":token.is_stop} for token in doc]
    json.dump(pos, pos_file, indent=6)
    #Section to merge both dictionaries into one
    ents_pos = merge(ents, pos)
    ents_pos_file = open("Beowulf_ents_pos.json", "w")
    json.dump(ents_pos, ents_pos_file, indent=6)
    
# word_frequency()
ents_pos()
