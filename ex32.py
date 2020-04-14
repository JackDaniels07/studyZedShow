the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pie', 'pineapple']
change = [1, 'halfpart', 2, 'fifty', 3, 'a_hundread']

#cycl 'for' first type assemble list
for number in the_count:
    print(f"Счетчик {number}")
    
#repeat
for fruit in fruits:
    print(f"Фрукт: {fruit}.")
    
#Также можно обрабатывать смешанные списки
# ОБратите внимание, что используются символы {}, так как неизвестен тип значения
for i in change:
    print(f'Я получил {i}')
    
#также мы можем создавать списки, начнем с пустого
elements = []

for i in range(0, 6):
    print(f"Добавление {i} в список")
    #append - функция добавления элементов в список
    elements.append(i)
    
#теперь мы их выводим
for i in elements:
    print(f'Номер элемента: {i}')
print(elements)