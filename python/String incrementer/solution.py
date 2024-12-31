import re

def increment_string(strng):
    if not strng:  # If the input string is empty
        return "1"
    
    # Match the trailing number (if any)
    match = re.search(r'\d+$', strng)
    if not match:  # If no numeric suffix is found
        return strng + "1"
    
    # Extract the numeric part and the non-numeric prefix
    num_part = match.group()
    prefix = strng[:match.start()]
    
    # Increment the numeric part, preserving leading zeros
    incremented_num = str(int(num_part) + 1).zfill(len(num_part))
    
    # Combine the prefix and the incremented number
    return prefix + incremented_num
