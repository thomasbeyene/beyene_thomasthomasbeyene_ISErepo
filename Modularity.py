def convertString(inString, upper_lower):  # 1
    #convert string to lower or upper
    outString = ''

    if upper_lower == 'U' or upper_lower == 'u':
        outString = inString.upper()
    else:
        outString = inString.lower()

    return outString

def convertStringOption():  # 1
    convert_type = str(input("Do you want to convert the string to (U)pper or (L)ower case: ")).upper()

    if convert_type == 'U' or convert_type == 'L':
        inString = str(input("Enter string you want to convert: "))
        outString = convertString(inString, convert_type)
        print(outString)
    else:
        print("String cannot be converted")


