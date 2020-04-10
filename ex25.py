#for i in range(1, 101):
 #   print("Fizz"*(i % 3 == 0)+"Buzz"*(i % 5 == 0) or i)
 
def break_words(stuff):
    """ this func disacc text on word."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sort word"""