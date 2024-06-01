def decorateFun(func):
    def sumOfSquare(x, y):
        return func(x**2, y**2)
    return sumOfSquare

def addTwoNumbers(a, b):
    c = a+b
    return c

obj=decorateFun(addTwoNumbers)
c=obj(4,5)
print("Addition of square of two numbers=", c)