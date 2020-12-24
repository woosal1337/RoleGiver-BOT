import math


def sort(fileName):
    finalNames = []

    with open(fileName, "r") as teamNames:
        currentNames = teamNames.readlines()
        sortedNames = currentNames[0].split(",")

    for i in range(0, math.ceil(len(sortedNames) % 10) - 1):
        finalNames.append(sortedNames[i * 10:i * 10 + 10])

    return (finalNames)
