#fruits = ['apple' , 'peach' 'pear']

#for fruit in fruits:
   # print(fruit)
    #print(fruit + 'pie')

#print(fruits)





#student_scores = [150 , 145 , 180 , 177]

#max_score = 0

#for score in student_scores:
   # if score > max_score:
       # max_score = score

#print(max_score)        

#total = 0

#for number in range(1 , 101):
  #total += number
#print(total)


#for github
""" for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
   print(number)
 """
 
import random


letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("welcome to the PyPassword Generator")
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Easy_level
""" password = ""
for char in range(0, nr_letter):
  password += random.choice(letter)
  
for char in range(0, nr_symbols):
  password += random.choice(symbols)
  
for char in range(0, nr_numbers):
  password += random.choice(numbers)
  
print(password)    
 """
 
 #Hard_level
password_list = []
for char in range(0, nr_letter):
  password_list.append(random.choice(letter))
  
for char in range(0, nr_symbols):
  password_list.append(random.choice(symbols))
  
for char in range(0, nr_numbers):
  password_list.append(random.choice(numbers))

print(password_list)  
random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list:
  password += char
  
print(f"Your password is: {password}")     

 
   