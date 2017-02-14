'''
Nicholas Paz and Brandon Alcala
Period 3
Data Project
'''
import os.path
import matplotlib.pyplot as plt
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'qa05101_2014.txt')
datafile = open(filename,'r')

labels=[]
quantities=[]

for line in datafile:
    crime, amount = line.split('|')
    if crime == 'Gamers Under 18 in 2014':
        labels += [crime]
        quantities += [amount]
    if crime == 'Total Crimes':
        labels += [crime]
        quantities += [amount]

 


colors = ['#FA8416','#0E82F7']

fig, ax = plt.subplots(1, 1)
ax.pie(quantities, labels=labels, colors=colors, autopct='%.0f%%')
ax.set_aspect(1) # Square axes for round plot
ax.set_title('Gamers Under The Age 18 & Juveniles That Committed A Crime')
fig.show()
