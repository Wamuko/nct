import csv
import os

if not os.path.isdir('csv'):
    exit()

# calculateファイルを作る、既存のは消す

file = open('csv/calculate', 'w')
