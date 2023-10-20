import subprocess
import os
import sys
import time
import math
import random

workingOutputFolderName = "workingOutputs"
userOutputFolderName = "userOutput"

workingProgramsFolderName = "workingPrograms"

allOutputsFolderName = "allOutputs"

def runCPPProgram(programName):
    # Command to run the C++ program and get its output 
    runArguments = [programName," < test.in"]
    runCommand = "".join(str(x) for x in runArguments)
    # Run the C++ program 
    try:
        runProcess = subprocess.run([runCommand], capture_output=True, timeout=2, text=True, shell=True)
        return runProcess.stdout
    # if the program times out catch the exception and just print timeout
    except Exception as e:
        print(e)
        print("Program " + programName + " timed out.")
        return "timeout"
    

# Makes the numbers closer towards the extremes, to test edge cases 
def pushTowardExtremes(num, minValue, maxValue):
    x = (num-minValue)/(maxValue-minValue) # Get percentage of how far the number is from the min and max
    intensity = 10 # How much it should be pushed towards the extremes (set close to 0 BUT NOT 0 for linear distribution)
    offset = ((math.atan(2*intensity*x-intensity)*math.pi)/(math.pi*math.atan(intensity))+1)/2 # Function from image
    newNum = offset*(maxValue-minValue)+minValue # Apply the offset to the number
    return int(newNum)

def generateRandom(min, max):
    return pushTowardExtremes(random.randint(min, max), min, max)

outputCounter = 0

def testProgram(userProgramName):
    global outputCounter
    # Generate input file # Currently hardcoded for DN2
    N = generateRandom(1, 100000)
    K = generateRandom(2, 10)
    A = generateRandom(1, 20)
    with open('test.in', 'w') as f:
        f.write(str(N) + " " + str(K) + " " + str(A) + "\n")
        for i in range(N):
            f.write(str(generateRandom(0, 1000000000)) + "\n")
    
    #### Generate output file by running the working programs with the generated input file
    workingProgramNames = os.listdir("./workingPrograms")
    
    # Get outputs of all the working programs
    prevOutput = ""
    for currWorkingProgram in workingProgramNames:
        output = runCPPProgram("./"+workingProgramsFolderName+"/"+currWorkingProgram)
        with open(workingOutputFolderName + "/" + currWorkingProgram + '.out', 'w') as f:
            f.write(output)
        if prevOutput != "" and prevOutput != output:
            print("Working programs disagree.")
        prevOutput = output
    
    # Get the output of the program to be tested
    userOutput = runCPPProgram("./"+userProgramName)
    with open(userOutputFolderName+"/" + userProgramName + '.out', 'w') as f:
        f.write(userOutput)
    
    # Compare the outputs of the working programs with the output of the program to be tested
    workingOutputs = os.listdir("./workingOutputs")
    outputsMatch = True
    for currWorkingOutput in workingOutputs:
        # Compare the outputs
        with open(workingOutputFolderName + "/" + currWorkingOutput, 'r') as f:
            workingOutput = f.read()
            if workingOutput!=userOutput :
                outputsMatch = False
                break
    
    passedOrNotFolderName = "/passed/"
    if outputsMatch:
        print(str(outputCounter) + ": " + "[+] Test passed.")
    else:
        print(str(outputCounter) + ": " + "[-] Test failed.")
        passedOrNotFolderName = "/failed/"
    
    os.makedirs(allOutputsFolderName + passedOrNotFolderName+ str(outputCounter) + "/" + "working")
    os.makedirs(allOutputsFolderName + passedOrNotFolderName+ str(outputCounter) + "/" + "user")
    for currWorkingOutput in workingOutputs:
        # Compare the outputs
        with open(allOutputsFolderName + passedOrNotFolderName + str(outputCounter) + "/" + "working" + "/" + currWorkingOutput, 'w') as fileToPrintTo:
            with open(workingOutputFolderName + "/" + currWorkingOutput, 'r') as originalFile:
                textToWrite = originalFile.read()
                fileToPrintTo.write(textToWrite)
    
    with open(allOutputsFolderName + passedOrNotFolderName + str(outputCounter) + "/" + "user" + "/" + userProgramName + ".out", 'w') as fileToPrintTo:
        fileToPrintTo.write(userOutput)
    
    outputCounter += 1

def setup():
    # Check if the user has provided any parameters
    if len(sys.argv) <= 1 or len(sys.argv) > 2:
        print("Incorrect number of paramters. Check README.md for more details.\n")
        exit(1)

    # Get the name of the program to be tested, aka. the first provided argument
    firstArg = sys.argv[1]

    program = firstArg 
    programName = program.split(".")[0]

    # Command to compile the C++ program 
    compileArr = ["g++ -std=c++20 -o", programName, program]
    compileCmd = " ".join(str(x) for x in compileArr)
    # Compile the C++ program 
    compileProcess = subprocess.run(compileCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # Check if everything compiled successfully, else exit
    if compileProcess.returncode == 0: 
        print("Compilation successful.") 
    else:
        print("Compilation failed.")
        exit(1)

    # Read settings file
    f = open("settings", "r")

    # Get the name of the folder with the worknig programs
    line1 = f.readline()
    line1 = line1.split(" ")
    workingProgramFolder = line1[-1]
    if len(workingProgramFolder)<1: # I don't think this actually works
        print("Incorrect working file specified in settings file.")
        exit(1)

    # Skip the next two lines
    f.readline()
    f.readline()

    # Get the input settings: // For now everything will be hardcoded
    """ inputNames = []
    currLine = f.readline()
    while currLine != "":
        currLine = f.readline()
        splitLine = currLine.split(" ") """
        
    # Clear previous outputs
    if os.path.exists(workingOutputFolderName):
        os.system("rm -rf " + workingOutputFolderName)
        os.makedirs(workingOutputFolderName)
    if os.path.exists(userOutputFolderName):
        os.system("rm -rf " + userOutputFolderName)
        os.makedirs(userOutputFolderName)
    if os.path.exists(allOutputsFolderName):
        os.system("rm -rf " + allOutputsFolderName)
        os.makedirs(allOutputsFolderName)
        os.makedirs(allOutputsFolderName + "/passed")
        os.makedirs(allOutputsFolderName + "/failed")
    
    # Infinite loop for infinite test
    print("Starting test program.")
    while True:
        testProgram(programName);
        
        
setup()