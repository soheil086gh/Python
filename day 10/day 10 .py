#def format_name(f_name, l_name):
    #formated_f_name = f_name.title()
    #formated_l_name = l_name.title()
    #return f"{formated_f_name} {formated_l_name}"


#print(format_name(f_name="soheil",l_name="alizadeh"))


#def function_1(text):
    #return text + text



#def function_2(text):
    #return text.title()

#output = function_2(function_1("hello"))
#print(output)


#def format_name(f_name, l_name):
    #if f_name == "" or l_name == "":
        #return "you did not provide valid inputs"
    #formated_f_name = f_name.title()
    #formated_l_name = l_name.title()
    #return f"{formated_f_name} {formated_l_name}"


#print(format_name(input("what is your name"),input("what is your last name?")))



# for github
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}



def calculator():
    should_continue = True
    first_num = float(input("Type the first number: "))


    while should_continue:
        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        second_num = float(input("Type the second number: "))
        answer = operation[operation_symbol](first_num, second_num)
        print(f"{first_num} {operation_symbol} {second_num} = {answer}")
        choice = input(f"type 'y' to continue calculating with {answer} , or type 'n' to start new calculating")
        if choice == "y":
            first_num = answer
        else:
            should_continue = False
            print("\n"*20)
         
calculator()            


    





    