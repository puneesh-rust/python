#def add(a,b):
#    return a+b 

#print(add(4,5))

#agrs = takes multiple arguments 

def add(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum  # return AFTER the loop

print(add(2))  # outside the function

    

