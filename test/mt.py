import math

a = [0.25, 2.0215781529744468, 1.652654806772868, 5.0121668179829917, 1.6337366898854575]


possiblevalues = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25,
                  4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75,
                  9.0, 9.25, 9.5, 9.75, 10.0, 10.25, 10.5, 10.75, 11.0, 11.25, 11.5, 11.75, 12.0, 12.25, 12.5, 12.75,
                  13.0, 13.25, 13.5, 13.75, 14.0, 14.25, 14.5, 14.75, 15.0, 15.25, 15.5, 15.75, 16.0, 16.25, 16.5,
                  16.75, 17.0, 17.25, 17.5, 17.75, 18.0, 18.25, 18.5, 18.75, 19.0, 19.25, 19.5, 19.75, 20.0, 20.25,
                  20.5, 20.75, 21.0, 21.25, 21.5, 21.75, 22.0, 22.25, 22.5, 22.75, 23.0, 23.25, 23.5, 23.75, 24.0,
                  24.25, 24.5, 24.75, 25.0, 25.25, 25.5, 25.75, 26.0, 26.25, 26.5, 26.75, 27.0, 27.25, 27.5, 27.75,
                  28.0, 28.25, 28.5, 28.75, 29.0, 29.25, 29.5, 29.75, 30.0, 30.25, 30.5, 30.75, 31.0, 31.25, 31.5,
                  31.75]
control = 0
l1 = []
for durations in a:
    control += float(durations)
    l1.append(control)

l2 = []
for duration in l1:
    l2.append(float(min(possiblevalues, key=lambda x: abs(x - duration * (100 / 60.0)))))
l3 = []
turn = 0
keep = 0.0

print l2
for number in l2:
    if math.floor(float(number) / 4) > math.floor(keep / 4):
        if math.floor(float(number) / 4) == float(number) / 4:
            if math.floor(float(number) / 4) - math.floor(keep / 4) <= 1:
                l3.append(number)
            else:
                for i in range(0, int(math.floor(float(number) / 4 - math.floor(keep / 4)))):
                    l3.insert(turn, [math.floor(float(number) / 4) * 4 - (
                            (int(math.floor(float(number) / 4 - math.floor(keep / 4))) - 1 - i) * 4), "None"])
                    turn += 1
                l3.append(number)

        else:
            for i in range(0, int(math.floor(float(number) / 4 - math.floor(keep / 4)))):
                l3.insert(turn, [math.floor(float(number) / 4) * 4 - (
                        (int(math.floor(float(number) / 4 - math.floor(keep / 4))) - 1 - i) * 4), "None"])
                turn += 1
            l3.append(number)
    else:
        l3.append(number)
    keep = number
    turn += 1

print l3
