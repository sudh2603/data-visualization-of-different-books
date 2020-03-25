# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 14:59:34 2018

@author: sudhanshu kumar sinh
"""

from collections import Counter
import os
import pandas as pd
import matplotlib.pyplot as plt

def read_book(book):
    with open(book,"r",encoding="utf8") as f:
        text=f.read()
    for i in [",",".",'"',":",";","#","'","?","/","!","@","$","%","(",")","*","_","^",">","<","[","]"]:
        text=text.replace(i,"")
    text=text.replace("\n","").replace("\r","")
    return text
    
def word_stats(word_count):
    unique_word=len(word_count)
    count=word_count.values()
    return (unique_word,count)

book_dir="./books"
stats=pd.DataFrame(columns=("LANGUAGE","AUTHOR","TITLE","LENGTH","UNIQUE"))
title_num=1
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir+"/"+language):
        for title in os.listdir(book_dir+"/"+language+"/"+author):
            input_file=book_dir+"/"+language+"/"+author+"/"+title
            print(input_file)
            text=read_book(input_file)
            word_count=Counter(text.split(" "))
            (num_unique,count)=word_stats(word_count)
            stats.loc[title_num]=language, author.capitalize(), title.replace(".txt",""), sum(count), num_unique
            title_num+=1
plt.figure(figsize=(10,10))
subset=stats[stats.LANGUAGE=="English"]
plt.loglog(subset.LENGTH,subset.UNIQUE,"o",label="English",color="crimson")

subset=stats[stats.LANGUAGE=="German"]
plt.loglog(subset.LENGTH,subset.UNIQUE,"o",label="German",color="forestgreen")

subset=stats[stats.LANGUAGE=="French"]
plt.loglog(subset.LENGTH,subset.UNIQUE,"o",label="French",color="orange")

subset=stats[stats.LANGUAGE=="Portuguese"]
plt.loglog(subset.LENGTH,subset.UNIQUE,"o",label="Portuguese",color="blue")
plt.legend()
plt.xlabel("Book Length")
plt.ylabel("No of Unique Word")


#book_text=read_book("./Books_EngFr/Books_EngFr/English/shakespeare/Romeo and Juliet.txt")
#word_count=Counter(book_text.split(" "))
#(num_unique,counts)=word_stats(word_count)
#print((num_unique,counts))
    


#book_text_german=read_book("./Books_GerPort/Books_GerPort/German/shakespeare/Romeo und Julia.txt")
#word_count=Counter(book_text_german.split(" "))
#(num_unique,counts)=word_stats(word_count)
#print((num_unique,counts))




#from collections import Counter
#string="This comprehension check is to check for comprehension"
#string=string.lower()
#count=Counter(string.split(" "))

#import string
#a=string.ascii_letters


#import numpy as np
#import matplotlib.pyplot as plt
#delta_x=np.random.normal(0,1,(2,5))
#x=np.cumsum(delta_x,axis=1)
#y=np.sum(delta_x,axis=1)
#plt.plot(x[0],x[1],"rs--");

#plt.subplot(331)
#plt.subplot(332)
#plt.subplot(333)

#plt.subplot(3,3,1)
#plt.subplot(3,3,2)
#plt.subplot(3,3,3)