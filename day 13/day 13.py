#bug fixer
""" year = int(input("what is your year of birthday?"))

if year > 1980 and year < 1994:
    print("millennial")
elif year >= 1994:
    print("you are a Gen z")     """
    
    
try:
    age = int(input("how old are you?"))
except ValueError:
    print(" you have to write numerical input please try again") 
    age = int(input("how old are you?"))
    
    
if age > 18:
    print(f"you can drive at age: {age}.")       