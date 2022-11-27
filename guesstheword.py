#hangman problem 
# word guessing game
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
-------------''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
-------------''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
-------------''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
--------------''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
--------------''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
--------------''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
--------------''']
print("'Welcome to Word guessing game!") 
print('''    
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
--------------''')
print( '"What is the most important part of DSA?(9 letter word)"' )
word="algorithm" 
nos_of_chances=len(word)
x=len(word)
word1="_________" 
list1=list(word1) 

def wordsearch(a): 
    hang=0
    count=0
    for i in range(0,x):
        if(a==word[i]):
            list1[i]=a 
            
            print("Good job!\n")  
            break
        else:
            count+=1 
          
    
    if(count==x):
        hang=1
        print("Oops!")
    print(list1) 
    return hang


    
nos_of_chances=0 
y=0
while(nos_of_chances<len(word)):
    a=input("Guess the letter of the word!\n") 
    
    b=wordsearch(a) 
    nos_of_chances+=1 
    print(f"{x-nos_of_chances} chances left!")
    
    if(b==1): 
        y+=1
        print(HANGMANPICS[y])   
        
    else: 
        print(HANGMANPICS[y])
    if(y==6):
        break


def res(): 
    count=0
    for i in range(0,x):
        if(word[i]==list1[i]):
            count=x-1

if(res()==x-1):
    print("You did it!\n") 
else:
    print("Try next time!\n") 
