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