
from random import randint
import math

import csv

startyear = -10000
present = 2018
singularity = 2056

events = {}
with open('timelineoftech.csv','r',newline='') as f:
    lines = csv.reader(f,delimiter=',')
    for i in lines:
        try:
            year = int(i[1])
            randrange = int((present-year)/20)
            year = year + randint(-randrange,randrange)
            year = min(year,present-1)
            #year = max(year,startyear)
            try:
                events[year] = events[year] + ', ' + i[0]
            except:
                events[year] = i[0]
        except:
            pass
    events[present] = 'THE PRESENT ({})'.format(present)


def linear(events):
    for i in range(startyear,present):
        try:
            print(events[i])
        except:
            print('')

    print('THE PRESENT ({})'.format(present))

def logarithmic(events):
    steps = range(0,1000)
    steps = [1.01**i for i in steps]
    steps = steps[::-1]
    print(steps)
    for i in range(len(steps)-1):
        invs = ''
        for n in range(int(steps[i+1]),int(steps[i]))[::-1]:
            n = singularity - n
            #print(n)
            try:
                #print(events[n])
                invs = invs + events[n] + ', '
            except:
                pass
        print(invs[:-2])

linear(events)

print('---------')

logarithmic(events)

#print(events)

#inventions = {}

#for i in lines:
    #try:
        #print(int(i[48:56]))
    #except:
        #pass
