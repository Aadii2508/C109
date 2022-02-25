import statistics as stats
import pandas as pd
import csv

file= pd.read_csv("height-weight.csv")
weightlist=file["Weight(Pounds)"].tolist()

mean= stats.mean(weightlist)
print("Mean is {}".format(mean))

median= stats.median(weightlist)
print("Median is {}".format(median))

mode= stats.mode(weightlist)
print("Mode is {}".format(mode))

stdev= stats.stdev(weightlist)
print("Standard deviation is {}".format(stdev))

minimum= mean- 3*stdev
maximum= mean+ 3*stdev

list=[]

for i in weightlist:
    if i>minimum and i<maximum:
        list.append(i)

n= len(list)
total= len(weightlist)

probability= (n*100)/total

print("{} % of data lies within third standard deviation".format(probability))