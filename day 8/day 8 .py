#def greet():
    #print("Hello World")
    #print("hello world")
    #print("hello world")
 
#greet()


#def greet_with_name(name):
    #print(f"Hello {name}")
    #print(f"How you doing {name}")

#greet_with_name("soheil")    


#def life_in_weeks(age):
    #years_remaining = 90 - age
    #weeks_remaining = years_remaining * 52
    #print(f"You have {weeks_remaining} weeks left.")


#life_in_weeks(18)






#def greet_with(name, location):
    #print(f"Hello {name}")
    #print(f"what is it like in {location}")
    
#greet_with(location="london", name="soheil")    


#def calculate_love_score(name1 ,name2):
   # combined_names = name1 + name2
    #lower_names = combined_names
    #t = lower_names.count("t") 
   # r = lower_names.count("r")
    #u = lower_names.count("u")
    #e = lower_names.count("e")
    #first_digit = t + r + u + e
    #l = lower_names.count("l")
    #o = lower_names.count("o")
    #v = lower_names.count("v")
    #e = lower_names.count("e")
    #second_digit = l + o + v + e
    
    
    #score = int(str(first_digit) + str(second_digit))
    #print(score)
    
#calculate_love_score("Angela Yu", "Jack Bauer")



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

direction = input("type `encode` to encrypt , type `decode` to decrypt:\n").lower()
text = input("type your message:\n").lower()
shift = int(input("type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ''
    for letter in original_text:
        shift_position = alphabet.index(letter) + shift_amount
        shift_position %= len(alphabet)
        cipher_text += alphabet[shift_position]

    print(f"here is the encode result: {cipher_text}")





def decrypt(original_text, shift_amount):
    output_text = ''
    for letter in original_text:
        shift_position = alphabet.index(letter) + shift_amount
        shift_position %= len(alphabet)
        cipher_text += alphabet[shift_position]

    print(f"here is the decode result: {output_text}")

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ''
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1   
        shift_position = alphabet.index(letter) - shift_amount
        shift_position %= len(alphabet)
        cipher_text += alphabet[shift_position]

    print(f"here is the d result: {output_text}") 
            

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)