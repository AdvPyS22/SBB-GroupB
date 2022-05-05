import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf

# Data acquisition
data = pd.read_csv('./haltestelle-uhr.csv', sep=';')
# Data cleaning
# deal with missing value,replace by mode
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
# input station name
station = input("Please input the station name: ").strip().lower().title()
while station not in list(data['Stop name']):
    print('Please inpit right station name!')
    station = input("Please input the station name: ").strip().lower().title()
result = data[data['Stop name'] == station]

# plot statistics
fig1 = plt.figure(figsize=(8, 4))
data = result['Line'].value_counts()
labels = result['Line'].drop_duplicates()
plt.bar(range(len(data)), data, tick_label=labels, width=0.3,
        color=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'g'])
for a, b, label in zip(range(len(labels)), data, data):
    plt.text(a,
             b,
             label,
             ha='center',
             va='bottom')
plt.title('Line Statistics')
# plt.show()
# plt.savefig("Line Statistics")

fig2 = plt.figure(figsize=(8, 4))
data = result.groupby('Line')['KM'].mean()
labels = result['Line'].drop_duplicates()
plt.bar(range(len(data)), data, tick_label=labels, width=0.3,
        color=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'g'])
for a, b, label in zip(range(len(labels)), data, round(data, 2)):
    plt.text(a,
             b,
             label,
             ha='center',
             va='bottom')
plt.title('Mileage of the line(KM)')
# plt.show()
# plt.savefig('Mileage of the line(KM)')

fig3 = plt.figure(figsize=(8, 4))
data = result['Befestigung Auswahl'].value_counts()
labels = result['Befestigung Auswahl'].drop_duplicates()
plt.bar(range(len(data)), data, tick_label=labels, width=0.3,
        color=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'g'])
plt.title('Befestigung Auswahl Statistics')
for a, b, label in zip(range(len(labels)), data, data):
    plt.text(a,
             b,
             label,
             ha='center',
             va='bottom')
# plt.show()
# plt.savefig('Befestigung Auswahl Statistics')

fig4 = plt.figure(figsize=(8, 4))
data = result['Type of display'].value_counts()
labels = result['Type of display'].drop_duplicates()
plt.bar(range(len(data)), data, tick_label=labels, width=0.3,
        color=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'g'])
for a, b, label in zip(range(len(labels)), data, data):
    plt.text(a,
             b,
             label,
             ha='center',
             va='bottom')
plt.title('Type of display Statistics')
# plt.show()
# plt.savefig('Type of display Statistics')
pdf = matplotlib.backends.backend_pdf.PdfPages(f"{station}-output1.pdf")
for fig in [fig1, fig2, fig3, fig4]:
    pdf.savefig(fig)
pdf.close()
