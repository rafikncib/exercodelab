# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:25:30 2024

@author: Rafik Ncib
"""

def arithmetic_arranger(problems, show_answers=False):
    # Check if there are more than 5 problems; return an error if true
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Initialize variables for the arranged output lines
    first_line = ""
    second_line = ""
    third_line = ""
    answer_line = ""
    
    # Loop through each problem to process and format it
    for problem in problems:
        # Split the problem into operands and operator
        calc = problem.split(' ')
        first_operand, operator, second_operand = calc

        # Validate the operator; only '+' and '-' are allowed
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        # Ensure both operands are numeric
        if not (first_operand.isdigit() and second_operand.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        # Check if operands are within the 4-digit limit
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Determine the width of the problem by finding the length of the longer operand and adding 2
        longest_operand = max(len(first_operand), len(second_operand))
        width = longest_operand + 2  # Space for the operator and at least one space before operands
        diff = abs(len(first_operand) - len(second_operand))  # Difference in length of operands
        
        # Calculate the result of the arithmetic operation
        result = str(eval(problem))

        # Calculate padding for alignment
        # `padding_first` is the leading space for the first operand
        # `padding_second` is the space after the operator for the second operand
        padding_first = (diff + 2) if len(first_operand) < len(second_operand) else 2
        padding_second = (diff + 1) if len(first_operand) >= len(second_operand) else 1
        
        # Format the first line with proper spacing
        first_line += (' ' * padding_first) + first_operand
        # Format the second line with the operator and properly spaced second operand
        second_line += operator + (' ' * padding_second) + second_operand

        # Add spacing between problems
        first_line += ' ' * 4
        second_line += ' ' * 4
        # Format the third line with dashes
        third_line += '-' * width
        third_line += ' ' * 4
        # Format the answer line with the result, aligning it to the right
        answer_line += ' ' * (width - len(result)) + result
        answer_line += ' ' * 4
    
    # Remove extra trailing spaces at the end of each line
    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    third_line = third_line.rstrip()
    
    # Combine all lines into the final formatted output
    arranged_problems = first_line + '\n' + second_line + '\n' + third_line
    # If answers are to be displayed, add the answer line
    if show_answers:
        answer_line = answer_line.rstrip()
        arranged_problems += "\n" + answer_line
    
    return arranged_problems

# Example usage: Display arranged arithmetic problems with answers
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
