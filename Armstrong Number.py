def ArmstrongNumber(num):
    num_str=str(num)
    num_len=len(num_str)

    sum_of_cubes=0

    for digit in num_str:
        digit=int(digit)
        sum_of_cubes+=digit**num_len
        
    if sum_of_cubes==num:
        return True
    else:
        return False
    
number=int(input("Enter a number: "))
if ArmstrongNumber(number):
    print(number," is an armstrong number.")
else:
    
    print(number," is not an armstrong number.")