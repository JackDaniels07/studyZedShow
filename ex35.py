from sys import exit 

def gold_room():
    print("Здесь полно золото. сколько кг ты хочешь унести?")
    
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("эй, надо ввести число")
        
    if how_much < 50:
        print ("Шикарно, ты не жадныйю поэтому выигрываешь.")
        exit(0)
    else:
        dead("Ах ты жадина")
        
def bear_room():
    print("Здесь сидит медведь.")
    print("У медведя бочка с медом.")
    print("Bear close the door.")
    print("How teleport Bear?")
    bear_moved = False
    
    while True:
        choice = input("> ")
        
        if choice == "Get med":
            dead("Bear watch to you and die you")
        elif choice == "joke bear" and not bear_moved:
            print("bear go away.")
            print("You can go in the door. go?")
            bear_moved = True
        elif choice == "Подразнить медведя" and bear_moved:
            dead("bear die you")
        elif choice == "gu" and bear_moved:
            gold_room()
        else:
            print("enter action")
            
def cthulhu_room():
    print("На тебя смотрит великий Ктулуху")
    print("Он смотрит на тебя, и ты начинаешь сходить с ума.")
    print("Убежать или начать сражаться?")
    
    choice = input("> ")
    
    if "убежать" in choice:
        start()
    elif "начать сражаться?" in choice:
        dead("Может и победишь")
    else:
        cthulhu_room()
        

def dead(why):
    print(why, "Великолепно")
    exit(0)
    
def start():
    print("ты в темной комнате.")
    print("Отсюда ведут две двери и налево и направо.")
    print("Куда ты повернешь?")
    
    choice = input("> ")
    
    if choice == "налево":
        bear_room()
    elif choice == "направо":
        cthulhu_room()
    else:
        dead("ТЫ ходишь из комнаты в комнату.")
        
        
start()    
    
            
            
        
