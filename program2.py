def romanToInt(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for char in s:
        value = roman_dict[char]
        # If the current value is greater than the previous value,
        # it means subtraction is needed.
        if value > prev_value:
            result += value - 2 * prev_value  # Subtract twice the previous value
        else:
            result += value
        prev_value = value
    
    return result

# Test cases
print(romanToInt("III"))      # Output: 3
print(romanToInt("LVIII"))    # Output: 58
print(romanToInt("MCMXCIV"))  # Output: 1994
