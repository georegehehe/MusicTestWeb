import random
import math
def determination(music):
    maximum = len(str(music)) - 1
    print "ye"
    number1 = 0
    number2 = 0
    number3 = 0
    randomnum3 = 0
    randomnum4 = 0
    allmajor = False
    activated1 = False
    activated2 = False
    format = random.randint(1, 10)
    if format <= 1:
        allmajor = True
    else:
        allmajor = False
    minorselect = random.randint(1, maximum - 1)
    selection = random.randint(1, 2)
    preresult = []
    unablepreferred = [2, 4]
    preferred = [3, 6]
    major = [1, 4, 5]
    minor = [2, 3, 6, 7]
    firstmajor = [0, maximum]
    n = 0
    result = []
    while n <= maximum:
        if int(music[n]) <= 0:
            number1 = int(music[n]) + 7
        else:
            number1 = int(music[n])
        if int(music[n]) - 2 <= 0:
            number2 = int(music[n]) + 5
        else:
            number2 = int(music[n]) - 2
        if int(music[n]) - 4 <= 0:
            number3 = int(music[n]) + 3
        else:
            number3 = int(music[n]) - 4
        if n in firstmajor:
            if number1 == 1:
                result.append(1)
                n += 1

            elif number2 == 1:
                result.append(1)
                n += 1

            elif number3 == 1:
                result.append(1)
                n += 1

            else:
                for i in major:
                    if i == number1:
                        preresult.append(number1)
                    if i == number2:
                        preresult.append(number2)
                    if i == number3:
                        preresult.append(number3)
                randomnum = random.randint(0, len(preresult) - 1)
                result.append(preresult[randomnum])
                n += 1
                preresult = []
        else:
            if allmajor:
                for i in major:
                    if i == number1:
                        preresult.append(number1)
                    if i == number2:
                        preresult.append(number2)
                    if i == number3:
                        preresult.append(number3)
                randomnum = random.randint(0, len(preresult) - 1)
                result.append(preresult[randomnum])
                n += 1
                preresult = []
            else:
                if activated1:
                    # need something here
                    if preferred[randomnum4] == number1:
                        result.append(preferred[randomnum4])
                        n += 1
                        activated1 = False
                        continue
                    elif preferred[randomnum4] == number2:
                        result.append(preferred[randomnum4])
                        n += 1
                        activated1 = False
                        continue
                    elif preferred[randomnum4] == number3:
                        result.append(preferred[randomnum4])
                        n += 1
                        activated1 == False
                        continue
                    else:
                        for i in major:
                            if i == number1:
                                preresult.append(number1)
                            if i == number2:
                                preresult.append(number2)
                            if i == number3:
                                preresult.append(number3)
                        randomnum = random.randint(0, len(preresult) - 1)
                        result.append(preresult[randomnum])
                        n += 1
                        preresult = []
                        activated1 = False
                        continue

                if activated2:
                    if preferred[randomnum3] == number1:
                        result.append(preferred[randomnum3])
                        n += 1
                        activated2 = False
                        continue
                    elif preferred[randomnum3] == number2:
                        result.append(preferred[randomnum3])
                        n += 1
                        activated2 = False
                        continue
                    elif preferred[randomnum3] == number3:
                        result.append(preferred[randomnum3])
                        n += 1
                        activated2 == False
                        continue
                    else:
                        for i in major:
                            if i == number1:
                                preresult.append(number1)
                            if i == number2:
                                preresult.append(number2)
                            if i == number3:
                                preresult.append(number3)
                        randomnum = random.randint(0, len(preresult) - 1)
                        result.append(preresult[randomnum])
                        n += 1
                        preresult = []
                        activated2 = False
                        continue

                if selection == 1:
                    if n == 2:
                        if music[n] not in unablepreferred:
                            while randomnum3 == randomnum4:
                                randomnum3 = random.randint(0, 1)
                                randomnum4 = random.randint(0, 1)
                            if number1 == preferred[randomnum3]:
                                result.append(preferred[randomnum3])
                                activated1 = True
                                n += 1
                            elif number2 == preferred[randomnum3]:
                                result.append(preferred[randomnum3])
                                activated1 = True
                                n += 1

                            elif number3 == preferred[randomnum3]:
                                result.append(preferred[randomnum3])
                                activated1 = True
                                n += 1
                            else:
                                result.append(preferred[randomnum4])
                                activated2 = True
                                n += 1
                        else:
                            minorselect = random.randint(3, max - 1)
                            selection = 2
                            for i in major:
                                if i == number1:
                                    preresult.append(number1)
                                if i == number2:
                                    preresult.append(number2)
                                if i == number3:
                                    preresult.append(number3)
                            randomnum = random.randint(0, len(preresult) - 1)
                            result.append(preresult[randomnum])
                            n += 1
                            preresult = []

                    else:
                        for i in major:
                            if i == number1:
                                preresult.append(number1)
                            if i == number2:
                                preresult.append(number2)
                            if i == number3:
                                preresult.append(number3)
                        randomnum = random.randint(0, len(preresult) - 1)
                        result.append(preresult[randomnum])
                        n += 1
                        preresult = []
                else:
                    if n == minorselect:
                        for i in minor:
                            if i == number1:
                                preresult.append(number1)
                            if i == number2:
                                preresult.append(number2)
                            if i == number3:
                                preresult.append(number3)
                        randomnum = random.randint(0, len(preresult) - 1)
                        result.append(preresult[randomnum])
                        n += 1
                        preresult = []
                    else:
                        for i in major:
                            if i == number1:
                                preresult.append(number1)
                            if i == number2:
                                preresult.append(number2)
                            if i == number3:
                                preresult.append(number3)
                        randomnum = random.randint(0, len(preresult) - 1)
                        result.append(preresult[randomnum])
                        n += 1
                        preresult = []
    return result