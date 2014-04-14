FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    output = []

    units = number%10
    number /= 10

    tens = number % 10
    number /= 10

    hundrends = number % 10

    if hundrends != 0:
        if tens == 1:
            return FIRST_TEN[hundrends] + " " + HUNDRED + " " + SECOND_TEN[units ]
        elif tens == 0 and FIRST_TEN[units] != "zero":
            return FIRST_TEN[hundrends] + " " + HUNDRED + " " + FIRST_TEN[units]
        elif tens == 0 and FIRST_TEN[units] == "zero":
            return FIRST_TEN[hundrends] + " " + HUNDRED 
        elif tens != 1 and tens != 0 and FIRST_TEN[units] != "zero":
            return FIRST_TEN[hundrends] + " " + HUNDRED + " " + OTHER_TENS[tens-2] + " " + FIRST_TEN[units]
        else:
            return FIRST_TEN[hundrends] + " " + HUNDRED + " " + OTHER_TENS[tens-2] 
    elif hundrends == 0:
        if tens != 1 and tens != 0:
            if FIRST_TEN[units] == "zero":
                return OTHER_TENS[tens-2] 
            else:
                return OTHER_TENS[tens-2] + " " + FIRST_TEN[units]
        elif tens == 0:
            return FIRST_TEN[units]
        else:
            return SECOND_TEN[units]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio(100)
