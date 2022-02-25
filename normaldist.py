import statistics as stats
import pandas as pd
import csv

file= pd.read_csv("height-weight.csv")
heightlist=file["Height(Inches)"].tolist()

mean= stats.mean(heightlist)
print("Mean is {}".format(mean))

median= stats.median(heightlist)
print("Median is {}".format(median))

mode= stats.mode(heightlist)
print("Mode is {}".format(mode))

stdev= stats.stdev(heightlist)
print("Standard deviation is {}".format(stdev))

minimum= mean- 3*stdev
maximum= mean+ 3*stdev

list=[]

for i in heightlist:
    if i>minimum and i<maximum:
        list.append(i)

n= len(list)
total= len(heightlist)

probability= (n*100)/total

print("{} % of data lies within third standard deviation".format(probability))