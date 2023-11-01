import subprocess
import os
import sys
import time
import inputGeneration
import shutil
import platform

workingOutputFolderName = "workingOutputs"
userOutputFolderName = "userOutput"

workingProgramsFolderName = "workingPrograms"

allOutputsFolderName = "allOutputs"

timeoutLimit = 2 # in seconds

operatingSystem = platform.system()

slash = "/"

def runCPPProgram(programName, inputTxt):
    # Command to run the C++ program and get its output 
    # runArguments = [programName]
    # runCommand = "".join(str(x) for x in runArguments)
    # Run the C++ program 
    try:
        runProcess = subprocess.run([programName],input=inputTxt, capture_output=True, timeout=timeoutLimit, text=True, shell=True)
        return runProcess.stdout
    # if the program times out catch the exception and just print timeout
    except subprocess.CalledProcessError as e:
        exit_code = e.returncode
        stderror = e.stderr
        print(exit_code, stderror)
        exit(1)
    except Exception as e:
        print(e)
        print("Program " + programName + " timed out.")
        return "timeout"

def giveExecutePermission(path):
    # Give execute permission to the program
    os.system("chmod +x " + path)
    

outputCounter = 0

def testProgram(userProgramName):
    global outputCounter
    # Generate input file # Currently hardcoded for DN2
    ############################################################# CHANGE THIS ###################################################################
    inputGeneration.mediane()


    # This is dumb but im not fixing it rn. Reads the generated input from the created file
    inputTxt = "";
    with open('test.in', 'r') as f:
        inputTxt = f.read()
    
    #### Generate output file by running the working programs with the generated input file
    workingProgramNames = os.listdir("." + slash + workingProgramsFolderName)
    
    
    # Get outputs of all the working programs
    prevOutput = ""
    for currWorkingProgram in workingProgramNames:
        path = workingProgramsFolderName + slash + currWorkingProgram
        output = runCPPProgram(path, inputTxt)
        with open(workingOutputFolderName + slash + currWorkingProgram + '.out', 'w') as f:
            f.write(output)
        if prevOutput != "" and prevOutput != output:
            print("Working programs disagree.")
        prevOutput = output
    
    # Simplest way to check if everything is working
    if prevOutput == "":
        print("Working programs failed to generate output. This could be due to an error in the program or due to no working programs for this operating system in the workingPrograms folder.")
        exit(1)
    
    # Get the output of the program to be tested
    t1 = time.time()
    userOutput = runCPPProgram("." + slash + userProgramName, inputTxt)
    with open(userOutputFolderName+slash + "" + userProgramName + '.out', 'w') as f:
        f.write(userOutput)
    t2 = time.time()
    
    # Compare the outputs of the working programs with the output of the program to be tested
    workingOutputs = os.listdir("." + slash + "workingOutputs")
    outputsMatch = True
    for currWorkingOutput in workingOutputs:
        # Compare the outputs
        with open(workingOutputFolderName + slash + currWorkingOutput, 'r') as f:
            workingOutput = f.read()
            if workingOutput!=userOutput :
                outputsMatch = False
                break
    
    # Ignore everything past this point, i gave up
    passedOrNotFolderName = slash + "passed" + slash
    if outputsMatch:
        print(str(outputCounter) + ": " + "[\033[32m+\033[0m] Test passed.", end="")
    else:
        print(str(outputCounter) + ": " + "[\033[31m-\033[0m] Test failed.", end="")
        passedOrNotFolderName = slash + "failed" + slash

    print(" - Time taken: " + str(t2-t1) + " seconds.")

    
    os.makedirs(allOutputsFolderName + passedOrNotFolderName+ str(outputCounter) + slash + "working")
    if not outputsMatch:
        os.makedirs(allOutputsFolderName + passedOrNotFolderName+ str(outputCounter) + slash + "user")
    for currWorkingOutput in workingOutputs:
        # Compare the outputs
        with open(allOutputsFolderName + passedOrNotFolderName + str(outputCounter) + slash + "working" + slash + currWorkingOutput, 'w') as fileToPrintTo:
            with open(workingOutputFolderName + slash + currWorkingOutput, 'r') as originalFile:
                textToWrite = originalFile.read()
                fileToPrintTo.write(textToWrite)
    
    if not outputsMatch:
        with open(allOutputsFolderName + passedOrNotFolderName + str(outputCounter) + slash + "user" + slash + userProgramName + ".out", 'w') as fileToPrintTo:
            fileToPrintTo.write(userOutput)
        
    with open('test.in', 'r') as originalInputFile:
        with open(allOutputsFolderName + passedOrNotFolderName + str(outputCounter) + slash + "test.in", 'w') as fileToPrintTo:
            textToWrite = originalInputFile.read()
            fileToPrintTo.write(textToWrite)
        
    outputCounter += 1

def setup():
    global workingProgramsFolderName
    global slash
    
    
    # Check if the user has provided any parameters
    if len(sys.argv) <= 1 or len(sys.argv) > 2:
        print("Incorrect number of paramters. Check README.md for more details.\n")
        exit(1)
        
    # Check which operating system the user is running
    if not operatingSystem == "Linux" and not operatingSystem == "Windows":
        print("Unsupported operating system. Run this program on linux or windows.\n")
        exit(1)
    
    if operatingSystem == "Windows":
        slash = "\\"
        
    # Get the correct folder name for the working programs
    if operatingSystem == "Linux":
        workingProgramsFolderName += slash + "linux"
    elif operatingSystem == "Windows":
        workingProgramsFolderName += slash + "windows"
    else:
        print("Unsupported operating system. Run this program on linux or windows.\n")
        exit(1)
    

    # Get the name of the program to be tested, aka. the first provided argument
    firstArg = sys.argv[1]

    program = firstArg 
    programName = program.split(".")[0]
    programName+=".userCompiled"

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

    # Get the input settings: //  For now everything will be hardcoded
    """ inputNames = []
    currLine = f.readline()
    while currLine != "":
        currLine = f.readline()
        splitLine = currLine.split(" ") """
        
    # Clear previous outputs
    if os.path.exists(workingOutputFolderName):
        shutil.rmtree(workingOutputFolderName)
    os.makedirs(workingOutputFolderName)
    if os.path.exists(userOutputFolderName):
        shutil.rmtree(userOutputFolderName)
    os.makedirs(userOutputFolderName)
    if os.path.exists(allOutputsFolderName):
        shutil.rmtree(allOutputsFolderName)
    os.makedirs(allOutputsFolderName)
    os.makedirs(allOutputsFolderName + slash + "passed")
    os.makedirs(allOutputsFolderName + slash + "failed")
    
    workingProgramNames = os.listdir("." + slash + workingProgramsFolderName)
    # Give execute permission to the working programs
    if (operatingSystem == "Linux"):
        for currWorkingProgram in workingProgramNames:
            # In some cases the programs might not have execute permission, so do that first
            path = "." + slash + workingProgramsFolderName + slash + currWorkingProgram
            giveExecutePermission(path)
        print("Gave all working programs execute permissions")
        
    
    # Infinite loop for infinite test
    print("Starting test program.")
    while True:
        testProgram(programName);
        
        
setup()