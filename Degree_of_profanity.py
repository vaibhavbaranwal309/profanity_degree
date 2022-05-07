import re
# assuming the new tweet file and
# racial slurs are given as input
# below input_filepath and racial_slurs are used as an example
racial_slurs = ['abc', 'xyz'] 
file = open("input_filepath", "w")
file.write("This is tweet one with slurs abc, abc, xyz, xyz. This is tweet two with slurs abc, xyz.This is tweet three with slurs abc.")
file.close()


file = open("input_filepath", "r")
text = " ".join([line.rstrip() for line in file]) # getting all the sentence from the file into a single string value
sentence_list = re.split(r' *[\.\?!][\'"\)\]]* *', text) # spliting of string text into sentences
file.close()


# The degree of profanity lies between 0 and 1
# 0 being the least profane and 1 being the highest

for sentence in sentence_list: # itterating to each sentence
    slur_count = 0 # initial profane count
    
    for words in racial_slurs:
        slur_count+=sentence.count(words) # total count of racial word in a sentence
    if len(sentence)!=0:
        
        profanity = slur_count/(len(sentence.split(" "))) # calculating degree of profanity
        
        f = open("output_filepath", "a") # outputing the result in a file
        f.write("{} || {} \n".format(sentence, round(profanity,3)))
        f.close()
        
        


f = open("output_filepath", "r") # the results are appended in the output file
for line in f:
    print(line)

f.close()



# This is tweet one with slurs abc, abc, xyz, xyz. || 0.4
# This is tweet two with slurs abc, xyz. || 0.25
# This is tweet three with slurs abc. || 0.14
