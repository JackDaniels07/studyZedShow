print("Давайте попрактикуемся!")
print('Вы должны знать об управляющих последовательностях с символом \\, которые:')
print('\n управляют переносом строк и \t отступами.')

poem = """
\tДля счастья 
мне совсем немного надо.
Хочу тебя \n я нежно обнимать.
Хочу всегда
я быть с тобою рядом
\n\t\t и никогда не отпускать!
"""

print("---------------------------------------")
print(poem)
print("---------------------------------------")


five = 10 - 2 + 3 - 6
print(f"Здесь должна быть пятерка: {five}")

def secret_formula(started):
    jelly_beans = started + 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000

beans, jars, crates = secret_formula(start_point)

#помните, что это еще один способ форматирования строки
print("начиная с: {}".format(start_point)) 
#так жеб как с строкой F
print(f"у нас {beans} бобов, {jars} банок и {crates} ящиков.")

start_point = start_point / 10 

print('мы также можем сделать это таким образом:')
formula = secret_formula(start_point) 
# простой способ применить список к форматированной строке
print("у нас есть{} бобов, {} банок и {} ящиков.".format(*formula))  