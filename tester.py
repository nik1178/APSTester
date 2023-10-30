import subprocess
import os
import sys
import time
import inputGeneration as ig

workingOutputFolderName = "workingOutputs"
userOutputFolderName = "userOutput"

workingProgramsFolderName = "workingPrograms"

allOutputsFolderName = "allOutputs"

def runCPPProgram(programName):
    # Command to run the C++ program and get its output 
    runArguments = ["time ",programName," < test.in"]
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
    


outputCounter = 0

def testProgram(userProgramName):
    global outputCounter
    # Generate input file # Currently hardcoded for DN2
    ############################################################# CHANGE THIS ###################################################################
    ig.Kzlitje()
    
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
    t1 = time.time()
    userOutput = runCPPProgram("./"+userProgramName)
    with open(userOutputFolderName+"/" + userProgramName + '.out', 'w') as f:
        f.write(userOutput)
    t2 = time.time()
    
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
    
    # Ignore everything past this point, i gave up
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
        
    with open('test.in', 'r') as originalInputFile:
        with open(allOutputsFolderName + passedOrNotFolderName + str(outputCounter) + "/test.in", 'w') as fileToPrintTo:
            textToWrite = originalInputFile.read()
            fileToPrintTo.write(textToWrite)
        
    print("Time taken: " + str(t2-t1) + " seconds.")
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