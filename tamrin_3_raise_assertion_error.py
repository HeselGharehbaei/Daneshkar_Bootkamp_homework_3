
#Error of the given code in section3 of HW_3 is SyntaxWarning: assertion is always true, perhaps remove parentheses? assert '(' 
# So by removing the parentheses after 'assert' this error be resolved and an AssertionError be raised 
# But the assert statement is not a reliable way to validate data because it can be disabled in Python.
# If we run the corrected file in the terminal using "python3 -O tamrin_3_raise_assertion_error.py", the assert command will be disabled and this code will run without any errors.
# So finally the code can be modified as follows: 


def apply_discount(price: int, discount: float = 0.0) -> int:
    """
    Apply Discount Percent and Calculate Final Price
    """

    if price < 0 or discount < 0 or discount > 1:
        raise ValueError("Invalid input values. Price and discount must be positive numbers; discount must be between 0 and 1.")        
    final_price = int(price * (1 - discount))
    

    return final_price


def test_apply_discount_function():
    """
    This function tests 
    the defined apply_discount function
    by two input values
    price and discount
    """

    print(apply_discount(-100, 0.6))


if __name__ == '__main__':
    test_apply_discount_function()    