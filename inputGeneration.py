import collections
import math
import os
import random

def inverted_extremes(num, minValue, maxValue, intensity): # (0,pi/2)
    if minValue>=maxValue:
        return maxValue
    x = (num-minValue)/(maxValue-minValue) # Get percentage of how far the number is from the min and max
    """ intensity = intensity  """# How much it should be pushed towards the extremes (set close to 0 BUT NOT 0 for linear distribution)
    offset = ((math.tan(2*intensity*x-intensity))/(math.tan(intensity))+1)/2.0 # Function from image
    newNum = offset*(maxValue-minValue)+minValue # Apply the offset to the number
    return int(round(newNum))

# Makes the numbers closer towards the extremes, to test edge cases 
def pushTowardExtremes(num, minValue, maxValue, intensity):
    if minValue>=maxValue:
        return maxValue
    x = (num-minValue)/(maxValue-minValue) # Get percentage of how far the number is from the min and max
    """ intensity = intensity  """# How much it should be pushed towards the extremes (set close to 0 BUT NOT 0 for linear distribution)
    offset = ((math.atan(2*intensity*x-intensity))/(math.atan(intensity))+1)/2 # Function from image
    newNum = offset*(maxValue-minValue)+minValue # Apply the offset to the number
    return int(round(newNum))

def pushTowardMaximum(num, minValue, maxValue, intensity):
    if minValue>=maxValue:
        return maxValue
    x = (num-minValue)/(maxValue-minValue) # Get percentage of how far the number is from the min and max
    offset = math.sqrt(x**intensity) # Function from image // intensity (0,2] // 2 is linear, smaller value more intense
    newNum = offset*(maxValue-minValue)+minValue # Apply the offset to the number
    return int(round(newNum))

def pushTowardMinimum(num, minValue, maxValue, intensity):
    if minValue>=maxValue:
        return maxValue
    x = (num-minValue)/(maxValue-minValue) # Get percentage of how far the number is from the min and max
    offset = intensity**(-x) # Function from image // intensity (1,inf)
    newNum = offset*(maxValue-minValue)+minValue # Apply the offset to the number
    return int(round(newNum))

def minimumValues(min, n):
    return [min for _ in range(n)]

def maximumValues(max, n):
    return [max for _ in range(n)]

def minToMax(n, min, max):
    return [min + (max-min)*i//n for i in range(n)]

def maxToMin(n, min, max):
    return [max - (max-min)*i//n for i in range(n)]

def print_congrats():
    congrats = """
   _____ ____  _   _  _____ _____         _______ _____ _         __    
  / ____/ __ \| \ | |/ ____|  __ \     /\|__   __/ ____| |       / /  _ 
 | |   | |  | |  \| | |  __| |__) |   /  \  | | | (___ | |      | |  (_)
 | |   | |  | | . ` | | |_ |  _  /   / /\ \ | |  \___ \| |      | |     
 | |___| |__| | |\  | |__| | | \ \  / ____ \| |  ____) |_|      | |   _ 
  \_____\____/|_| \_|\_____|_|  \_\/_/    \_\_| |_____/(_)      | |  (_)
                                                                 \_\    
    """
    print("\033[32m%s\033[0m" % congrats)
    print("Ten cycles completed with zero mistakes! Keep going! 😎")
    print("You truly are an APSTester! Keep on APSTesting! 😎")

tests_failed_counter = 0 # Update from tester.py

testCounter = 0
randomCounter = 0
empty_rand_detection = "emptyBro"
prevRandNum = empty_rand_detection
prevMin = 0
prevMax = 0
print_cycle_message = True
def generateRandom(min, max):
    
    global testsPassedCounter, totalTestsDoneCounter
    global testCounter, randomCounter
    global prevRandNum, prevMin, prevMax
    global print_cycle_message
    howManyVariations = 15
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
    elif randomCounter%howManyVariations == 0:
        if print_cycle_message and randomCounter//howManyVariations > 0:
            if (tests_failed_counter == 0):
                print("Cycle %d completed. Tests failed so far: [\033[32m%d\033[0m]" % ((randomCounter//howManyVariations), tests_failed_counter))
                if randomCounter//howManyVariations == 10:
                    print_congrats();
            else:
                print("Cycle %d completed. Tests failed so far: [\033[31m%d\033[0m]" % ((randomCounter//howManyVariations), tests_failed_counter))

            print_cycle_message = False
        intensity=10
        return pushTowardExtremes(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 1:
        print_cycle_message = True
        intensity=1000
        return pushTowardExtremes(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 2:
        intensity=100000
        return pushTowardExtremes(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 9:
        intensity=1000000000
        return pushTowardExtremes(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 12:
        intensity = 1
        return pushTowardExtremes(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 3:
        intensity=0.01
        return pushTowardMaximum(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 4:
        intensity=0.1
        return pushTowardMaximum(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 5:
        intensity=0.5
        return pushTowardMaximum(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 10:
        intensity=0.0001
        return pushTowardMaximum(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 14:
        intensity=0.000000001
        return pushTowardMaximum(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 6:
        intensity=100
        return pushTowardMinimum(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 7:
        intensity=100000
        return pushTowardMinimum(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 8:
        intensity=100000000
        return pushTowardMinimum(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 11:
        intensity=100000000000
        return pushTowardMinimum(randNum, min, max, intensity)
    elif randomCounter%howManyVariations == 13:
        intensity=1.5
        return inverted_extremes(randNum, min, max, intensity)
    
def generateRandomWord(min, max):
    # Generates a random word with a random length between min and max
    length = generateRandom(min, max)
    word = ""
    for _ in range(length):
        word += chr(random.randint(97, 122))
    return word

def generate_random_word_from_list(min, max, word_list):
    # Generates a random word with a random length between min and max
    length = generateRandom(min, max)
    word = ""
    
    for _ in range(length):
        word += random.choice(word_list)
    
    return word

maxInputs = 0
maxLength = 0
def setMaxInputs(n):
    global maxInputs
    maxInputs=n

def setMaxLength(n):
    global maxLength
    maxLength=n

def getMax(max):
    global maxInputs
    if maxInputs!=0:
        return maxInputs
    return max

def getMaxLength(max):
    global maxLength
    if maxLength!=0:
        return maxLength
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
    global testCounter, randomCounter
    inputTxt = ""
    max = 100000
    max = getMax(max)
    N = generateRandom(1, max)
    K = generateRandom(2, 10)
    A = generateRandom(1, 20)
    inputTxt += str(N) + " " + str(K) + " " + str(A) + "\n"
    for _ in range(N):
        inputTxt += str(generateRandom(0, 1000000000)) + "\n"
    testCounter+=1
    randomCounter+=1
    return inputTxt

def neboticniki():
    global testCounter, randomCounter
    inputTxt = ""
    max = 1000000
    max = getMax(max)
    N = generateRandom(1, max)
    inputTxt += str(N) + "\n"
    for _ in range(N):
        inputTxt += str(generateRandom(0, 1000000000)) + "\n"
    testCounter+=1
    randomCounter+=1
    return inputTxt

def mediane():
    global testCounter, randomCounter
    inputTxt = ""
    max = 100000
    max = getMax(max)
    N = generateRandom(1, max)
    inputTxt += str(N) + "\n"
    for _ in range(N):
        inputTxt += str(generateRandom(0, 1000000000)) + "\n"
    testCounter+=1
    randomCounter+=1
    return inputTxt

def setTestCounter(n):
    global testCounter
    testCounter = n;

def vreca():
    global randomCounter, testCounter
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
        if randomCounter==0:
            print("Stress tests over, starting random tests.")
        
        max = getMax(max)
        N = generateRandom(min, max)
        inputTxt += str(N) + "\n"
        for _ in range(N):
            s = random.randint(-1, 1)
            if s==1:
                s = random.randint(min, max)
            elif s==-1:
                s = random.randint(-max, -min)
            randomNumTempDeleteMe = generateRandom(min, max)
            if randomNumTempDeleteMe==0:
                print("oh goddddddddddddddddddddddddddddddddd. REPORT TO GONNADOSTUFF RIGHT NOW 😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭")
            inputTxt += str(s) + " " + str(randomNumTempDeleteMe) + "\n"
        randomCounter+=1


    testCounter+=1
    return inputTxt

def autocomplete():
    #Slovar vsebuje same razlicne besede. Prav tako so pomembnosti besed sama razlicna cela stevila.
    global allWords, testCounter, randomCounter

    inputTxt = ""
    
    if testCounter==0:
        inputTxt += "10\n"
        for i in range (10):
            for _ in range(10**5-1):
                inputTxt += chr(ord('a')+i)
            inputTxt += " " + str(i+1) + "\n"
        inputTxt += str(10**6) + "\n"
        for _ in range(10**6+1):
            inputTxt += "a\n"
    elif testCounter==1:
        inputTxt += "10\n"
        for i in range (10):
            for _ in range(10**5-1):
                inputTxt += chr(ord('a')+i)
            inputTxt += " " + str(i+1) + "\n"
        inputTxt += "10\n"
        for _ in range(10):
            for _ in range(10**5-1):
                inputTxt += "a"
            inputTxt += "\n"
    else:
        if randomCounter==0:
            print("Stress tests over, starting random tests.")
        # words
        max_word_length_sum = 1000000
        min_word_priority = 1
        max_word_priority = 1000000000
        N_max = 1000000
        N_max = getMax(N_max)
        
        # queries
        Q_max = N_max
        max_query_length_sum = 1000000
        max_random_word_length = 30
        
        # Randomly generate words remembering that their sum cannot be bigger than 10^6
        readSloveneFile()
        N = generateRandom(1, N_max)
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
        Q = generateRandom(1, Q_max)
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
        randomCounter+=1
    
    testCounter+=1
    return inputTxt

def vzorci():
    global testCounter, randomCounter
    inputTxt = ""
    
    characters = "abcdefghijklmnopqrstuvwxyz___"
    
    maxN = 50
    maxN = getMax(maxN)
    N = generateRandom(1, maxN)
    maxLen = 1000
    maxLen = getMaxLength(maxLen)
    inputTxt += str(N) + "\n"
    for _ in range(N):
        rand_sentence = generate_random_word_from_list(1, maxLen, characters)
        query = ""
        random_select = random.randint(0, 100)
        query = rand_sentence
        query = list(query)
        if random_select < 25: # Just replace random chars with * or ?
            how_many = generateRandom(0, len(rand_sentence))
            for _ in range(how_many):
                replace_symbol = "?"
                if random.randint(0, 1) == 0:
                    replace_symbol = "*"
                query[random.randint(0, len(query)-1)] = replace_symbol
        elif random_select < 50: # Just remove and replace random chars with * or ?
            how_many = generateRandom(0, len(rand_sentence))
            for _ in range(how_many):
                replace_symbol = "?"
                if random.randint(0, 1) == 0:
                    replace_symbol = "*"
                if random.randint(0, 2) == 0: # Remove random char
                    if len(query) > 1:
                        query[random.randint(0, len(query)-1)] = ""
                else: # Replace random char
                    query[random.randint(0, len(query)-1)] = replace_symbol
        elif random_select < 75: # Replace and add random chars with * or ?
            how_many = generateRandom(0, len(rand_sentence))
            for _ in range(how_many):
                replace_symbol = "?"
                if random.randint(0, 1) == 0:
                    replace_symbol = "*"
                if random.randint(0, 2) != 0: # Replace random char
                    query[random.randint(0, len(query)-1)] = replace_symbol
                else:
                    #query = query[:random.randint(0, len(query)-1)] + replace_symbol + query[random.randint(0, len(query)-1):]
                    query.insert(random.randint(0, len(query)-1), replace_symbol)
        else: # Generate new query
            query_characters = characters + "*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?"
            query = generate_random_word_from_list(1, maxLen, characters)
            query = list(query)
            
            
        if len(query) > maxLen:
            query = query[:maxLen]
        
        if not isinstance(query, list):
            print("Tests still being weird, contact GonnaDoStuff please.")
        
        query = "".join(query)
        
        if len(query) < 1:
            query = "a"
        if len(query) > maxLen:
            print("Query too long in test")
            exit(1)
        if len(rand_sentence) > maxLen:
            print("Rand sentence too long in test")
            exit(1)
        
        inputTxt += str(query) + " " + rand_sentence + "\n"
        
        split_split = inputTxt.split(" ")
        if len(split_split[0]) == 0:
            print(inputTxt)
            print(query)
            print("Despite everything, it's still you. And you make TERRIBLE CODE")
            print("Please contact GonnaDoStuff with the above message")
            exit(1)
        if len(split_split[1]) == 0:
            print(inputTxt)
            print(rand_sentence)
            print("Despite everything, it's still you. And you make TERRIBLE CODE part 2")
            print("Please contact GonnaDoStuff with the above message")
            exit(1)
    
    randomCounter+=1
    testCounter+=1
    return inputTxt

def razporeditev():
    global testCounter, randomCounter
    inputTxt = ""
    
    maxN = 100000
    maxM = 1000000
    maxN = getMax(maxN)
    maxM = getMaxLength(maxM)
    # randomCounter=13
    # testCounter = 5
    N = generateRandom(2, maxN)
    M = generateRandom(1, maxM)
    # N = 100000
    # M = 1000000
    
    step = random.randint(1, 2) # Decides if test will be solvable or -1
    start_pos = random.randint(1, 2) # Start on the first one or the second one
    
    
    pairs = []
    how_many_selected = 0
    
    nums = [i for i in range(start_pos, N+1, step)]
    random_choice = random.randint(0, 1)
    if random_choice == 0:
        random.shuffle(nums)
        
    # for which_first in range(start_pos,N+1, step):
    for which_first in nums:
        
        for which_second in range(which_first+1, N+1, step):
            if random.randint(0,100) < 90:
                continue
            current_pair = [which_first, which_second]
            random.shuffle(current_pair)
            pairs.append(current_pair)
            how_many_selected += 1
            if how_many_selected >= M:
                break
        if how_many_selected >= M:
            break
    
    if len(pairs) == 0:
        pairs.append([1,2])
    
    if len(pairs) < M:
        M = len(pairs)
    
    if M == 0:
        print("Something went wrong with this test.")
    
    random.shuffle(pairs)
    
    
    
    inputTxt += str(N) + " " + str(M) + "\n"
    for i in range(M):
        inputTxt += str(pairs[i][0]) + " " + str(pairs[i][1]) + "\n"
    
    
    testCounter+=1
    randomCounter+=1
    return inputTxt

def druganajkrajsa():
    global testCounter, randomCounter
    inputTxt = ""
    
    
    maxN = 2000
    maxM = 10000
    maxK = 10000
    maxN = getMax(maxN)
    maxM = getMaxLength(maxM)
    # randomCounter=13
    # testCounter = 5
    N = generateRandom(2, maxN)
    M = generateRandom(1, maxM)
    
    trios = []
    
    if random.randint(0, 3) == 0:
        # print("first")
        # Generate 10 random numbers leading from 0. Then 10 random leading from the last generated to 10 random
        
        nums = []
        N-=1
        for i in range(N):
            nums.append(i)
        
        # random.shuffle(nums)
        all_nums = []
        for i in range(N):
            all_nums.append(nums.copy())
        

        trios = []
        how_many_generated = 0
        last_generated_num = 0
        how_many_per_num = 10
        if N<20:
            how_many_per_num = N//3
        while how_many_generated < M//2-10 and how_many_generated < N*(N-2)//2:
            current_num = last_generated_num
            
            # if nums.count(current_num) == 0:
            #     indeks = random.randint(0, len(nums)-1)
            #     current_num = nums[indeks]
            
            # nums.remove(current_num)
            
            for _ in range(how_many_per_num):
                if how_many_generated >= M:
                    break
                if len(all_nums[current_num]) < 2:
                    last_generated_num = random.randint(0, N-1)
                    break
                current_random_num = current_num
                current_random_num_indeks = 0
                repeat_counter = 0
                while current_random_num == current_num:
                    if repeat_counter<10:
                        current_random_num_indeks = generateRandom(0, len(all_nums[current_num])-1)
                        current_random_num = all_nums[current_num][current_random_num_indeks]
                    elif repeat_counter<20:
                        current_random_num_indeks = random.randint(0, len(all_nums[current_num])-1)
                        current_random_num = all_nums[current_num][current_random_num_indeks]
                    # else:
                        # exit(1)
                    repeat_counter += 1
                
                # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                # print(current_num, current_random_num, current_random_num_indeks, all_nums[current_num])
                # print("-----------------------------------------")
                # print(all_nums[current_random_num])
                # print(current_num, current_random_num)
                # print(all_nums)
                all_nums[current_num].remove(current_random_num)
                all_nums[current_random_num].remove(current_num)
                current_trio = [current_num, current_random_num]
                random.shuffle(current_trio)
                current_trio.append(generateRandom(1, maxK))
                trios.append(current_trio)
                how_many_generated += 1
                last_generated_num = current_random_num
            
        how_many_generated1 = 0
        how_many_last_nums = 10
        if how_many_generated < how_many_last_nums:
            how_many_last_nums = how_many_generated
        
        # print("CAME")
        # for i in trios:
        #     for j in trios:
        #         if i == j:
        #             continue
        #         if i[0] == j[0] and i[1] == j[1] or i[0] == j[1] and i[1] == j[0]:
        #             print("UPSIE UPSIE UPSIE UPSIE XD IM LOSING SANITY WITH EACH PASSING DAY!!!!!!!!!!!!!!!!!!!!!")
        
        N+=1
        last_nums = []
        if how_many_last_nums != 0:
            for i in range(how_many_last_nums):
                last_nums.append(trios[-i-1][0])
        if len(last_nums) == 0:
            trios.append([0,N-1,maxK])
            last_nums.append(trios[0][1])
        
        prev_nums=[]
        
        for current_num in last_nums:
            if current_num == N-1:
                continue
            if current_num in prev_nums:
                continue
            prev_nums.append(current_num)
            current_trio = [current_num, N-1]
            random.shuffle(current_trio)
            current_trio.append(generateRandom(1, maxK))
            trios.append(current_trio)
            how_many_generated1 += 1
        
        # if len(trios) != M:
        M=len(trios)
        
        # for x in trios:
        #     if x[0] == x[1]:
        #         print("UPSIE XD THE FIRST THE ORIGINAL<---------------------------------------------------------------------")
        #         break
        
        # for i in trios:
        #     for j in trios:
        #         if i == j:
        #             continue
        #         if i[0] == j[0] and i[1] == j[1] or i[0] == j[1] and i[1] == j[0]:
        #             print(i[0], i[1], j[0], j[1])
        #             print("UPSIE UPSIE UPSIE UPSIE XD IM LOSING SANITY WITH EACH PASSING DAY")
        #             return "2 1 0 1 1"
        
        
    elif random.randint(0, 80) == 0:
        # print("second")
        
        N = 2000
        trios = []
        for i in range(1998):
            if i > 0:
                trios.append([0, i, 1])
            trios.append([i, 1999, 1])
            if i>0:
                trios.append([i, i+1, 1])
            if i<1996 and i>1:
                trios.append([i, i+2, 1])
            if i>4:
                trios.append([1, i, 1])
        
        M = len(trios)
        
        # for x in trios:
        #     if x[0] == x[1]:
        #         print("UPSIE XD HOW THE HECK THO")
        
        # for i in trios:
        #     for j in trios:
        #         if i == j:
        #             continue
        #         if i[0] == j[0] and i[1] == j[1] or i[0] == j[1] and i[1] == j[0]:
        #             print("UPSIE UPSIE UPSIE UPSIE XD IMMA BE QUIET")
        
    elif random.randint(0, 100) == 0:
        # print("third")
        N = 150
        trios = []
        for i in range(N):
            for j in range(i+1, N):
                trios.append([i, j, 1])
        M = len(trios)
        
        # for i in trios:
        #     for j in trios:
        #         if i == j:
        #             continue
        #         if i[0] == j[0] and i[1] == j[1] or i[0] == j[1] and i[1] == j[0]:
        #             print("UPSIE UPSIE UPSIE UPSIE XD IM THE GOOFFBALLLL")
        # print(M)
    elif random.randint(0, 50) == 0:
        N = 2000
        trios = []
        for i in range(0, 1998, 2):
            trios.append([i, i+2, 2])
            trios.append([i, i+1,1])
            trios.append([i+1, i+2, 1])
        # trios.append([1998, 1999, 1])
        M = len(trios)
        
        # for i in trios:
        #     for j in trios:
        #         if i == j:
        #             continue
        #         if i[0] == j[0] and i[1] == j[1] or i[0] == j[1] and i[1] == j[0]:
        #             print("UPSIE UPSIE UPSIE UPSIE XD NO MEEEEE")
    else:
        # print("fourth")
        step = random.randint(1, 2) # Decides if test will be solvable or -1
        
        trios = []
        how_many_selected = 0
        
        nums = [i for i in range(0, N, step)]
        random_choice = random.randint(0, 1)
        if random_choice == 0:
            random.shuffle(nums)
        
        nums_copy = nums.copy()
        random.shuffle(nums_copy)
        
        trios = []
        how_many_selected = 0
        
        nums = [i for i in range(0, N+1, step)]
        random_choice = random.randint(0, 1)
        if random_choice == 0:
            random.shuffle(nums)
            
        # for which_first in range(start_pos,N+1, step):
        for which_first in nums:
            
            for which_second in range(which_first+1, N, step):
                if random.randint(0,100) < 90:
                    continue
                current_trio = [which_first, which_second]
                random.shuffle(current_trio)
                current_trio.append(generateRandom(1, maxK))
                trios.append(current_trio)
                how_many_selected += 1
                if how_many_selected >= M:
                    break
            if how_many_selected >= M:
                break
            
        # for which_first in range(start_pos,N+1, step):
        # for which_first in nums:
            
        #     nums.remove(which_first)
        #     for which_second in nums_copy:
        #         if random.randint(0,100) < 90:
        #             continue
        #         current_pair = [which_first, which_second]
        #         random.shuffle(current_pair)
        #         current_pair.append(generateRandom(1, maxK))
        #         trios.append(current_pair)
        #         how_many_selected += 1
        #         if how_many_selected >= M:
        #             break
        #     if how_many_selected >= M:
        #         break
        
        
        for x in trios:
            if x[0] == x[1]:
                # print("UPSIE XD")
                trios.remove(x)
        
        # if len(trios) == 0:
        if random.randint(0, 1) == 0:
            is_good=True
            for i in trios:
                if i[0] == 0 and i[1] == N-1 or i[0] == N-1 and i[1] == 0:
                    is_good=False
                    break
            if is_good:
                trios.append([0,N-1,maxK])
        
        if len(trios) == 0:
            trios.append([0,N-1,maxK])
        
        
        # if len(trios) < M:
        M = len(trios)
        if M == 0:
            print("Something went wrong with this test.<-----------------")
            
        # for x in trios:
        #     if x[0] == x[1]:
        #         print("UPSIE XD<---------------------------------------------------------------------")
        
        # for i in trios:
        #     for j in trios:
        #         if i == j:
        #             continue
        #         if i[0] == j[0] and i[1] == j[1] or i[0] == j[1] and i[1] == j[0]:
        #             print("UPSIE UPSIE UPSIE UPSIE XD I DID THISSSSS")
    
    # for x in trios:
    #     if x[0] == x[1]:
    #         print("UPSIE XD")
    
    # for i in trios:
    #     for j in trios:
    #         if i == j:
    #             continue
    #         if i[0] == j[0] and i[1] == j[1] or i[0] == j[1] and i[1] == j[0]:
    #             print("UPSIE UPSIE UPSIE UPSIE XD")
    #             break
            
    # for x in trios:
    #     if x[0] == x[1]:
    #         print("UPSIE XD")
        #---------------------------------------------------------------------------
        
        # step = random.randint(1, 2) # Decides if test will be solvable or -1
    
        # trios = []
        # how_many_selected = 0
        
        # nums = [i for i in range(0, N, step)]
        # random_choice = random.randint(0, 1)
        # if random_choice == 0:
        #     random.shuffle(nums)
            
        # # for which_first in range(start_pos,N+1, step):
        # for which_first in nums:
            
        #     for which_second in range(which_first+1, N, step):
        #         if random.randint(0,100) < 90:
        #             continue
        #         current_pair = [which_first, which_second, generateRandom(1, maxK)]
        #         # random.shuffle(current_pair)
        #         trios.append(current_pair)
        #         how_many_selected += 1
        #         if how_many_selected >= M:
        #             break
        #     if how_many_selected >= M:
        #         break
        
        # # if len(trios) == 0:
        # if random.randint(0, 1) == 0 or len(trios) == 0:
        #     trios.append([0,N-1,maxK])
        
        # # if len(trios) < M:
        # M = len(trios)
        
        # if M == 0:
        #     print("Something went wrong with this test.")
            
        # for x in trios:
        #     if x[0] == x[1]:
        #         print("UPSIE XD")
        
    if M == 0:
        print("Something went wrong with this test.")
        
    # random.shuffle(trios)
    
    inputTxt += str(N) + " " + str(M) + "\n"
    for i in range(len(trios)):
        inputTxt += str(trios[i][0]) + " " + str(trios[i][1]) + " " + str(trios[i][2]) + "\n";
    
    testCounter+=1
    randomCounter+=1
    return inputTxt

def otoki():
    global testCounter, randomCounter
    input_txt = ""
    
    # 1 <= V,S
    # V * S <= 10^5
    # 0 <= H <= 10^5
    
    maxN = 10**5 # Height and width limit
    maxN = getMax(maxN)
    
    maxH = 10**5 # Height limit
    maxH = getMaxLength(maxH)
    
    if testCounter == 0:
        input_txt += "1 100000\n"
        for i in range(100000):
            input_txt += str(i) + " "
        input_txt += "\n"
    elif testCounter == 1:
        input_txt += "100000 1\n"
        for i in range(100000):
            input_txt += str(i) + "\n"
    elif testCounter == 2:
        input_txt += "316 316\n"
        for i in range(316):
            for j in range(316):
                input_txt += str(i+316*j) + " "
            input_txt += "\n"
    elif testCounter == 3:
        input_txt += "316 316\n"
        for i in range(316):
            for j in range(316):
                if i%2==0 or j%2==0:
                    input_txt += str(0) + " "
                else:
                    input_txt += str(i+j+1) + " "
            input_txt += "\n"
    elif testCounter == 4:
        input_txt += "316 316\n"
        height_counter = 100000
        small_height_counter = 1
        for i in range(0,316,1):
            for j in range(0,316,2):
                if i%2==0:
                    input_txt += str(height_counter) + " " + str(small_height_counter) + " "
                else:
                    input_txt += str(small_height_counter) + " " + str(height_counter) + " "
                height_counter -= 1
                small_height_counter += 1
            input_txt += "\n"
    elif testCounter == 5:
        input_txt += "316 316\n"
        height_counter = 100000
        small_height_counter = 1
        for i in range(0,316,1):
            for j in range(0,316,2):
                if i%2==0:
                    input_txt += str(height_counter) + " " + str(small_height_counter) + " "
                else:
                    input_txt += str(small_height_counter) + " " + str(height_counter) + " "
            input_txt += "\n"
    elif testCounter == 6:
        input_txt += "316 316\n"
        height_counter = 100000
        small_height_counter = 1
        for i in range(0,316,1):
            for j in range(0,316,2):
                input_txt += str(height_counter) + " " + str(small_height_counter) + " "
            input_txt += "\n"
    elif testCounter == 7:
        input_txt += "316 316\n"
        height_counter = 100000
        small_height_counter = 0
        for i in range(0,316,1):
            for j in range(0,316,2):
                if i%2==0:
                    input_txt += str(height_counter) + " " + str(small_height_counter) + " "
                else:
                    input_txt += str(small_height_counter) + " " + str(height_counter) + " "
            input_txt += "\n"
    
    else:
        if randomCounter==0:
            print("Stress tests over, starting random tests.")
        
        V = generateRandom(1, maxN) # height
        S = generateRandom(1, maxN) # width
        if (V*S > 10**5):
            if random.randint(0, 1) == 0:
                if random.randint(0,5) != 0:
                    S = int(math.sqrt(S))
                V = 10**5 // S
            else:
                if random.randint(0,5) != 0:
                    V = int(math.sqrt(V))
                S = 10**5 // V
        
        H = generateRandom(0, maxH)
        if (H > 10**5):
            H = 10**5
            print("Something strange happened. H was bigger than 10^5. Please report this to GonnadoStuff.")
        
        input_txt += str(V) + " " + str(S) + "\n"
        
        if random.randint(0, 1) == 0:
            for _ in range(V):
                for s in range(S):
                    random_height = generateRandom(0, H)
                    if (s>0):
                        input_txt += " "
                    input_txt += str(random_height)
                input_txt += "\n"
        else:
            coords = []
            board = [[-1 for _ in range(S)] for _ in range(V)]
            how_many_peaks = generateRandom(1, V*S)
            for _ in range(how_many_peaks):
                coords.append([generateRandom(0, S-1), generateRandom(0, V-1)])
                
            new_coords = []
            for coord in coords:
                if board[coord[1]][coord[0]] != -1:
                    continue
                height = generateRandom(0, H)
                board[coord[1]][coord[0]] = height
                if coord[0]-1 >= 0 and board[coord[1]][coord[0]-1] == -1:
                    new_coords.append([coord[0]-1, coord[1], height])
                if coord[0]+1 < S and board[coord[1]][coord[0]+1] == -1:
                    new_coords.append([coord[0]+1, coord[1], height])
                if coord[1]-1 >= 0 and board[coord[1]-1][coord[0]] == -1:
                    new_coords.append([coord[0], coord[1]-1, height])
                if coord[1]+1 < V and board[coord[1]+1][coord[0]] == -1:
                    new_coords.append([coord[0], coord[1]+1, height])
            
            while len(new_coords) > 0:
                # if len(new_coords)%1000 == 0:
                #     print(len(new_coords))
                coord = new_coords[0]
                if board[coord[1]][coord[0]] == -1:
                    height = coord[2]
                    height = height-pushTowardMinimum(random.randint(0,height), 0, height, 100)
                    board[coord[1]][coord[0]] = height
                    
                    if coord[0]-1 >= 0 and board[coord[1]][coord[0]-1] == -1:
                        new_coords.append([coord[0]-1, coord[1], height])
                    if coord[0]+1 < S and board[coord[1]][coord[0]+1] == -1:
                        new_coords.append([coord[0]+1, coord[1], height])
                    if coord[1]-1 >= 0 and board[coord[1]-1][coord[0]] == -1:
                        new_coords.append([coord[0], coord[1]-1, height])
                    if coord[1]+1 < V and board[coord[1]+1][coord[0]] == -1:
                        new_coords.append([coord[0], coord[1]+1, height])
                new_coords.pop(0)
            
            for i in range(V):
                for j in range(S):
                    if j>0:
                        input_txt += " "
                    input_txt += str(board[i][j])
                input_txt += "\n"
            
            
        randomCounter+=1

    testCounter+=1
    return input_txt

def empty():
    global testCounter, randomCounter
    input_txt = ""
    
    # Input generation code here:
    
    
    randomCounter+=1
    testCounter+=1
    return input_txt

def funkcije():
    global testCounter, randomCounter
    input_txt = ""
    
    if testCounter == 0:
        input_txt += "2 2\n1 2\n999999999 1000000000"
    
    # Input generation code here:
    # 1 <= N <= 1000
    # 1 <= ai <= bi <= 10^9
    # 1 <= k <= sum(bi-ai+1)
    else:
        if randomCounter==0:
            print("Manual tests over, starting random tests.")
        maxN = 1000
        maxN = getMax(maxN)
        maxNum = 10**9
        maxNum = getMax(maxNum)
        
        N = generateRandom(1, maxN)
        
        pairs = []
        for i in range(N):
            a = generateRandom(1, maxNum)
            b = generateRandom(a, maxNum)
            pairs.append([a, b])
        
        k = generateRandom(1, sum(b-a+1 for a, b in pairs))
        
        input_txt += str(N) + " " + str(k) + "\n"
        for i in range(N):
            input_txt += str(pairs[i][0]) + " " + str(pairs[i][1]) + "\n"
        
        randomCounter+=1
    testCounter+=1
    return input_txt

def pretvorba():
    global testCounter, randomCounter
    input_txt = ""
    
    if testCounter == 0:
        input_txt+="0 1 0\n"
        input_txt+="T\n"
        input_txt+="TFPDM"
    else:
        if randomCounter==0:
            print("Manual tests over, starting random tests.")
    
        # Input generation code here:
        maxS = 1000
        maxT = 1000
        
        maxS = getMax(maxS)
        maxT = getMax(maxT)
        
        Slen = generateRandom(1, maxS)
        Tlen = generateRandom(1, maxT)
        
        S = generateRandomWord(1, Slen)
        T = generateRandomWord(1, Tlen)
        
        S = S.upper()
        T = T.upper()
        
        maxNum = 1000
        maxNum = getMaxLength(maxNum)
        x = generateRandom(0, maxNum)
        y = generateRandom(0, maxNum)
        z = generateRandom(0, maxNum)
        
        input_txt += str(x) + " " + str(y) + " " + str(z) + "\n"
        input_txt += S + "\n"
        input_txt += T + "\n"
        
        
        randomCounter+=1
    testCounter+=1
    return input_txt

def zemljisce():
    global testCounter, randomCounter
    input_txt = ""
    
    # Input generation code here:
    if testCounter == 0:
        input_txt += "1\n"
        input_txt += "1 1 1 1 1 2 1 2\n"
    else:
        if randomCounter==0:
            print("Manual tests over, starting random tests.")
        maxT = 1000
        maxT = getMax(maxT)
        T = generateRandom(1, maxT)
        maxDistance = 10000
        maxDistance = getMaxLength(maxDistance)
        
        input_txt += str(T) + "\n"
        for i in range(T):
            x1 = generateRandom(-maxDistance, maxDistance)
            y1 = generateRandom(-maxDistance, maxDistance)
            x2 = generateRandom(-maxDistance, maxDistance)
            y2 = generateRandom(-maxDistance, maxDistance)
            x3 = generateRandom(-maxDistance, maxDistance)
            y3 = generateRandom(-maxDistance, maxDistance)
            x4 = generateRandom(-maxDistance, maxDistance)
            y4 = generateRandom(-maxDistance, maxDistance)
            
            input_txt += str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + " " + str(x3) + " " + str(y3) + " " + str(x4) + " " + str(y4) + "\n"
        
        
        randomCounter+=1
    testCounter+=1
    return input_txt