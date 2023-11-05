import random
import math


# Makes the numbers closer towards the extremes, to test edge cases 
def pushTowardExtremes(num, minValue, maxValue, intensity):
    x = (num-minValue)/(maxValue-minValue) # Get percentage of how far the number is from the min and max
    """ intensity = intensity  """# How much it should be pushed towards the extremes (set close to 0 BUT NOT 0 for linear distribution)
    offset = ((math.atan(2*intensity*x-intensity)*math.pi)/(math.pi*math.atan(intensity))+1)/2 # Function from image
    newNum = offset*(maxValue-minValue)+minValue # Apply the offset to the number
    return int(newNum)

counter = 0
def generateRandom(min, max):
    global counter
    intensity = 10
    if counter%3 == 0:
        intensity=10
    elif counter%3 == 1:
        intensity=1000
    else:
        intensity=100000
    counter += 1
    return pushTowardExtremes(random.randint(min, max), min, max, intensity)

###### INPUT OPTIONS:

def Kzlitje():
    inputTxt = ""
    N = generateRandom(1, 100000)
    K = generateRandom(2, 10)
    A = generateRandom(1, 20)
    inputTxt += str(N) + " " + str(K) + " " + str(A) + "\n"
    for _ in range(N):
        inputTxt += str(generateRandom(0, 1000000000)) + "\n"
    return inputTxt

def neboticniki():
    inputTxt = ""
    N = generateRandom(1, 1000000)
    inputTxt += str(N) + "\n"
    for _ in range(N):
        inputTxt += str(generateRandom(0, 1000000000)) + "\n"
    return inputTxt

def mediane():
    inputTxt = ""
    N = generateRandom(1, 100000)
    inputTxt += str(N) + "\n"
    for _ in range(N):
        inputTxt += str(generateRandom(0, 1000000000)) + "\n"
    return inputTxt

def vreca():
    inputTxt = ""
    N = generateRandom(1, 1000000)
    inputTxt += str(N) + "\n"
    for _ in range(N):
        s = random.randint(-1, 1)
        inputTxt += str(s) + " " + str(generateRandom(0, 1000000)) + "\n"
    return inputTxt