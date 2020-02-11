import math
import random
import itertools
def determination(musicpiece,mode):
    major = [1,4,5,7]
    possiblechords = []
    allcombos = []
    scorelist = []
    positionlist = []
    positionpositionlist = []
    song = musicpiece
    numiteration = 0
    num1 = 0
    num2 = 0
    num3 = 0
    for num in song:
        num1 = int(num)
        if int(num) - 2 > 0:
            num2 = int(num) - 2

        else:
            num2 = int(num) + 5
        if int(num) - 4 > 0:
            num3 = int(num) - 4
        else:
            num3 = int(num) + 3
        if numiteration == 0:
            if mode == 2:
                possiblechords.append(num)
            else:
                if num1 == 1:
                    possiblechords.append([1])
                elif num2 == 1:
                    possiblechords.append([1])
                elif num3 == 1:
                    possiblechords.append([1])
                else:
                    possiblechords.append([num1, num2, num3])
        elif numiteration == 7 + mode:
            if num1 == 1:
                possiblechords.append([1])
            elif num2 == 1:
                possiblechords.append([1])
            elif num3 == 1:
                possiblechords.append([1])
            else:
                possiblechords.append([num1, num2, num3])
        else:
            if mode == 2:
                if numiteration == 1:
                    if num1 == 1:
                        possiblechords.append([1])
                    elif num2 == 1:
                        possiblechords.append([1])
                    elif num3 == 1:
                        possiblechords.append([1])
                    else:
                        possiblechords.append([num1, num2, num3])
                else:
                    possiblechords.append([num1, num2, num3])
            else:
                print num2
                possiblechords.append([num1, num2, num3])
        numiteration += 1
    print possiblechords
    numiteration = 0

    allcombos = list(itertools.product(*possiblechords))
    score = 0
    for listneeded in allcombos:
        for note in listneeded:
            try:
                if note == 2 and listneeded[numiteration + 1] == 5:
                    score += 1
                elif note == 4 and listneeded[numiteration + 1] == 1:
                    if mode == 2:
                        if numiteration == 6:
                            if listneeded[8] == 1:
                                score += 1
                        if numiteration >= 7:
                            score += 1

                    else:
                        if numiteration == 5:
                            if listneeded[7] == 1:
                                score += 1
                        if numiteration >= 6:
                            score += 1
                elif note == 2 and listneeded[numiteration + 1] == 7:
                    score += 1
                elif note == 4 and listneeded[numiteration + 1] == 5:
                    score += 1
                elif note == 4 and listneeded[numiteration + 1] == 7:
                    score += 1
                elif note == 5 and listneeded[numiteration + 1] == 1:
                    if mode == 2:
                        if numiteration == 6:
                            if listneeded[8] == 1:
                                score += 2
                        if numiteration >= 7:
                            score += 2
                    else:
                        if numiteration == 5:
                            if listneeded[7] == 1:
                                score += 2
                        if numiteration >= 6:
                            score += 2
                elif note == 7 and listneeded[numiteration + 1] == 1:
                    if mode == 2:
                        if numiteration == 6:
                            if listneeded[8] == 1:
                                score += 2
                        if numiteration >= 7:
                            score += 2
                    else:
                        if numiteration == 5:
                            if listneeded[7] == 1:
                                score += 2
                        if numiteration >= 6:
                            score += 2
                elif note == 7 and listneeded[numiteration + 1] != 1:
                    if listneeded[numiteration + 1] != 7 and listneeded[numiteration + 1] != 5:
                        score -= 1
                elif note == 3 and listneeded[numiteration + 1] == 6:
                    score += 1
                elif note == 6 and listneeded[numiteration + 1] == 2:
                    score += 1
                elif note == 6 and listneeded[numiteration + 1] == 4:
                    score += 1
                elif note == 6 and listneeded[numiteration + 1] == 3:
                    score += 1
                elif note == 4 and listneeded[numiteration + 1] == 2:
                    score += 0.5
                elif note == 2 and listneeded[numiteration + 1] == 4:
                    score += 0.5
                elif note == 6 and listneeded[numiteration + 1] == 5:
                    score += 0.5
                elif note == 5 and listneeded[numiteration + 1] == 6:
                    score += 0.5
                elif note == 5 and listneeded[numiteration + 1] == 4:
                    score += 0.5
                elif note == 3 and listneeded[numiteration + 1] == 4:
                    score += 0.5
                elif note == 3 and listneeded[numiteration + 1] == 5:
                    score += 0.5
                else:
                    if note != 1 and listneeded[numiteration + 1] != 5 and note != listneeded[numiteration + 1] and \
                            listneeded[numiteration + 1] != 1 and (note != 5 and listneeded[numiteration + 1] != 7):
                        score -= 1
                if mode == 2:
                    if numiteration <= 8:
                        if note == listneeded[numiteration + 1] and note == listneeded[numiteration + 2]:
                            score -= 1
                    numiteration += 1
                else:
                    if numiteration <= 7:
                        if note == listneeded[numiteration + 1] and note == listneeded[numiteration + 2]:
                            score -= 1
                    numiteration += 1
            except IndexError:
                numiteration += 1
        scorelist.append(score)
        score = 0.0
        numiteration = 0
    print max(scorelist)
    for eachscore in scorelist:
        if eachscore == max(scorelist):
            positionlist.append(numiteration)
        numiteration += 1
    scorelist = []
    numiteration = 0
    for position in positionlist:
        print allcombos[position]
        for items in allcombos[position]:
            if items in major:
                score += 1
        scorelist.append(score)
        score = 0.0
    for eachscore in scorelist:
        if eachscore == max(scorelist):
            positionpositionlist.append(numiteration)
        numiteration += 1
    for positionlisted in positionpositionlist:
        print str(allcombos[positionlist[positionlisted]]) + "/"
    return list(allcombos[positionlist[random.choice(positionpositionlist)]])
