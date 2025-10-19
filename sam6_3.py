def count_digits(digit_string):
    if len(digit_string) < 15:
        return "Строка должна содержать минимум 15 символов"
    
    digit_count = {}
    for char in digit_string:
        digit = int(char)
        digit_count[digit] = digit_count.get(digit, 0) + 1
    
    frequent_three = sorted(digit_count.items(), key=lambda x: (-x[1], x[0]))[:3]
    
    result_dict = dict(sorted(frequent_three, key=lambda x: x[0]))
    
    print("Три самых частых числа:", result_dict)
    return result_dict

digits = "123456789012345678901234567890"
count_digits(digits)
