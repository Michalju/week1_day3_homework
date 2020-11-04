# The purpose of this function is to return value 10
def return_10():
        return 10

# The purpose of this function is to return result of var_1 + var_2
def add(var_1, var_2):
    return var_1 + var_2

# The purpose of the function is to return result of var_1 - var_2
def subtract(var_1, var_2):
    return var_1 - var_2

# The purpose of the function is to return result of var_1 * var_2
def multiply(var_1, var_2):
    return var_1 * var_2

# The purpose of the function is to return result of var_1 / var_2
def divide(var_1, var_2):
    return var_1 / var_2

# The purpose of the function is to return length of the string
def length_of_string(input_string):
    return len(input_string)


# The purpose of the function is to join two strings
def join_string( string_1, string_2 ):
    return string_1 + string_2

# The purpose of the function is to add two converted into number string
def add_string_as_number( string_1, string_2 ):
    return int(string_1) + int(string_2)

# The purpose of the function is to convert a number into month full name
def number_to_full_month_name( input ):
    import datetime
    datetime_object = datetime.datetime.strptime(str(input), "%m")
    return datetime_object.strftime("%B")

# The purpose of the function is to convert a number into month abbreviated name
def number_to_short_month_name( input ):
    import datetime
    datetime_object = datetime.datetime.strptime(str(input), "%m")
    return datetime_object.strftime("%b")

# The purpose of the function is to return cube volume for a given side length
def volume_of_cube(side_length):
    return pow(side_length, 3)

# The purpose of the function is to return reversed input string
def reverse_string(input):
    return input [::-1]

# The purpose of the function is to convert farenheit to celsius
def fahrenheit_to_celsius(input):
    return (input - 32)*5/9
 