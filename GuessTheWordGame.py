import random 
name = ['deafening', 'frequently', 'ancient', 'archaic', 'transparent', 'excruciating', 'ashen', 'flawless', 'destitute', 'compelling', 'beautiful', 'rapid', 'hushed', 'pouring', 'wealthy', 'sorrowfull', 'petrified', 'chilling', 'grave', 'keen', 'gleaming', 'brief', 'timid', 'basic', 'spider', 'wide', 'ride', 'pride', 'mawire', 'tiana']

def guess():
  word = random.choice(name)
  count= len(word)
  lives= len(word)
  print(str(count) + '  Letters in the word')
  print(str(count) + ' AttemptS in ThiS GamE, GooD LucK')
  while lives>0:
    lives-=1
    

    
    print()
    turn1=input('Enter a letter you think is in the word then press Enter!......?')
    if turn1 in word:
      print()
      print('correct')
      print('Positiont  ' + str(word.index(turn1)+1))
      print('Next letter?')
      print()

    if turn1 not in word:
      
      print()
      print('WRONG!!, that letter is not in the word')
      print('Try again!') 
      print(str(lives) + '  Lives left')

    if lives == 0:
      print("The word is", word)

        
      
      
  
  
guess()  
  
  
  
    
    



