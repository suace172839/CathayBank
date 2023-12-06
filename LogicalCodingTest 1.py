def gradeCorrector(grades: list[int]) -> list[int]:
    '''
    This function is for reversing the input numbers(academic grade).
    
    e.g. input: [35, 46, 57, 91, 29]
         output: [53, 64, 75, 19, 92]
    
    Since the reverse of 1 could be 10 or 100, I define this situation to be 10.
    '''

    res = []
    for grade in grades:
        if grade == 100:
            res.append(1)
        else:
            # Due to the range of remaining number is [0 - 99], just switch the 
            # tens digit and units digit of each input number
            res.append((grade % 10) * 10 + (grade // 10))
    
        '''
        # The code for input with range [0 - (100 or more)]
        realGrade = 0
        while grade > 0:
            realGrade = realGrade * 10 + grade % 10
            grade = grade // 10
        res.append(realGrade)
        '''
        
    return res
        

input1 = [35, 46, 57, 91, 29]
input2 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
input3 = [100, 10, 1]
input4 = []

print("\nTestcase1:", input1)
print(gradeCorrector(input1))
print("\nTestcase2:", input2)
print(gradeCorrector(input2))
print("\nTestcase3:", input3)
print(gradeCorrector(input3))
print("\nTestcase4:", input4)
print(gradeCorrector(input4))
