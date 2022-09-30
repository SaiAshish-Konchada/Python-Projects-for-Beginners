romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    # specify more numerals if you wish
}

def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if romans[left] < romans[right]:
            sum -= romans[left]
        else:
            sum += romans[left]
    sum += romans[romanNumeral[-1]]
    return sum

print(RomanNumeralToDecimal("XXV"))