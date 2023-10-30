# Temp ReadME

This program works based on differential fuzzing.
In the workingPrograms folder there needs to be at least one (there can be more) compiled program for which you are decently certain gives the correct solution. (There is no required naming scheme for the working programs)
To use this program just place your .cpp file into this folder.
After that run the program with the following command:
python3 tester.py *name of your program*.cpp

The program will always be made with the latest homework in mind. Check "Side-notes" if you wish to see how to test older homeworks.

### Side-notes

Everything is hardcoded.
If you wish to change which HW yo uare currently testing, place the appropriate compiled program from the "otherPrograms" folder into the "workingPrograms" folder, or use your own if yo uso wish.
After that change the inputgenerator in "tester.py". You will find what you have to change under a "CHANGE THIS" comment.
To see all input options check the "inputGeneration.py" file.


# Ignore from this point onward
# APS Tester

This program will generate an infinite amount of randomized outputs (with preference for low and high extremes). It will feed these inputs into multiple verified working programs and into your program, then compare the results to determine whether your solution is valid.

There is no user input, everything is handled through the file "settings".

# Setup

In the "settings" file, input the name of the compiled working program.
Input the structure of the input and the bounds.
An example is already written in "settings".

To run, use:
APStester.py *your program name*.cpp