# create test data for knapsack problem

import sys
import random

testFile = open(sys.argv[1], 'w')
numTests = int(sys.argv[2])
maxValue = int(sys.argv[3])
testFile.write(str(numTests) + "\n")
testFile.write(str(maxValue) + "\n")
for num in range (1,numTests+1):
    weight = random.randint(1,50)
    value = random.randint(1,10)
    testFile.write(str(weight) + " " + str(value) + "\n")
testFile.close()
