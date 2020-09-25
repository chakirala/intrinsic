def check_if_number_exists(num1,num2):
    c = 0
    while(num1 != 0):
        if(num1%10 == num2):
            return True
            break
        else:
            num1 = num1//10
            c=c+1
    if(c == 8):
        return False
result = check_if_number_exists(41539418,0)
print(result)