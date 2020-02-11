import random
correct = False
numcorrect = False
a = 0.0
recordnum = 0.0
controlnum = 0.0
current = 0.0
noteamount = random.randint(2,8)
valuenum = random.randint(0,22)
notenum = random.randint(0,21)
musicpiece = input("enter the music with number")
piecenoteamount = []
finalnoteamount = 128
numlist = []
recordnumlist = []
recordnoteamount = 0
notelist = []
recordnotelist = []
recordvaluelist = []
possiblevalue = [0.25,0.25,0.5,0.5,0.5,1.0,1.0,1.0,1.0,2.0,2.0,2.0,2.0,3.0,3.0,4.0,4.0]
possiblenotes = ["C-3","D-3","E-3","F-3","G-3","A-3","B-3","C-4","D-4","E-4","F-4","G-4","A-4","B-4","C-5","D-5","E-5","F-5","G-5","A-5","B-5","C-6"]
listneeded = []
for i in range(0,8):
    correct = False
    while not correct:
        noteamount = random.randint(4,16)
        for i in range (0,noteamount):
            valuenum = random.randint(0,16)
            notenum = random.randint(0, 21)
            numlist.append(possiblevalue[valuenum])
            notelist.append(possiblenotes[notenum])
            controlnum += possiblevalue[valuenum]
        if controlnum != 4.0:
            numlist = []
            notelist = []
            print controlnum
            controlnum = 0.0
        else:
            for i in range(0,noteamount):
                recordnotelist.append(notelist[i])
                recordnumlist.append(numlist[i])
                recordvaluelist.append(recordnum)
                recordnum += numlist[i]
            recordnoteamount += noteamount
            print controlnum
            controlnum = 0.0
            numlist = []
            notelist = []
            correct = True
for i in range(0,recordnoteamount):
    listneeded.append([current,recordnumlist[i],recordnotelist[i]])
    current += recordnumlist[i]
print listneeded