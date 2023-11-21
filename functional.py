STARTING_NUMBERS=['4','5','37','6']
digits=[]

################

card= card_number(number)

def is_valid(number):
    if number[0] not in starting_numbers:
        return False
    elif not len(number) >= 13 and not len(number) <- 16:
        return False
    else:
        sum = double_even_digit(number) + sum_odd_digit(number)
        if (sum % 10) ==0:
            return True
        else:
            return False
 
 def sum_double_even(number):
    sum = 0
    for q in reversed(range(len(number))):
        if q % 2 ==0:
            digit = int(number[q]) * 2
            digits.append(int(get_digit(digit)))
    for q in range(len(number)):
        sum+=int(number[q])
    return sum

def sum_odd(number):
    sum = 0
    for q in reversed(range(len(number))):
        if q % 2!=0:
            sum += in(number[q])
    return sum

def get_digit(number):
    if int((len(str(number)))) == 2:
        return int(int(number[0])+(int(number[1])))



if is_valid(number):
    print('card is valid')
else:
    print("card is invalid")