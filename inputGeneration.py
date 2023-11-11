import collections
import math
import os
import random


# Makes the numbers closer towards the extremes, to test edge cases 
def pushTowardExtremes(num, minValue, maxValue, intensity):
    x = (num-minValue)/(maxValue-minValue) # Get percentage of how far the number is from the min and max
    """ intensity = intensity  """# How much it should be pushed towards the extremes (set close to 0 BUT NOT 0 for linear distribution)
    offset = ((math.atan(2*intensity*x-intensity))/(math.atan(intensity))+1)/2 # Function from image
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
empty_rand_detection = "emptyBro"
prevRandNum = empty_rand_detection
prevMin = 0
prevMax = 0
def generateRandom(min, max):
    
    global testCounter
    global prevRandNum, prevMin, prevMax
    howManyVariations = 13
    intensity = 10
    
    randNum = 0
    
    if random.randint(0,25) == 0 and str(prevRandNum) != empty_rand_detection and prevMin == min and prevMax == max:
        randNum = prevRandNum
    else:
        randNum = random.randint(min, max)
        prevRandNum = randNum
        prevMin = min
        prevMax = max
    
    if testCounter==0:
        return min
    elif testCounter==1:
        return max
    elif testCounter%howManyVariations == 0:
        print("Cycle %d comepleted" % (testCounter//howManyVariations))
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
    elif testCounter%howManyVariations == 12:
        intensity = 1
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
    
def generateRandomWord(min, max):
    # Generates a random word with a random length between min and max
    length = generateRandom(min, max)
    if length > 30:
        print("YOOOOOOOOOOOOOOOOOOOOOhereherhehrhe " + str(min) + " " + str(max))
    word = ""
    for _ in range(length):
        word += chr(generateRandom(97, 122))
    return word

maxInputs = 0
def setMaxInputs(n):
    global maxInputs
    maxInputs=n

def setMax(max):
    global maxInputs
    if not maxInputs==0:
        return maxInputs
    return max




allWords = []
sloveneWordsFile = os.path.join("supportFiles","allSloveneWords.txt")
gotSloveneFile = False

def readSloveneFile():
    global gotSloveneFile
    global allWords
    if gotSloveneFile:
        return

    with open(sloveneWordsFile, 'r') as f:
        fullFile = f.read()
        fullFile = fullFile.split("\n")
        seen = set()
        allWords = []
        for x in fullFile:
            if x not in seen:
                allWords.append(x)
                seen.add(x)
        
    gotSloveneFile = True

###### INPUT OPTIONS:

def Kzlitje():
    global testCounter
    inputTxt = ""
    max = 100000
    max = setMax(max)
    N = generateRandom(1, max)
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
    max = 1000000
    max = setMax(max)
    N = generateRandom(1, max)
    inputTxt += str(N) + "\n"
    for _ in range(N):
        inputTxt += str(generateRandom(0, 1000000000)) + "\n"
    testCounter+=1
    return inputTxt

def mediane():
    global testCounter
    inputTxt = ""
    max = 100000
    max = setMax(max)
    N = generateRandom(1, max)
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
        
        max = setMax(max)
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

def autocomplete():
    #Slovar vsebuje same razlicne besede. Prav tako so pomembnosti besed sama razlicna cela stevila.
    global allWords, testCounter
    
    inputTxt = ""
    
    # words
    max_word_length_sum = 1000000
    min_word_priority = 1
    max_word_priority = 1000000000
    
    # queries
    max_query_length_sum = 1000000
    max_random_word_length = 30
    
    # Randomly generate words remembering that their sum cannot be bigger than 10^6
    readSloveneFile()
    N = generateRandom(1, 1000000)
    selected_words = random.sample(allWords, N if N<len(allWords) else len(allWords))
    word_length_sum = sum(len(i) for i in selected_words)
    # print(word_length_sum)
    if word_length_sum > max_word_length_sum:
        while word_length_sum > max_word_length_sum:
            current_word = selected_words[-1]
            word_length_sum -= len(current_word)
            selected_words.pop()
    N = len(selected_words)
    
    # Randomly generate priorities for the words
    word_priority_list = random.sample(range(min_word_priority, max_word_priority), N)
    
    # Add the words and priorities to the inputTxt
    inputTxt += str(N) + "\n"
    for i in range(N):
        inputTxt += selected_words[i] + " " + str(word_priority_list[i]) + "\n"
    
    # Generate the queries
    # Some queries will be random chars, while some will be shortened words from selected_words
    Q = generateRandom(1, 1000000)
    query_list = []
    query_list_length_sum = 0
    while query_list_length_sum < 1000000 and len(query_list) < Q:
        random_num = random.randint(0, 100)
        current_word = ""
        if random_num < 10:
            current_word = generateRandomWord(1, max_random_word_length)
            query_list.append(current_word)
        else:
            current_word = random.choice(selected_words)
            current_word_len = len(current_word)
            current_word = current_word[:random.randint(1, current_word_len)]
            query_list.append(current_word)
        query_list_length_sum += len(current_word)
    
    if query_list_length_sum > max_query_length_sum:
        query_list.pop()
    
    if len(query_list) < Q:
        Q = len(query_list)
    
    # Add the queries to the inputTxt
    inputTxt += str(Q) + "\n"
    for i in range(Q):
        inputTxt += query_list[i] + "\n"
    
    print (inputTxt)
    testCounter+=1

autocomplete()