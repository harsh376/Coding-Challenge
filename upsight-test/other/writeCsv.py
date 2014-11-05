import csv
with open('test.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')

    d1 = {"a":[1,2,3,5,7,8,9], "b":[2,3,6]}

    data = [['Me', 'You'],
            ['293', '219'],
            ['54', '13']]
    a.writerows(d1)