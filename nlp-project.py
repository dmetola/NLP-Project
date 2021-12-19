import spacy
import json
import collections
from collections import Counter

nlp = spacy.load('en_core_web_lg')

file_name = "Beowulf-translated-tolkien.txt"
text = open(file_name).read()
doc = nlp(text)

def word_frequency():
    words = [token.text for token in doc if not token.is_stop if not token.tag_ in ["CD", "_SP"] and not token.is_punct]
    word_freq = Counter(words)
    common_words = word_freq.most_common(100)
    unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
    with open("word-frequency.txt", "w") as file:
        file.write(str(common_words))
        file.write("\n" + str(unique_words))

#Esto es una prueba

def ents_pos():
    """Recognises NER from text file and outputs it into JSON"""
    ents_file = open("Beowulf-ents-pos.json", "w")
    ents = [{"TOKEN":ent.text, "LABEL":ent.label_, "DEF":spacy.explain(ent.label_)} for ent in doc.ents]
    pos = [{"POS":token.pos_, "TAG":token.tag_, "STOPWORD":token.is_stop} for token in doc]
    #Section to merge both dictionaries into one
    ents_pos = {}
    for k in set(k for d in ents_pos for k in d):
        ents_pos[k] = [d[k] for d in dicts if k in d]
    json.dump(ents_pos, ents_file, indent=6)
    # print(ents)
    
word_frequency()
ents_pos()
