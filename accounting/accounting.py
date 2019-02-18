""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "Which year has the highest profit?",
               "What is the average (per item) profit in a given year?"]
    ui.print_menu("Stores", options, "Back to main menu")

    table = data_manager.get_table_from_file("accounting/items.csv")

    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]

    while True:
        try:
            if option == "1":
                show_table(table)
                break
            elif option == "2":
                return add(table)
            elif option == "3":
                id_ = ui.get_inputs(["Please provide ID to remove:   "], "")
                remove(table, id_)
                # show_table(table)
            elif option == "4":
                id_ = ui.get_inputs(["Please give me an ID to update:   "], "")
                update(table, id_,)
                # show_table(table)
            elif option == "5":
                which_year_max(table)
                break
            elif option == "6":
                year = ui.get_inputs(["Please give me a Year to calculate:  "], "")
                avg_amount(table, year)
            elif option == "0":
                break
        except KeyError as err:
            ui.print_error_message(str(err))


def show_table(table):
    table = data_manager.get_table_from_file("accounting/items.csv")
    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    ui.print_table(table, title_list)
    return start_module()


def add(table):
    list_labels = ["Month",
                   "Day",
                   "Year",
                   "Type",
                   "Amount"]
    new_id = common.generate_random()
    new_data = ui.get_inputs(list_labels, "")
    new_data.insert(0, new_id)
    table = common.add_line_to_file("accounting/items.csv", new_data)
    return table


def remove(table, id_):
    for i in range(len(table)):
        if table[i][0] == id_:
            del table[i]
            break
        data_manager.write_table_to_file("accounting/items.csv", table)
        return table

    return table


def update(table, id_):
    for sublist in table:
        if id_[0] in sublist:
            inputs = ui.get_inputs(["ID", "Month", "Day", "Year", "Type", "Amount"], "")
            for item in range(len(sublist)):
                sublist[item] = inputs[item]

    data_manager.write_table_to_file("accounting/items.csv", table)
    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    profits = []
    for i, value in enumerate(table):
        if "in" in value:
            profits.append(value)
    number = []
    for i, value in enumerate(profits):
        number.append(value[5])
    # print(number)
    number = list(map(int, number))
    max_profit = (max(number))
    max_profit = str(max_profit)
    for i, value in enumerate(table):
        if max_profit in value[5]:
            ui.print_result(value[3], label="")


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    year_s = []
    # for i, value in enumerate(table):
    #    if year[0] in value:
    #        print(value)
    for i, value in enumerate(table):
        if year[0] in value:
            year_s.append(value)
    profit = []
    items = []

    for i, value in enumerate(year_s):
        if "in" in value:
            profit.append(value[5])
        if "out" in value:
            items.append(value[5])
    # print(profit,items)
    profit = list(map(int, profit))
    items = list(map(int, items))
    halo = (sum(profit) / sum(items))
    print(halo * len(year_s))
    
