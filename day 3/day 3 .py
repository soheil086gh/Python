#print('welcome to rollercoaster!')
#hight = int(input('whats your hight in cm ? '))
#if hight >= 120:
   # print('you can ride the rollercoaster!')
#else:
# print('you are too short to ride the rollercoaster!')





#number=int(input('enter the number'))
#if number%2==0:
   # print('the number is even')
#else:
# print('the number is odd')



#print('welcome to rollercoaster!')
#hight = int(input('whats your hight in cm ? '))
#bill = 0
#if hight >= 120:
    #print('you can ride the rollercoaster!')
    #age = int(input('what is your age? '))
    #if age <= 12:
       #bill = 5
       #print('pay 5 dollars')
    #elif age <=18:
       #bill = 7
       #print('pay 7 dollars')
    #else:
       #bill = 12
       #print('pay 12 dollars')
       #wants_photo = input('do you want to have a photo ? type y for yes and n for no. ')
       #if wants_photo == 'y':
          #bill += 3
          #print(f"your final bill is ${bill}")
#else:
#print('you are too short to ride the rollercoaster!')









#print('welcome to python pizza deliveries! ')
#size = input('what size pizza do you want? S.M.L: ')
#peperoni = input('do you want peperoni on your pizza? Y or N ')
#cheese =  input('do you want extra cheese? Y or N ')
#bill = 0
#if size == 'S':
    #bill += 15
#elif size == 'm':
    #bill += 20
#elif size == 'L':
    #bill += 25
#else:
    #print('invalid size')

    #if peperoni == 'Y':
        #if size == 'S':
           # bill += 2
        #else:
           # bill += 3

            #if cheese == 'Y':
                #bill += 1
                #print(f"your final bill is ${bill}")
        







# for github
print("welcome to rollercoaster")

height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
   print("you can ride the rollercoaster")
   age = int(input("what is your age? "))
   if age <= 12:
      bill = 5
      print("child tickets are $5")
   elif age <= 18:
      bill = 7
      print("youth ticket are $7.")
   else:
      bill = 12
      print("adult ticket are $12.")

   wants_photo = input("do you want to have photo take? type 'y' for Yes and n for No.")
   if wants_photo == "y":
      bill += 3

   print(f"your final bill is ${bill}")
else:
   print("sorry you can'ride")      