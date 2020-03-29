def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"У нас есть {cheese_count} сырков!")
    print(f"У нас есть {boxes_of_crackers} пачек чипсов!")
    print("Этого достаточно для вечеринки!")
    print("Погнали!\n")
    
print("мы можем непосредственно передать числа функции:")
cheese_and_crackers(20, 30)

print("ИЛИ, мы можем использовать переменные из нашего сценария:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("Мы даже можем выполнять вычисления внутри функций:")
cheese_and_crackers(10+5, 6+1)

print("И объеденить переменые с вычислениями:")
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 1000)