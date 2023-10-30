import random
import math


# Makes the numbers closer towards the extremes, to test edge cases 
def pushTowardExtremes(num, minValue, maxValue):
    x = (num-minValue)/(maxValue-minValue) # Get percentage of how far the number is from the min and max
    intensity = 10 # How much it should be pushed towards the extremes (set close to 0 BUT NOT 0 for linear distribution)
    offset = ((math.atan(2*intensity*x-intensity)*math.pi)/(math.pi*math.atan(intensity))+1)/2 # Function from image
    newNum = offset*(maxValue-minValue)+minValue # Apply the offset to the number
    return int(newNum)

def generateRandom(min, max):
    return pushTowardExtremes(random.randint(min, max), min, max)

###### INPUT OPTIONS:

def Kzlitje():
    N = generateRandom(1, 100000)
    K = generateRandom(2, 10)
    A = generateRandom(1, 20)
    with open('test.in', 'w') as f:
        f.write(str(N) + " " + str(K) + " " + str(A) + "\n")
        for i in range(N):
            f.write(str(generateRandom(0, 1000000000)) + "\n")
            
def neboticniki():
    print("Implement later")