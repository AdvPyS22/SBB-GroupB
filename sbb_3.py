"""Analysis of SBB dataset"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
data = pd.read_csv('./haltestelle-uhr.csv', sep=';')
def main():
    """call other functions in main()"""
    data = pd.read_csv('./haltestelle-uhr.csv', sep=';')
    sum(data['Line'].isnull())  # 0
    sum(data['KM'].isnull())  # 0
    sum(data['Stop name'].isnull())  # 0
    sum(data['Befestigung text'].isnull())  # 147
    sum(data['Befestigung Auswahl'].isnull())  # 23
    data['Befestigung Auswahl'] = data['Befestigung Auswahl'].fillna(data['Befestigung Auswahl'].mode()[0])
    sum(data['Type of display'].isnull())  # 101
    data['Type of display'] = data['Type of display'].fillna(data['Type of display'].mode()[0])
    sum(data['Mounted on'].isnull())  # 305
    data['Mounted on'] = data['Mounted on'].fillna(data['Mounted on'].mode()[0])
    sum(data['Lighting'].isnull())  # 47
    data['Lighting'] = data['Lighting'].fillna(data['Lighting'].mode()[0])
    sum(data['Second hand'].isnull())  # 44
    data['Second hand'] = data['Second hand'].fillna(data['Second hand'].mode()[0])
    sum(data['FID'].isnull())
    sum(data['Geopos'].isnull())
    station = input("Please input the station name: ").strip().lower().title()
    while station not in list(data['Stop name']):
        print('Please inpit right station name!')
        station = input("Please input the station name: ").strip().lower().title()
    result = data[data['Stop name'] == station]
    data_1,labels_1 = get_plot_data(result,'Line')
    data_2,labels_2 = get_plot_data(result,'Befestigung Auswahl')
    data_3,labels_3 = get_plot_data(result,'Type of display')
    data_4,labels_4 = get_plot_data(result,'Lighting')
    data_5,labels_5 = get_plot_data(result,'Second hand')
    fig1 = plt.figure(figsize=(8, 6))
    draw_fig(data_1,labels_1)
    plt.title('Line Statistics')
    fig2 = plt.figure(figsize=(8, 6))
    draw_fig(data_2,labels_2)
    plt.title('Befestigung Auswahl Statistics')
    fig3 = plt.figure(figsize=(8, 6))
    draw_fig(data_3,labels_3)
    plt.title('Type of display Statistics')
    fig4 = plt.figure(figsize=(8, 6))
    draw_fig(data_4,labels_4)
    plt.title('Lighting Statistics')
    fig5 = plt.figure(figsize=(8, 6))
    draw_fig(data_5,labels_5)
    plt.title('Second hand Statistics')
    pdf = matplotlib.backends.backend_pdf.PdfPages(f"{station}-output1.pdf")
    for fig in [fig1, fig2, fig3, fig4, fig5]:
        pdf.savefig(fig)
    pdf.close()
    #task2
    data2 = pd.read_csv('./rampe-treppe.csv',sep=';')
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
    y_data = np.array([1]*12)
    mylabels = ['Line', 'KM','Hand rail', 'Station abbreviation', 
        'Stop name',  'Type', 'Type of construction', 'Use', 'Width', 
        'Length', 'DIFF H=', 'FID']
    print(mylabels)
    plt.pie(y_data, labels = mylabels, startangle = 90)
    plt.show()  
    # plot pie chart
    var1 = input("Please input the same name mentioned in above pie chart: ")   
    # get the related data
    data_frame = list(data2[var1])
    var1_data = deal_data(data_frame)
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
def get_plot_data(result,column):
    """
    get the data from dataframe,count and drop duplicate,respectly,
    as of data and label of plot 
    """
    data = result[column].value_counts()
    labels = result[column].drop_duplicates()
    return data,labels
def draw_fig(data,labels):
    """draw bar according to task1
    """
    plt.bar(range(len(data)), data, tick_label=labels, width=0.3,
        color=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'g'])
    for a_value, b_value, label in zip(range(len(labels)), data, data):
        plt.text(a_value,
                 b_value,
                 label,
                 ha='center',
                 va='bottom')    
def deal_data(dataframe):
    """"count the value repeat time. If the value's number is 
    greater than 10,then we return top 10 result"""
    dict_of_counts = {item:dataframe.count(item) for item in dataframe}
    result = sorted(dict_of_counts.items(), key = lambda  item:item[1], reverse=True)
    if len(result) > 10:
        result = dict(result[0:10])
        return result
    return dict(result)
def draw_bar(dic, var1):
    """draw bar according to task2
    """
    y_value = dic.values()
    height = dic.keys()
    plt.bar(height, y_value,width = 0.3,
    color = ['b','r','g','y','c','m','y','k','c','g','g'])
    for a_value, b_value, label in zip(range(len(height)), y_value,y_value):
        plt.text(a_value,
             b_value,
             label,
             ha='center', 
             va='bottom')
    plt.title(var1)
    plt.show()
def draw_pie(dic, var1):
    """draw bar according to task2
    """
    y_value = dic.values()
    mylabels = dic.keys()
    plt.pie(y_value, labels = mylabels, startangle = 90)
    plt.title(var1)
    plt.show()
# call main
main()