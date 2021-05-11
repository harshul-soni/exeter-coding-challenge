       
import time
start_time=time.time();


file = open(r"E:\exetermedia\t8.shakespeare.txt")

line = file.read()
file.close()


import re


# def find_replace_multi(text,d):
#     for item in d.keys():
#         # sub item for item's paired value in string
        
#         string = re.sub(item, dictionary[item], string)
#     return string

# find_replace_multi(text, d)


def countFrequency(text,d):
    for key in d:
        with open("t8.shakespeare.txt") as file:
            for line in file:
                for word in line.split():
                    if key == word:
                        d[key]= d[key]+1








    

def multiwordReplace(text, wordDic):
    """
    take a text and replace words that match a key in a dictionary with
    the associated value, return the changed text
    """
    rc = re.compile('|'.join(map(re.escape, wordDic)))
    def translate(match):
        return wordDic[match.group(0)]
    return rc.sub(translate, text)



import csv
reader = csv.reader(open(r'E:\exetermedia\french_dictionary.csv', 'r'))
mydict = {}
for row in reader:
   k, v = row
   mydict[k] = v
   



str2 = multiwordReplace(line, mydict)




f = open(r'E:\exetermedia\shakespeare_translated.txt', "w")
f.write(str2)
f.close()


d = {}
with open("find_words.txt") as f:
    for line in f:
       key = line.rstrip("\n")
       d[key] = 0
       


countFrequency(f,d)



#writing to csv 
import csv

fields= ['English word','French word','Frequency']

rows=[]

for key in d:
    rows.append([[key,mydict[key],d[key]]])
    



filename=r"E:\exetermedia\frequency.csv"



import pandas as pd
engwords=[]
frenchwords=[]
frequency=[]
for key in d.keys():
    engwords.append(key)
    frenchwords.append(mydict[key])
    frequency.append(d[key])


    
finalDF={'English words':engwords,'French words':frenchwords,'Frequency':frequency}
df= pd.DataFrame(finalDF)

df.to_csv('frequency.csv')

print(time.time()-start_time)

