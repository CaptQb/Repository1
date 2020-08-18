# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 10:24:18 2020

@author: rm23m
"""
str="Global warming is the steady and continuous rise in the level of earth temperature. Out earth surface is becoming hotter day by day just because of some unnoticeable habits of human beings all across the world. Global warming has become the most worrying threat for the earth’s atmosphere as it is reducing the life possibilities on the earth day by day through a continuous and steady declining process. Before planning the solutions of the global warming, we must think about the causes and effects of it on the atmosphere in order to get sure that we are in right direction of getting full relief from this issue. The continuous warming of the earth surface is the increasing emission of CO2 in the environment. However, the increasing level of CO2 is caused due to many reasons like deforestation, use of coal, oil, gas, burning of fossil fuels, burning of gasoline for transportation, unnecessary use of electricity, etc which in turn causes rise in earth temperature. Again it becomes the reason of rising sea level, occurrence of flooding, storms, cyclone, ozone layer damage, changing weather patterns, fear of epidemic diseases, lack of food, death, etc. We cannot blame any single entity for this as each and every human being is responsible for the increasing threat of global warming which can be solved only by the global awareness and kind efforts of everyone."
print(str.lower())
count=len(str.split())
print("the number of words are :",count)
count1=0
for i in range(len(str)):
    count1=count1+1
print("the number of characters are :",count1)
str2=str.lower()
words=str2.split()
print("Duplicate words in the given string :")
for i in range(0,len(str2)):
    count2=1
    for j in range(i+1,len(words)):
        if(words[i]==words[j]):
            count2=count2+1
            words[j]="0"
    if(count2>1 and words[i]!="0"):
        print(words[i],count2)
    
#%%
list=['the','in','on','are','a','with','from']
words=str.split()
resultwords=[word for word in words not in list]
newstr=' '.join(resultwords)