def add(a, b):
    print(f"sum {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"minus {a} - {b}")
    return a - b
    
def multiply(a, b):
    print(f"multy {a} * {b}")
    return a * b

def devide(a, b):
    print(f"dev {a} / {b}")
    return a / b

print("Lets get command with func!") 

age = add(30, 5) 
height = subtract(190, 4) 
weight = multiply(35,2) 
iq = devide(250, 2)

print(f" age: {age}, height: {height}, weight: {weight}, IQ: {iq}!")

print (" this is teaser!")

what = add(age, subtract(height, multiply(weight, devide(iq, 2))))

print("in result: ", what, "can you calculate manuall?")