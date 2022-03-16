import csv
import pandas as pd

student_score = []
pth_canvas = './quiz7/2022-03-15T1923_Grades-PHYS2A_WI22_B00.csv'
pth_scantron = './quiz7/Phys2A-B_quiz7.csv'

with open(pth_scantron) as quiz:
    reader = csv.reader(quiz)
    for line in reader:
        if line[3] == 'phone':
            pass
        else:
            student_score.append([line[3],line[5]])

df = pd.read_csv(pth_canvas)
for index, row in df.iterrows():
    for i, j in enumerate(student_score):
        if row[3] == j[0]:
            df.loc[index,'QUIZ 7 (463019)'] = j[1]
        else:
            pass
df.to_csv('./out-q7.csv')
