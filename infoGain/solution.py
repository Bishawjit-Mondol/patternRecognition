import pandas
import math

# GETTING THE DATA
data = pandas.read_csv('prlab3dataset.csv')


def entropy(maleCount, femaleCount, totalData):
    return -(maleCount / totalData) * (math.log2(maleCount / totalData)) - (femaleCount / totalData) * (
        math.log2(femaleCount / totalData))


mainEntropy, maleCount, femaleCount = 0, 0, 0
totalData = len(data)

for datum in range(totalData):
    if data.iloc[datum]['class'] == 'm':
        maleCount += 1
    elif data.iloc[datum]['class'] == 'f':
        femaleCount += 1

mainEntropy = entropy(maleCount, femaleCount, totalData)

print("Main Entropy: ", mainEntropy)

hairLength = int(input("Enter the hair length <=: "))
yesCount, noCount, yesMaleCount, yesFemaleCount, noMaleCount, noFemaleCount = 0, 0, 0, 0, 0, 0

for datum in range(totalData):
    if data.iloc[datum]['hair length'] <= hairLength:
        yesCount += 1
        if data.iloc[datum]['class'] == 'm':
            yesMaleCount += 1
        elif data.iloc[datum]['class'] == 'f':
            yesFemaleCount += 1
    else:
        noCount += 1
        if data.iloc[datum]['class'] == 'm':
            noMaleCount += 1
        elif data.iloc[datum]['class'] == 'f':
            noFemaleCount += 1

hairLengthYesEntropy = entropy(maleCount, femaleCount, yesCount)
hairLengthNoEntropy = entropy(noMaleCount, noFemaleCount, noCount)

print("Hair Length Yes Entropy: ", hairLengthYesEntropy)
print("Hair Length No Entropy: ", hairLengthNoEntropy)
