from cs50 import get_int
import math

# Ask user for input
answer = get_int("Number: ")

remainingNum = answer
underlinedNum = False
underlinedSum = 0
nonUnderlinedSum = 0
digitCount = 0

# Determine if number is syntactically valid
while remainingNum > 0:
    lastDigit = remainingNum % 10
    # Every other number
    if underlinedNum == False:
        nonUnderlinedSum += lastDigit
        underlinedNum = True
    else:
        remainingNum2 = lastDigit * 2
        while remainingNum2 > 0:
            lastDigit2 = remainingNum2 % 10
            underlinedSum += lastDigit2
            remainingNum2 = math.floor(remainingNum2 / 10)
        underlinedNum = False
    remainingNum = math.floor(remainingNum / 10)
    digitCount += 1
    
total = underlinedSum + nonUnderlinedSum

# Determine card type
if (total % 10) != 0:
    print("INVALID")
else:
    numString = str(answer)
    # Check Amex
    if digitCount == 15: 
        if numString.startswith('34') or numString.startswith('37'):
            print("AMEX")
        else:
            print("INVALID")
    elif digitCount == 16:
        # Check MC
        if numString.startswith('51') or numString.startswith('52') or numString.startswith('53') or numString.startswith('54') or numString.startswith('55'):
            print("MASTERCARD")
        # Check Visa
        elif numString.startswith('4'):
            print("VISA")
        else:
            print("INVALID")
    elif digitCount == 13:
        if numString.startswith('4'):
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")