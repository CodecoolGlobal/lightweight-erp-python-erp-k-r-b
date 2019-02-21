""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    while True:
        options = ["Show table",
                   "Add",
                   "Remove",
                   "Update",
                   "Who is the oldest person?",
                   "Who is the closest to the average age?"]
        ui.print_menu("Human Resources", options, "Back to main menu")

        table = data_manager.get_table_from_file("hr/persons.csv")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        try:
            if option == "1":
                show_table(table)
                break
            elif option == "2":
                return add(table)
            elif option == "3":
                id_ = ui.get_inputs(["Please provide ID to remove: "], "")
                remove(table, id_)
                break
            elif option == "4":
                id_ = ui.get_inputs(["Please give me an ID to update: "], "")
                update(table, id_,)
            elif option == "5":
                get_oldest_person(table)
                break
            elif option == "6":
                get_persons_closest_to_average(table)
                break
            elif option == "0":
                break
        except KeyError as err:
            ui.print_error_message(str(err))


def show_table(table):
    table = data_manager.get_table_from_file(r"hr/persons.csv")
    title_list = ["id", "name", "birth_year"]
    ui.print_table(table, title_list)
    return start_module()


def add(table):
    list_labels = ["Name: ",
                   "Birth_year: "]
    new_id = common.generate_random()
    new_data = ui.get_inputs(list_labels, "")
    new_data.insert(0, new_id)
    table = common.add_line_to_file("hr/persons.csv", new_data)
    return table


def remove(table, id_):
    for i in range(len(table)):
        if table[i][0] == id_:
            del table[i]
            break
        data_manager.write_table_to_file("hr/persons.csv", table)
        return table


def update(table, id_):
    for sublist in table:
        if id_[0] in sublist:
            inputs = ui.get_inputs(["ID", "Name", "Birth Year"], "")
            for item in range(len(sublist)):
                sublist[item] = inputs[item]

    data_manager.write_table_to_file("hr/persons.csv", table)


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    # oldest = []
    # for i,value in enumerate(table):
    #    if value[2] >= value[2]:
    #        oldest.append(value[1])
    # print(min(oldest))
    date_dict = {}
    d = date_dict
    for line in table:
        date = int(line[2])
        date_dict[line[1]] = date
    sort_dict = sorted(d.items(), key=lambda x: (x[0], -x[1]))  # sorting by year the names
    enough = []
    for i, v in sort_dict:
        enough.append(i)
    # print(enough)
    ui.print_result(enough[:3], label="")


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    sum = 0                                     # REFACTOR ASAP
    to_closest = []
    for i, value in enumerate(table):
        to_closest.append(value[2])
    to_closest = list(map(int, to_closest))  # convert list to integers
    for num in to_closest:
        sum = sum + num
    average = sum / len(to_closest)             # get average
    closest = to_closest[0]
    for i in range(1, len(to_closest)):
        if abs(to_closest[i] - average) < abs(closest - average):  # calculate which year is the closest to the average
            closest = to_closest[i]
    closest = str(closest)                      # convert integers to string :'D
    for i, value in enumerate(table):
        if closest in value[2]:
            print(value[1])


def takeClosest(myList, myNumber):
    closest = myList[0]
    for i in range(1, len(myList)):
        if abs(myList[i] - myNumber) < abs(closest - myNumber):
            closest = myList[i]
    print(closest)
    # if round(average)  value[2]:      #if rounding is close to years in list
    #        print(value[1])               #print the name of the closest
