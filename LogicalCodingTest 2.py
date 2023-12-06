def characterCount(string: str) -> None:
    '''
    This function is for counting the frequency of all appeared character in
    input string.
    
    e.g. input: "Hello welcome to Cathay 60th year anniversary"
         output: [('0', 1), ('6', 1), ('A', 5), ('C', 2), ... , ('Y', 3)]
    '''

    # Creare a dictionary storing the frequency of all appeared character
    freq = dict()
    
    # Remove all whitespace from string
    string = ''.join(string.split())
    
    # Transform all characters in string uppercase
    for c in string.upper():
        # Increase the value of freq[c] (the frequency of char c)
        freq[c] = freq.get(c, 0) + 1

    # Sort the dictionary with keys and print out the result
    res = sorted(freq.items(), key = lambda x: x[0])
    for char, frequency in res:
        print(char, frequency)


input1 = "Hello welcome to Cathay 60th year anniversary"
input2 = "aaAA aA"
input3 = " aaAA aA"
input4 = "aaAA aA "
input5 = "_@#$"
input6 = "1234567890"
input7 = ""

print("\nTestcase1: ", input1)
characterCount(input1)
print("\nTestcase2: ", input2)
characterCount(input2)
print("\nTestcase3: ", input3)
characterCount(input3)
print("\nTestcase4: ", input4)
characterCount(input4)
print("\nTestcase5: ", input5)
characterCount(input5)
print("\nTestcase6: ", input6)
characterCount(input6)
print("\nTestcase7: ", input7)
characterCount(input7)
