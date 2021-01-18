#1 Libraries importieren
import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams

#2 Pandas dataframe erstellen
df = pd.read_excel('downloads/export-7.xlsx')

#print(df)

#3 Quadretmeterabschnitte erstellen
df['quadratmeterRange'] = pd.cut(df.Wohnflaeche, bins = [0,20,30,40,50,60,70,80,90,100,120,140,160,180,200,220,240], 
                                 labels = ['0-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100',
                                           '100-120','120-140','140-160','160-180','180-200', '200-220', '220-240'])

#4 Neue Spalte: Preis pro Qm erstellen
df['preisProQm'] = df.Kaufpreis / df.Wohnflaeche

#5 Quadratmeterabschnitte aggregieren und durchschnitt errechnen
aggRange = df.groupby(['quadratmeterRange']).agg('mean')  #Ranges zusammenfassen und mittelwert errechnen

#print(aggRange.preisProQm)
graphData = aggRange.preisProQm

#6 Daten visualisieren
rcParams['figure.figsize'] = 15, 5
plt.plot(aggRange.preisProQm)

plt.xlabel('Quadratmeter Spanne')
plt.ylabel('Durchschnittlicher Preis pro Qm in €')
plt.title('Durchschnittlicher Quadratmeterpreis für ausgewählte Wohnungsgrößen in München')