# In Python, both LBYL (Look Before You Leap) and EAFP (Easier to Ask for Forgiveness than Permission)
# styles of programming can be used.
# In **EAFP** style, the action and handle any exceptions that may occur
# directly perform. 
# In **LBYL** style, check a certain condition is met before performing an action. 
# Both styles have their own advantages and disadvantages, and which one to use depends on the situation. 
# In general, EAFP style is more concise and readable, while LBYL style can be more explicit and easier 
# to reason about in complex situations.


from math import inf


def division(number1: (str|float), number2: (str|float))-> float:
    """
    This function takes two numbers as input and return
    the result of dividing the first number by the second number
    """


    try:
        number1 = float(number1)
        number2 = float(number2)
        division_result = number1 / number2     
    except ZeroDivisionError:
        division_result = inf if number1 > 0 else -inf 
    except ValueError:
        print("ValueError: one or two number is invalid and not digit value")
        division_result = None
    except Exception as error:
        print("occure {error}")
    return division_result




def tese_division_function():
    """
    This function tests 
    the defined division function
    by receiving two input values
    number1 and number2
    """
    number1 = input("number1:")
    number2 = input("number2:")
    print(division(number1, number2))
    print(division(-1, 0))
    

if __name__ == '__main__':
    tese_division_function()
