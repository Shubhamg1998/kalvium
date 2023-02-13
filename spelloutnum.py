def spell_out_number(number):
    # Dictionary containing all the single digit numbers
    single_digit_numbers = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    # Dictionary containing all the two digit numbers
    two_digit_numbers = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }

    # If the number is a single digit
    if number < 10:
        return single_digit_numbers[number]

    # If the number is a two digit number
    elif number < 100:
        if number in two_digit_numbers:
            return two_digit_numbers[number]
        else:
            first_digit = number // 10 * 10
            second_digit = number % 10
            return two_digit_numbers[first_digit] + "-" + single_digit_numbers[second_digit]

    # If the number is a 3 or 4 digit number
    else:
        return "Number too large. Only up to 4 digit numbers allowed."
