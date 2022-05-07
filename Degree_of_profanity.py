import re

file = open('filepath','r') # opening the file

racial_slurs = [] # list of racial slurs

text = " ".join([line.rstrip() for line in file]) # getting all the sentence from the file into a single string value

sentence_list = re.split(r' *[\.\?!][\'"\)\]]* *', text) # spliting of string text into sentences


# The degree of profanity lies between 0 and 1
# 0 being the least profane and 1 being the highest

for sentence in sentence_list: # itterating to each sentence
    count = 0 # initial profane count
    
    for words in racial_slurs:
        count+=sentence.count(words) # total count of racial word in a sentence
    if len(sentence)!=0:
        
        profanity = count/(len(sentence.split(" "))) # calculating degree of profanity
        print(sentence.strip(),end=" || ")
        print("Profanity = {}".format(round(profanity,3))) # output
        print()
file.close()