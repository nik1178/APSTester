# How to run
Place your cpp file into the APSTester folder, then use the command:
```python3 tester.py *name of your program*.cpp```

For more options:
```python3 tester.py -h```

All the tests and program outputs are stored in:
```./allOutputs```

## Description
This program works based on differential fuzzing.
It generates a random (or sometimes non random) test which first feeds into one or more working programs for each assignment.
After, the same input is fed into your program, and the results are compared.
I do extensive testing to make sure my programs are "working", but there is never a guarantee that I did not make a mistake.

## How to make your own tests with this program
In the workingPrograms folder there needs to be at least one (there can be more) compiled program for which you are decently certain gives the correct solution.
I will be updating this repository to have my version of the program included.

The program will always be updated to test the latest assignment given. This can be changed with the ```-a``` argument.