"""
Find Max Sum - Coding Challenge Solution
========================================

Problem: Given an array of strings containing letters and digits, 
find the largest sum of digits within any single string.

Each digit is treated as a separate 1-digit number.
Example: "h1n36mfl" has digits 1, 3, 6 with sum = 1 + 3 + 6 = 10
"""

def find_max_sum(strings):
    """
    Find the maximum sum of digits across all strings in the array.
    
    Args:
        strings (list): List of strings containing letters and digits
        
    Returns:
        int: The maximum sum of digits found in any string
    """
    # Keep track of the highest sum found so far
    max_sum = 0
    
    # Check each string in the array
    for string in strings:
        # Reset sum for current string
        current_sum = 0
        
        # Look at each character in the current string
        for character in string:
            # If the character is a digit (0-9)
            if character.isdigit():
                # Add its value to the current string's sum
                current_sum += int(character)
        
        # Update max_sum if current string has a higher sum
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum


def main():
    """
    Test the solution with the provided example and demonstrate results.
    """
    # Test case from the problem
    test_input = ["dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw"]
    
    print("=== Find Max Sum Solution ===")
    print(f"Input: {test_input}")
    print()
    
    # Show the breakdown for each string
    print("Breaking down each string:")
    for i, string in enumerate(test_input, 1):
        # Find all digits in the string
        digits_found = []
        string_sum = 0
        
        for char in string:
            if char.isdigit():
                digits_found.append(char)
                string_sum += int(char)
        
        print(f"{i}. '{string}' -> digits: {digits_found} -> sum: {string_sum}")
    
    print()
    
    # Calculate and display the final result
    result = find_max_sum(test_input)
    print(f"Maximum sum found: {result}")
    
    # Verify this matches expected output
    expected = 13
    if result == expected:
        print("✅ Correct! Solution matches expected output.")
    else:
        print(f"❌ Error: Expected {expected}, got {result}")


# Run the test when script is executed
if __name__ == "__main__":
    main()
