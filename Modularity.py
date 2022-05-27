def convertString(INPUT, upper_lower):  # 1
    #convert string to lower or upper
    OUTPUT = ''

    if upper_lower == 'U' or upper_lower == 'u':
        OUTPUT = INPUT.upper()
    else:
        OUTPUT = INPUT.lower()

    return OUTPUT

def convertStringOption():  # 1
    convert_type = str(input("Do you want to convert the string to (U)pper or (L)ower case: ")).upper()

    if convert_type == 'U' or convert_type == 'L':
        INPUT = str(input("Enter string you want to convert: "))
        OUTPUT = convertString(INPUT, convert_type)
        print(OUTPUT)
    else:
        print("String cannot be converted")


def ContainsNumbericValue(INPUT):  # 2
   # check if input string contains ['0':'9']
    numeric = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in INPUT:
        if i in numeric:
            return True

    return False


def ContainsNumbericValueOption():  # 2
    INPUT = str(input("Enter string you want to check: "))

    if ContainsNumbericValue(INPUT):
        print("The string contains numeric value.")
    else:
        print("The string does not contain numeric value.")


def IsValidNumber(INPUT):  # 3
    #check if all digit in input string contain ['0':'9']
    numeric = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in INPUT:
        if i not in numeric:
            return False

    return True

def IsValidNumberOption():  # 3

    """
    check if string is valid number
    :return: None
    """
    INPUT = str(input("Enter string you want to check: "))

    if IsValidNumber(INPUT):
        print("The string is the value number.")
    else:
        print("The string is not the valid number.")


def RemoveNumeric(INPUT):  # 4
    #Remove any numeric values in a given string
    OUTPUT = ''
    numeric = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in INPUT:
        if i not in numeric:
            OUTPUT += i

    return OUTPUT


def RemoveNumericAndConvertOption():  # 4
    INPUT = str(input("Enter string you want to remove and convert: "))
    OUTPUT = RemoveNumeric(INPUT)

    convert_type = str(input("Do you want to convert the string to (U)pper or (L)ower case: ")).upper()

    if convert_type == 'U' or convert_type == 'L':
        OUTPUT = convertString(OUTPUT, convert_type)
        print(OUTPUT)
    else:
        print("String cannot be converted")



