print("Guess Game")
User_name=input("your_name: ")
print("Hi, " +User_name)
print("you have 3 tries to Guess the word")
guess_word= "wall" 
user_word= " "
count= 0
limit= 3 
out_of_tries = False
while user_word!=guess_word and not out_of_tries:
    if count < limit :
        user_word=input("What runs around a house but doesn't move ?")
        count+=1
    else:
        out_of_tries = True
if out_of_tries:
    print("you lost out of tries")
else:
    print("YOU WIN")
