"""
total = 0
for number in range(1, 10 + 1):
    print(number)
    total = total + number
print(total)
"""
"""
def add_numbers():
    for number in range(1, 10 + 1):
        print (number)
        number=number+45
    return(number)
    #write the body of this
    #function, similar to the block
    #of code we just saw. Hint:
    #don’t forget to use return

answer = add_numbers()
print(answer)
"""




def add_numbers(start,end):
    total=0
    for number in range(start,end):
        print(number)
        total = total + number
    return(total)


test1 = add_numbers(1,2)
print(test1)
test2 = add_numbers(1, 100)
print(test2)
test3 = add_numbers(1000, 5000)
print(test3)

#"""
