import csv

# Define the header
header = [['First Name','Last Name','Email','ID','HW Total % (Max: 20%)','Quiz Total % (Max: 80%)','Overall Grade']]
hw_t = 9 # Change 8 to 9 after last HW.
quiz_t = 4*10 # Change 8 to 10 after last quiz
quiz_perc = 0.8
hw_perc = 0.2
del_num = 5 # change to 5 toward the end (5 quizzes get dropped)

hw_rows = []
with open('./kudu-grades/Physics1B-HW-3-12-21.csv', 'r') as hw:
    reader = csv.reader(hw)
    for line in reader:
        if line[3] == 'ID':
            pass
        else:
            hw1 = int(line[4])/22
            hw2 = int(line[5])/19
            hw3 = int(line[6])/16
            hw4 = int(line[7])/22
            hw5 = int(line[8])/17
            hw6 = int(line[9])/15
            hw7 = int(line[10])/22
            hw8 = 0.5*((5/8)*(int(line[11])/8) + (11/8)*(int(line[12])/12))
            hw9 = int(line[13])/17
            hw10 = int(line[14])/15
            hw_score_list = [hw1,hw2,hw3,hw4,hw5,hw6,hw7,hw8,hw9,hw10]
            # add only required HW
            lowest_hw_val = min(hw_score_list)
            hw_score_list.remove(lowest_hw_val)
            # print(len(hw_score_list))
            h_r = sum(hw_score_list)
            hw_rows.append([line[0],line[1],line[2],line[3],h_r])

quiz_us_rows = []
scores_us = []
with open('./kudu-grades/Physics1B-USquiz-3-12-21.csv', 'r') as quiz:
    reader = csv.reader(quiz)
    for line in reader:
        if line[3] == 'ID':
            pass
        else:
            quiz1a = int(float(line[4]))
            quiz1b = int(float(line[5]))
            quiz2a = int(float(line[6]))
            quiz2b = int(float(line[7]))
            quiz3a = int(float(line[8]))
            quiz3b = int(float(line[9]))
            quiz4a = int(float(line[10]))
            quiz4b = int(float(line[11]))
            quiz5a = int(float(line[12]))
            quiz5b = int(float(line[13]))
            # dummy quizzes
            finala = 0
            finalb = 0
            finalc = 0
            finald = 0
            finale = 0
            scores_us = [quiz1a,quiz1b,quiz2a,quiz2b,quiz3a,quiz3b,quiz4a,quiz4b,quiz5a,
                        quiz5b,finala,finalb,finalc,finald,finale]
            # Add routine here to remove lowest 5 blocks.
            deletions = 0
            while deletions < del_num:
                deletions += 1
                lowest_val = min(scores_us)
                scores_us.remove(lowest_val)
            # print(len(scores_us))
            quiz_us_rows.append([line[0],line[1],line[2],line[3],scores_us])

# Combine both the hw and quiz list.
overall_score = []
for i in hw_rows:
    for k in quiz_us_rows:
        if i[2] == k[2] and i[3] == k[3]:
            hw_total_perc = (i[4]/hw_t)*hw_perc
            quiz_total_perc = (sum(k[4])/quiz_t)*quiz_perc
            person_score = (hw_total_perc + quiz_total_perc) * 100
            overall_score.append([i[0],i[1],i[2],k[3],str(hw_total_perc*100) +'%',str(quiz_total_perc*100)+'%'
                                  ,str(person_score)+'%'])
        else:
            pass

file = open('Phys1B-all-Grades_test.csv', 'w+', newline='')
with file:
    write = csv.writer(file)
    write.writerows(header)
    write.writerows(overall_score)

# Test
# a = [22/22,17/19,12/16,20/22,17/17,15/15,0/22,0.5*((5/8)*(8/8)+(11/8)*(7/12)),14/17,15/15]
# lowest_num = min(a)
# print(lowest_num)
# a.remove(lowest_num)
# print(a)
# print((sum(a)/9)*20)
