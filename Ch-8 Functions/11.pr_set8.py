# write a python function to print multiplication table of a given number


# define the function with formal parameter num 

def print_table(num): 
    """ This function prints multiplication table of a given number"""
    for i in range(1,11): 
        print(num,' x ', i, ' = ',num*i) 
# end of function table


# input a number
n = int(input("Please Enter a number to print its multiplication table:"))

# call the function tanle by passing actual parameter 'n' 

print_table(n)