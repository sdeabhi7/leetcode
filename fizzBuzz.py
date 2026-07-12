#   author: sdeabhi



def fizzBuzz(n):
    value = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            value.append('FizzBuzz')
        elif i % 5 == 0:
            value.append('Buzz')
        elif i % 3 == 0:
            value.append('Fizz')
        else:
            value.append(str(i))
    return value

print(fizzBuzz(3))