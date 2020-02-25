import read.md as f
def count_word(fn,):
    word_number=0
    for line in f:    
       word = line.split()
       word_number += len(word)
    return word_number
    
