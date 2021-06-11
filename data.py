import os
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import sys

fileOrig = open(os.path.join(os.path.join(os.environ['USERPROFILE']), "Downloads\\Portugal.txt"), 'r', encoding="utf-8")

def sex():

    print("Calculating...")

    lines = fileOrig.readlines()

    arr = []

    for line in lines:
        if(line.split(":")[4]!=''):
            arr.append(line.split(":")[4])

    labels, values = zip(*Counter(arr).most_common(2))

    indexes = np.arange(len(labels))

    plt.barh(indexes, values)
    plt.yticks(indexes, labels)
    plt.xlim([0, 1300000])
    plt.title('Sex Distribution')
    for index, value in enumerate(values):
        plt.text(value, index, f'{value:,}')
    ax = plt.gca()
    ax.invert_yaxis()
    plt.show()

    print('Done.')
    sys.exit()

def name():

    print("Calculating...")

    lines = fileOrig.readlines()

    arr = []

    for line in lines:
        if(line.split(":")[2]!=''):
            arr.append(line.split(":")[2])

    labels, values = zip(*Counter(arr).most_common(20))

    indexes = np.arange(len(labels))

    plt.barh(indexes, values)
    plt.yticks(indexes, labels)
    plt.xlim([0, 60000])
    plt.title('20 Most Common Names')
    for index, value in enumerate(values):
        plt.text(value, index+0.25, f'{value:,}')
    ax = plt.gca()
    ax.invert_yaxis()
    plt.show()

    print('Done.')
    sys.exit()

def surname():

    print("Calculating...")

    lines = fileOrig.readlines()

    arr = []

    for line in lines:
        if(line.split(":")[3]!=''):
            arr.append(line.split(":")[3])

    labels, values = zip(*Counter(arr).most_common(20))

    indexes = np.arange(len(labels))

    plt.barh(indexes, values)
    plt.yticks(indexes, labels)
    plt.xlim([0, 100000])
    plt.title('20 Most Common Surnames')
    for index, value in enumerate(values):
        plt.text(value, index+0.25, f'{value:,}')
    ax = plt.gca()
    ax.invert_yaxis()
    plt.show()

    print('Done.')
    sys.exit()

def location():

    print("Calculating...")

    lines = fileOrig.readlines()

    arr = []

    for line in lines:
        if(line.split(":")[5]!=''):
            arr.append(line.split(":")[5])

    labels, values = zip(*Counter(arr).most_common(20))

    indexes = np.arange(len(labels))

    plt.barh(indexes, values)
    plt.yticks(indexes, labels)
    plt.xlim([0, 200000])
    plt.title('20 Most Common Locations')
    for index, value in enumerate(values):
        plt.text(value, index+0.25, f'{value:,}')
    ax = plt.gca()
    ax.invert_yaxis()
    plt.show()

    print('Done.')
    sys.exit()

def job():

    print("Calculating...")

    lines = fileOrig.readlines()

    arr = []

    for line in lines:
        if(line.split(":")[8]!=''):
            arr.append(line.split(":")[8])

    labels, values = zip(*Counter(arr).most_common(20))

    indexes = np.arange(len(labels))

    plt.barh(indexes, values)
    plt.yticks(indexes, labels)
    plt.xlim([0, 17000])
    plt.title('20 Most Common Jobs')
    for index, value in enumerate(values):
        plt.text(value, index+0.25, f'{value:,}')
    ax = plt.gca()
    ax.invert_yaxis()
    plt.show()

    print('Done.')
    sys.exit()

def phone():

    print("Calculating...")

    lines = fileOrig.readlines()

    arr = []

    for line in lines:
        if(line.split(":")[0]!=''):
            if(line.split(":")[0][3:5]=='91' or line.split(":")[0][3:6]=='921'):
                arr.append('Vodafone')
            elif(line.split(":")[0][3:5]=='96' or line.split(":")[0][3:6]=='924' or line.split(":")[0][3:6]=='925' or line.split(":")[0][3:6]=='926' or line.split(":")[0][3:6]=='927'):
                arr.append('MEO')
            elif(line.split(":")[0][3:5]=='93' or line.split(":")[0][3:6]=='929'):
                arr.append('NOS')
            else:
                arr.append('Others')

    labels, values = zip(*Counter(arr).most_common(4))

    indexes = np.arange(len(labels))

    plt.barh(indexes, values)
    plt.yticks(indexes, labels)
    plt.xlim([0, 1100000])
    plt.title('Provider (Not Counting For Number Portability)')
    for index, value in enumerate(values):
        plt.text(value, index, f'{value:,}')
    ax = plt.gca()
    ax.invert_yaxis()
    plt.show()

    print('Done.')
    sys.exit()

print("Type what you'd like to evaluate ('sex', 'name', 'surname', 'location', 'job', 'phone'). 'exit' to leave:")

while(True):
    userInput = input()

    if(userInput=='sex'):
        sex()
    elif(userInput=='name'):
        name()
    elif(userInput=='surname'):
        surname()
    elif(userInput=='location'):
        location()
    elif(userInput=='job'):
        job()
    elif(userInput=='phone'):
        phone()
    elif(userInput=='exit'):
        sys.exit()
    else:
        print("Type something valid.")
