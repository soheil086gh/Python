
#subscripting
#print("hello"[0])

#string
#print("123" + "456")

#integer
#print(123 + 456)

# larg integers
#print(123_456_789)

#float
#print(123.456)

#boolean 
#print(True)
#print(False)

#print(int("123") + int("456"))

#name_of_the_user = input("What is your name? ")
#length_of_name = len(name_of_the_user)
#print("number of letters in your name: " + str(length_of_name))

#print("my age: " + str(12))
#print(123 + 456)
#print(7 - 3)
#print(3 * 2)
#print(5 / 3)
#print(5 // 3)
#print(2 ** 3)



#BMI calculator for github
print("hello welcome to BMI calculator")
hight = float(input("what is your hight? "))
weight = float(input("what is your weight? "))
bmi = weight / (hight ** 2)
print("your BMI is: " + str(bmi))




#Tip Calculator for Github
print("Welcome to the tip calculator")
total_bill = float(input('what was the total bil?'))
tip = int(input('how much tip would you like to give 10. 12. or 15?'))
split_bill = int(input('how many people to split the bill?'))
tip_as_percent = tip / 100
total_tip_amount = total_bill * tip_as_percent
bill = total_bill + total_tip_amount
bill_per_person = bill / split_bill
final_amount = round(bill_per_person , 2)
print(f'each person should pay: ${final_amount}')