# See if the instructions really transform string1 into string2
def pretvorba_morph(instructions, inputTxt, cost):
    instructions = instructions.strip()
    split_instructions = instructions.split(" ")
    inputTxt = inputTxt.strip()
    split_input = inputTxt.split("\n")
    
    split_input = [x.strip() for x in split_input]
    costs = split_input[0].split(" ")
    costs = [int(x) for x in costs]
    first = split_input[1]
    second = split_input[2]
    
    presumed_cost = 0
    try:
        presumed_cost = int(cost)
    except:
        return False
    
    new_string = []
    first_counter = 0
    second_counter = 0
    total_cost = 0
    characters = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    for instruction in split_instructions:
        instruction_length = len(instruction)
        if instruction_length < 1 or instruction_length > 3:
            return False
        
        # Keep same
        if instruction_length == 1:
            if instruction != first[first_counter]:
                return False
            new_string.append(first[first_counter])
            first_counter += 1
            second_counter += 1
            continue
        
        # Add or remove
        if instruction_length == 2:
            if instruction[0] == "+":
                if instruction[1] not in characters:
                    return False 
                new_string.append(instruction[1])
                total_cost += costs[0]
                second_counter += 1
                continue
            if instruction[0] == "-":
                if instruction[1] != first[first_counter]:
                    return False
                first_counter += 1
                total_cost += costs[1]
                continue
            # Incorrect instruction cause neither - or +
            return False
        
        # Swap
        if instruction[0] == instruction[2]:
            return False
        if instruction[0] != first[first_counter]:
            return False
        if instruction[2] not in characters:
            return False
        if instruction[2] != second[second_counter]:
            return False
        new_string.append(instruction[2])
        first_counter += 1
        second_counter += 1
        total_cost += costs[2]

    if first_counter != len(first) or second_counter != len(second):
        return False
    
    if total_cost != presumed_cost:
        return False
    
    new_string = "".join(new_string)
    if new_string != second:
        return False
    
    return True

# Try to generate original string from nonchanging, removing and first in swap instructions
def pretvorba_original(instructions, inputTxt):
    instructions = instructions.strip()
    split_instructions = instructions.split(" ")
    
    new_string = []
    
    for instruction in split_instructions:
        instruction_length = len(instruction)
        if instruction_length < 1 or instruction_length > 3:
            return False
        
        if instruction_length == 1:
            new_string.append(instruction)
            continue
        
        if instruction_length == 2:
            if instruction[0] == "+":
                continue
            if instruction[0] == "-":
                new_string.append(instruction[1])
                continue
            return False
        if instruction[0] == instruction[2]:
            return False
        new_string.append(instruction[0])
        
    new_string = "".join(new_string)
    
    inputTxt = inputTxt.strip()
    split_input = inputTxt.split("\n")
    split_input = [x.strip() for x in split_input]
    first = split_input[1]
    if new_string != first:
        return False
    return True
    

def check_pretvorba(userOutput, currWorkingOutputs, inputTxt):
    user_lines = userOutput.split("\n")
    
    correct = True
    
    if len(user_lines) != 2:
        correct = False
        return correct

    for workingOutput in currWorkingOutputs:
        working_lines = workingOutput.split("\n")
        if len(working_lines) != 2:
            print("A working program doesn't corrent number of outputLines.")
            correct = False
        if working_lines[0] != user_lines[0]:
            return False
        if not pretvorba_morph(working_lines[1], inputTxt, working_lines[0]):
            print("A working program doesn't corrently morph the string.")
            continue
        if not pretvorba_original(working_lines[1], inputTxt):
            print("A working programs instructions don't stay true to original string S.")
    
    if not pretvorba_morph(user_lines[1], inputTxt, user_lines[0]):
        correct = False
        return correct
    
    if not pretvorba_original(user_lines[1], inputTxt):
        correct = False
        return correct
    
    
    return correct