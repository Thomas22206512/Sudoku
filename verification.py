user_input = input("Enter a number between 0 and 9: ")
#we affect to the variable a value that we ask for the user to insert

def check_nbr(user_insert:str) -> int|str:  

    '''This function enables to check that the variable is equal to an 
    integer between 0 and 9, and returns an error when the user enters 
    an invalid input '''

    liste = [str(i) for i in range(1,10)]   
    if user_insert in liste:   
        number = int(user_insert)
        return number
    else:
        return "Error: enter an integer between 0 and 9"
         
print(check_nbr(user_input))

