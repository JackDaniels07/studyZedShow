#for i in range(1, 101):
 #   print("Fizz"*(i % 3 == 0)+"Buzz"*(i % 5 == 0) or i)
 
def break_words(stuff):
    """ this func disacc text on word."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sort word"""
    return sorted(words)

def print_first_word(words):
    """output first word after pack"""
    word = words.pop(0)
    print(word)
    
def print_last_word(words):
    """output last word after pack"""
    word = words.pop(-1)
    print(word)
    
def sort_sentence(sentence):
    """Get sentence and return sort sentence"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """output first and last sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """sort words, and output first and last"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
        
