import random
import my_module

#random_integer = random.randint(1, 10)
#print(random_integer)     # prints a random integer between 1 and 10.

#print(my_module)


#random_number_0_to_1 = random.random()
#print(random_number_0_to_1)     # prints a random floating point number between 0

#random_float = random.uniform(1, 10)
#print(random_float)   



#head_or_tails = random.randint(a=0, b=1)
#if head_or_tails == 1 :
    #print("Heads")
#else:
    #print("Tails")




    #state_of_iran = ["tehran", "rasht", "tabriz", "shiraz", "yazd"] 

    #state_of_iran[2] = "mashhad"

   # state_of_iran.extend(['tabriz'])

    #print(state_of_iran)



#friend = ['soheil' , 'mohamad' ,'ali']
#print(random.choice(friend))






#for github
ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [ROCK , PAPER , SCISSORS]


user_choice = int(input("what do you choose? type 0 for Rock 1 for paper 2 for scissors\n"))
if user_choice >= 0 and user_choice <= 2:
   print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("computer_choice:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("invalid input You lose!")

elif user_choice == 0 and computer_choice == 2:
 print("You win!")
elif computer_choice == 0 and user_choice == 2:
   print("You lose!")
elif computer_choice > user_choice:
   print("You lose!")
elif user_choice > computer_choice:
   print("You win!")
elif computer_choice == user_choice:
   print("It's a draw!")
