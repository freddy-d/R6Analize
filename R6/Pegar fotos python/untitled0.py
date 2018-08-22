# -*- coding: utf-8 -*-
"""
Created on Sun May 20 22:56:34 2018

@author: Freddy Dratwa
"""

opATC=["lion","finka","dokkaebi","zofia","ying","jackal","hibana","capitao","blackbeard","buck","sledge","thatcher",
       "ash","thermite","montagne","twitch","blitz","iq","fuze","glaz"]

opDEF=["vigil","ela","lesion","mira","echo","caveira","valkyrie","frost","mute","smoke",
       "castle","pulse","doc","rook","jager","bandit","tachanka","kapkan"]

ops=["lion","finka","vigil","dokkaebi","zofia","ela","ying","lesion","mira","jackal","hibana","echo","caveira"
     ,"capitao","blackbeard","valkyrie","buck","frost","mute","sledge","smoke","thatcher",
     "ash","castle","pulse","thermite",
     "montagne","twitch","doc","rook","jager","bandit","blitz","iq","fuze","glaz","tachanka","kapkan"]

#import re
#lista=[]
#with open("fotos.txt") as f:
#    linhas=f.readlines()
#    for i in linhas:
#        lista.append(re.findall(r'(https?://[^\s]+)', i))
#    lista2 = [x for x in lista if x != []]
#with open("links.txt", "w") as t:
#    for i in lista2:
#        for q in i:
#            t.write(q)
#            t.write("\n")
#lista3=[]
#with open("links4.txt", "r") as st:
#        for line in st:
#           lista3.append(line)
#            
#           
#           
#           
#import urllib.request
#
#
#i=0
#while i < len(lista3):
#    resource = urllib.request.urlopen("{}".format(lista3[i]))
#    output = open("{}.png".format(ops[i]),"wb")
#    output.write(resource.read())
#    output.close()
#    i+=1
           
           
#           
#with open("links4.txt","w") as j:
#    i=0
#    while i <len(lista3):
#        if i%2 == 0:
#            j.write(lista3[i])
#        i+=1            


#print(len(opATC))
print(len(ops))