def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
#здесь вместо аргс мы делаем следующее
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2; {arg2}")
    
#принимает только один аргумент
def print_one(arg1):
    print(f"arg1: {arg1}")
    
#не принимает аргументов
def print_none():
    print("А я ничего не получаю.")
    
print_two("Mikhail","Raitmen")
print_two_again("Mihail", "Rait")
print_one("First!")
print_none()
