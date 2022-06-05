import pandas
import math
data = pandas.read_csv('prlab3dataset.csv')

def entropy(maleCount, femaleCount, totalData):
    return -(maleCount / totalData) * (math.log2(maleCount / totalData)) - (femaleCount / totalData) * (
        math.log2(femaleCount / totalData))

mainEntropy = 0
maleCount = 0
femaleCount = 0
totalData = len(data)

for datum in range(totalData):
    if data.iloc[datum]['class'] == 'm':
        maleCount += 1
    elif data.iloc[datum]['class'] == 'f':
        femaleCount += 1

mainEntropy = entropy(maleCount, femaleCount, totalData)

print("Main Entropy: ", mainEntropy)

hairLength = input("Enter the hair length <=: ")

for datum in range(totalData):
    if data.iloc[datum]['hair length'] <= hairLength:
        if data.iloc[datum]['class'] == 'm':
            maleCount += 1
        elif data.iloc[datum]['class'] == 'f':
            femaleCount += 1
hairLengthEntropy = entropy(maleCount, femaleCount, totalData)
print("Hair Length Entropy: ", hairLengthEntropy)





