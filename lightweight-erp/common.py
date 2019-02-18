""" Common module
implement commonly used functions here
"""

from random import randint


def generate_random():              #WE HAVE TO refactor it :D
    generated = ''
    random_str_seq = "0123456789"
    random_lower_seq = "abcdefghijklmnopqrstuvwxyz"
    random_upper_seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    random_special = "+-*/\<>#_-£"
    for i in range(2):
        generated += str(random_str_seq[randint(0, len(random_str_seq) - 1)])
        generated += str(random_special[randint(0, len(random_special) - 1)])
        generated += str(random_lower_seq[randint(0, len(random_lower_seq) - 1)])
        generated += str(random_upper_seq[randint(0, len(random_upper_seq) - 1)])
    
    return generated



def look_data(table,id_,):
    id_ = "" 
    table = data_manager.get_table_from_file(file_name)
    for index, item in enumerate(table):
        if item in table:
            print(item)

def add_line_to_file(file_name, line):
    with open(file_name, "a+") as file:
        file.write("\n" + ";".join(line))


def get_average(some_list):
    sum = 0
    some_list = list(map(int, some_list))   #convert list to integers  
    for num in some_list:
        sum = sum + num
    average = sum / len(some_list)
    