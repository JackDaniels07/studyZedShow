from sys import argv
script, user_name = argv
promt = '>'

print(f"Привет, {user_name}, я - сценарий {script}.")
print("Я хочу задать тебе несколько вопросов.")
print(f"Я тебе нравлюсь, {user_name}?")
likes = input(promt)

print(f"где ты живешь, {user_name}?")
lives = input(promt)

print("На каком компьютере ты работаешь?")
computer = input(promt)

print(f"""
      Итак ты ответил {likes} на вопрос, нравлюсь ли я тебею
      Ты живешь {lives}. Не представляю где это.
      И у тебя есть компьютер {computer} Прекрасно!
      """)