#############################################
# Filename: MyFirstProgram                  #
# Purpose: A simple demonstration of        #
# python program structure.                 #
#############################################


def main():
    '''
    This is our main function. It 
    controls the flow of execution of the 
    program.
    '''
    #Print something out.
    print ('Printing from main, Hellow World!!!')
    
    #Calls the first function
    first_function()
    
    #Call the second function
    second_function(greet='ola World !!!')

#Define first_function
def first_function():
    '''
    First function
    '''
    
    print ('I am first function')
    
#Define second function
def second_function(greet):
    '''
    Second function
    '''
    print ('I am second function ',greet)
    

#Execution Starts Here
if __name__ == '__main__':
    main()
