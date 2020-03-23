cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90 
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_pasengers_per_car = passengers / cars_driven


print('в Наличии', cars, "автомобилей.") 
print('и только', drivers, "водителей вышли на работу.")
print('получается, что', cars_not_driven, "машин пустуют.")
print('мы можем перезти сегодня', carpool_capacity, "человек.")
print('сегодня нужно перевести', passengers, "человек.")
print('В каждой машине будет примерно', average_pasengers_per_car, "человека.")
