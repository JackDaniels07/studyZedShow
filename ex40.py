class MyStuff(object):
    
    def __init__(self):
        self.tangerine = "Пусть бегут неуклюже..."
        
    def apple(self):
        print("Я - самое сладкое яблоко!")
        
thing = MyStuff()
thing.apple()
print(thing.tangerine)
        
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
happy_bday = Song(["не могу я тебе в день рождения", 
                   "Дорогие подарки подарит,",
                   "Но зато в эти ночи весенние"])

bulls_on_parade = Song(["Далеко-далеко на лугу пасется кто?",
                        "Пейте, дети, молоко, будете здоровы!"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()