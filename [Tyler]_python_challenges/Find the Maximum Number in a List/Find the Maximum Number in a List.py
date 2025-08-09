from typing import List, Union

def find_max(numbers: List[Union[int, float]]) -> Union[int, float]:
    if not numbers:
        raise ValueError("The list is empty. Cannot determine the maximum value.")
    
    max_value = numbers[0]  # Start with the first element
    for num in numbers[1:]:  # Loop through the rest
        if num > max_value:
            max_value = num  # Update if current number is larger
    
    return max_value
