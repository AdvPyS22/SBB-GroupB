#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def main():
    data2 = pd.read_csv('./rampe-treppe.csv',sep=';')
    data2.shape
    data2=data2.dropna(subset=['Use'])
    sum(data2['Station abbreviation'].isnull())#0
    sum(data2['Stop name'].isnull())#0
    sum(data2['Type'].isnull())#0
    sum(data2['Use'].isnull())#302 Null rate is 8%, so delete null value
    data2=data2.dropna(subset=['Use'])
    sum(data2['Type of construction'].isnull())#179
    data2['Type of construction'] = data2['Type of construction'].fillna(data2['Type of construction'].mode()[0])
    sum(data2['Hand rail'].isnull())#1
    data2['Hand rail'] = data2['Hand rail'].fillna(data2['Hand rail'].mode()[0])
    sum(data2['Line'].isnull())#0
    sum(data2['KM'].isnull())#0
    sum(data2['Width'].isnull())#44
    data2['Width'] = data2['Width'].fillna(data2['Width'].mean())
    sum(data2['Length'].isnull())#47
    data2['Length'] = data2['Length'].fillna(data2['Length'].mean())
    sum(data2['DIFF H='].isnull())#202
    data2['DIFF H='] = data2['DIFF H='].fillna(data2['DIFF H='].mean())
    sum(data2['FID'].isnull())#0
    
    
    # plot the information about ramps/stairs
    y = np.array([1]*12)
    mylabels = ['Line', 'KM','Hand rail', 'Station abbreviation', 'Stop name',  'Type', 'Type of construction', 'Use', 'Width', 'Length', 'DIFF H=', 'FID']
    print(mylabels)
    plt.pie(y, labels = mylabels, startangle = 90)
    plt.show()
    
    # plot pie chart
    var1 = input("Please input the same name mentioned in above pie chart: ")
    
    # get the related data
    df = list(data2[var1])
    var1_data = deal_data(df)
    # choose the type of result them want to get 
    print("you can input 'pie' or 'bar' or 'all' to get the result")
    var2 = input("Please input result's type: ")
    if var2 == 'pie':
        draw_pie(var1_data, var1)
    elif var2 == 'bar':
        draw_bar(var1_data, var1)
    elif var2 == 'all':
        draw_bar(var1_data, var1)
        draw_pie(var1_data, var1)

def deal_data(df):
    """"count the value repeat time. If the value's number is greater than 10,then we return top 10 result"""
    dict_of_counts = {item:df.count(item) for item in df}
    result = sorted(dict_of_counts.items(), key = lambda  item:item[1], reverse=True)
    if len(result) > 10:
        result = dict(result[0:10])
        return result
    return dict(result)


def draw_bar(dic, var1):
    y = dic.values()
    height = dic.keys()

    plt.bar(height, y,width = 0.3,color = ['b','r','g','y','c','m','y','k','c','g','g'])
    for a, b, label in zip(range(len(height)), y,y):
        plt.text(a,
             b,
             label,
             ha='center', 
             va='bottom')
    plt.title(var1)
    plt.show()
    

def draw_pie(dic, var1):
    y = dic.values()
    mylabels = dic.keys()
    plt.pie(y, labels = mylabels, startangle = 90)
    plt.title(var1)
    plt.show()
    
# call main
main()