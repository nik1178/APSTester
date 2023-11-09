import random
import math


# Makes the numbers closer towards the extremes, to test edge cases 
def pushTowardExtremes(num, minValue, maxValue, intensity):
    x = (num-minValue)/(maxValue-minValue) # Get percentage of how far the number is from the min and max
    """ intensity = intensity  """# How much it should be pushed towards the extremes (set close to 0 BUT NOT 0 for linear distribution)
    offset = ((math.atan(2*intensity*x-intensity)*math.pi)/(math.pi*math.atan(intensity))+1)/2 # Function from image
    newNum = offset*(maxValue-minValue)+minValue # Apply the offset to the number
    return int(newNum)

def pushTowardMaximum(num, minValue, maxValue, intensity):
    x = (num-minValue)/(maxValue-minValue) # Get percentage of how far the number is from the min and max
    offset = math.sqrt(x**intensity) # Function from image // intensity (0,2] // 2 is linear, smaller value more intense
    newNum = offset*(maxValue-minValue)+minValue # Apply the offset to the number
    return int(newNum)

def pushTowardMinimum(num, minValue, maxValue, intensity):
    x = (num-minValue)/(maxValue-minValue) # Get percentage of how far the number is from the min and max
    offset = intensity**(-x) # Function from image // intensity (1,inf)
    newNum = offset*(maxValue-minValue)+minValue # Apply the offset to the number
    return int(newNum)

        

def minimumValues(min, n):
    return [min for _ in range(n)]

def maximumValues(max, n):
    return [max for _ in range(n)]

def minToMax(n, min, max):
    return [min + (max-min)*i//n for i in range(n)]

def maxToMin(n, min, max):
    return [max - (max-min)*i//n for i in range(n)]

testCounter = 0
prevRandNum = 0
def generateRandom(min, max):
    
    global testCounter
    global prevRandNum
    howManyVariations = 12
    intensity = 10
    
    randNum = 0
    
    if random.randint(0,25) == 0:
        randNum = prevRandNum
    else:
        randNum = random.randint(min, max)
        prevRandNum = randNum
    
    if testCounter==0:
        return min
    elif testCounter==1:
        return max
    elif testCounter%howManyVariations == 0:
        intensity=10
        return pushTowardExtremes(randNum, min, max, intensity)
    elif testCounter%howManyVariations == 1:
        intensity=1000
        return pushTowardExtremes(randNum, min, max, intensity)
    elif testCounter%howManyVariations == 2:
        intensity=100000
        return pushTowardExtremes(randNum, min, max, intensity)
    elif testCounter%howManyVariations == 9:
        intensity=1000000000
        return pushTowardExtremes(randNum, min, max, intensity)
    elif testCounter%howManyVariations == 3:
        intensity=0.01
        return pushTowardMaximum(randNum, min, max, intensity)
    elif testCounter%howManyVariations == 4:
        intensity=0.1
        return pushTowardMaximum(randNum, min, max, intensity)
    elif testCounter%howManyVariations == 5:
        intensity=0.5
        return pushTowardMaximum(randNum, min, max, intensity)
    elif testCounter%howManyVariations == 10:
        intensity=0.0001
        return pushTowardMaximum(randNum, min, max, intensity)
    elif testCounter%howManyVariations == 6:
        intensity=100
        return pushTowardMinimum(randNum, min, max, intensity)
    elif testCounter%howManyVariations == 7:
        intensity=100000
        return pushTowardMinimum(randNum, min, max, intensity)
    elif testCounter%howManyVariations == 8:
        intensity=100000000
        return pushTowardMinimum(randNum, min, max, intensity)
    elif testCounter%howManyVariations == 11:
        intensity=100000000000
        return pushTowardMinimum(randNum, min, max, intensity)

###### INPUT OPTIONS:

def Kzlitje():
    global testCounter
    inputTxt = ""
    N = generateRandom(1, 100000)
    K = generateRandom(2, 10)
    A = generateRandom(1, 20)
    inputTxt += str(N) + " " + str(K) + " " + str(A) + "\n"
    for _ in range(N):
        inputTxt += str(generateRandom(0, 1000000000)) + "\n"
    testCounter+=1
    return inputTxt

def neboticniki():
    global testCounter
    inputTxt = ""
    N = generateRandom(1, 1000000)
    inputTxt += str(N) + "\n"
    for _ in range(N):
        inputTxt += str(generateRandom(0, 1000000000)) + "\n"
    testCounter+=1
    return inputTxt

def mediane():
    global testCounter
    inputTxt = ""
    N = generateRandom(1, 100000)
    inputTxt += str(N) + "\n"
    for _ in range(N):
        inputTxt += str(generateRandom(0, 1000000000)) + "\n"
    testCounter+=1
    return inputTxt

def setTestCounter(n):
    global testCounter
    testCounter = n;

def vreca():
    global testCounter
    inputTxt = ""
    
    min = 1
    max = 1000000
    if testCounter==0:
        N = 1
        inputTxt += str(N) + "\n"
        inputTxt += "".join("-1 " + str(x) + "\n" for x in minToMax(1, min, max))
    elif testCounter==1:
        N = 1
        inputTxt += str(N) + "\n"
        inputTxt += "".join("-1 " + str(x) + "\n" for x in maxToMin(1, min, max))
    elif testCounter==2:
        N = 1
        inputTxt += str(N) + "\n"
        inputTxt += "".join("-1 " + str(x) + "\n" for x in minimumValues(min, 1))
    elif testCounter==3:
        N = 1
        inputTxt += str(N) + "\n"
        inputTxt += "".join("-1 " + str(x) + "\n" for x in maximumValues(max, 1))
    elif testCounter==4:
        N = max
        inputTxt += str(N) + "\n"
        inputTxt += "".join("-1 " + str(x) + "\n" for x in minToMax(max, min, max))
    elif testCounter==5:
        N = max
        inputTxt += str(N) + "\n"
        inputTxt += "".join("-1 " + str(x) + "\n" for x in maxToMin(max, min, max))
    elif testCounter==6:
        N = max
        inputTxt += str(N) + "\n"
        inputTxt += "".join("-1 " + str(x) + "\n" for x in minimumValues(min, max))
    elif testCounter==7:
        N = max
        inputTxt += str(N) + "\n"
        inputTxt += "".join("-1 " + str(x) + "\n" for x in maximumValues(max, max))
    elif testCounter==8:
        N = min
        inputTxt += str(N) + "\n"
        inputTxt += "".join("0  " + str(x) + "\n" for x in minToMax(1, min, max))
    elif testCounter==9:
        N = min
        inputTxt += str(N) + "\n"
        inputTxt += "".join("0 " + str(x) + "\n" for x in maxToMin(1, min, max))
    elif testCounter==10:
        N = min
        inputTxt += str(N) + "\n"
        inputTxt += "".join("0 " + str(x) + "\n" for x in minimumValues(min, 1))
    elif testCounter==11:
        N = min
        inputTxt += str(N) + "\n"
        inputTxt += "".join("0 " + str(x) + "\n" for x in maximumValues(max, 1))
    elif testCounter==12:
        N = max
        inputTxt += str(N) + "\n"
        inputTxt += "".join("0 " + str(x) + "\n" for x in minToMax(max, min, max))
    elif testCounter==13:
        N = max
        inputTxt += str(N) + "\n"
        inputTxt += "".join("0 " + str(x) + "\n" for x in maxToMin(max, min, max))
    elif testCounter==14:
        N = max
        inputTxt += str(N) + "\n"
        inputTxt += "".join("0 " + str(x) + "\n" for x in minimumValues(min, max))
    elif testCounter==15:
        N = max
        inputTxt += str(N) + "\n"
        inputTxt += "".join("0 " + str(x) + "\n" for x in maximumValues(max, max))
    elif testCounter==16:
        N = min
        inputTxt += str(N) + "\n"
        inputTxt += "".join("1  " + str(x) + "\n" for x in minToMax(1, min, max))
    elif testCounter==17:
        N = min
        inputTxt += str(N) + "\n"
        inputTxt += "".join("1 " + str(x) + "\n" for x in maxToMin(1, min, max))
    elif testCounter==18:
        N = min
        inputTxt += str(N) + "\n"
        inputTxt += "".join("1 " + str(x) + "\n" for x in minimumValues(min, 1))
    elif testCounter==19:
        N = min
        inputTxt += str(N) + "\n"
        inputTxt += "".join("1 " + str(x) + "\n" for x in maximumValues(max, 1))
    elif testCounter==20:
        N = max
        inputTxt += str(N) + "\n"
        inputTxt += "".join("1 " + str(x) + "\n" for x in minToMax(max, min, max))
    elif testCounter==21:
        N = max
        inputTxt += str(N) + "\n"
        inputTxt += "".join("1 " + str(x) + "\n" for x in maxToMin(max, min, max))
    elif testCounter==22:
        N = max
        inputTxt += str(N) + "\n"
        inputTxt += "".join("1 " + str(x) + "\n" for x in minimumValues(min, max))
    elif testCounter==23:
        N = max
        inputTxt += str(N) + "\n"
        inputTxt += "".join("1 " + str(x) + "\n" for x in maximumValues(max, max))
        
    
    else:
        if testCounter==24:
            print("Stress tests over, starting random tests.")
        
        N = generateRandom(min, max)
        inputTxt += str(N) + "\n"
        for _ in range(N):
            s = random.randint(-1, 1)
            if s==1:
                s = random.randint(min, max)
            elif s==-1:
                s = random.randint(-max, -min)
            inputTxt += str(s) + " " + str(generateRandom(min, max)) + "\n"


    testCounter+=1
    return inputTxt