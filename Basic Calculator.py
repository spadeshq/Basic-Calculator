#Basic Calculator
print('Welcome to the basic calculator!')
print('You can use (+) (-) (/) or (*)')

#Ask user for number & float
x= float(input('Give me a number: '))
n= input('Give me an operator: ')
y= float(input('Give me the second number: '))
if n == "*":
    m = y * x
    print('The answer is: ', m)
elif n== "+":
    m = y+x
    print('The answer is: ', m)
elif n== "-":
    m=x-y
    print('The answer is: ', m)
elif n== "/":
    m =  (x/y)
    print('The answer is: ', m)
else:
    print('Invalid Response')

