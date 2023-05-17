def return_10():
    return 10

def add(x, y):
    return x + y   

def subtract(x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    return x / y

def length_of_string(string):
    return len(string)

def join_string(x, y):
    return x + y

def add_string_as_number(x, y):
    return int(x) + int(y)

def number_to_full_month_name(x):
    months = {
        1 : "January",
        2 : "February",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "Decemeber"
    }
    return months [x]

def number_to_short_month_name(x):
    months = {
        1 : "Jan",
        2 : "Feb",
        3 : "Mar",
        4 : "Apr",
        5 : "May",
        6 : "Jun",
        7 : "Jul",
        8 : "Aug",
        9 : "Sep",
        10 : "Oct",
        11 : "Nov",
        12 : "Dec"
    }
    return months [x]

def volume_of_cube(x):
    result = x**3
    return result 

def reverse_string(string):
    reverse = string[::-1]
    return reverse

def fahrenheit_to_celsius(x):
    temp_conversion = (x - 32)*(5/9)
    return int(temp_conversion)