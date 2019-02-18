""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

import main


def start_module():
    while True:
        options = ["Show table",
                   "Add",
                   "Remove",
                   "Update",
                   "What is the id of the customer with the longest name?",
                   "Which customers has subscribed to the newsletter?"]
        table = data_manager.get_table_from_file("crm/customers.csv")
        ui.print_menu("Customer relationship manager", options, "Back to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]

        try:
            if option == "1":
                return show_table(table)
            elif option == "2":
                return add(table)
            elif option == "3":
                id_ = ui.get_inputs(["Please provide ID of customer to remove: "], "")
                return remove(table, id_[0])
            elif option == "4":
                id_ = ui.get_inputs(["Please provide ID of customer to update: "], "")
                return update(table, id_[0])
            elif option == "5":
                get_longest_name_id(table)
                break
            elif option == "6":
                get_subscribed_emails(table)
                break
            elif option == "0":
                return
        except KeyError as err:
            ui.print_error_message(str(err))


def show_table(table):
    title_list = ["ID",
                  "Name",
                  "E-mail address",
                  "Subscription"]
    ui.print_table(table, title_list)
    return start_module()


def add(table):
    list_labels = ["Full name: ",
                   "E-mail address: ",
                   "Subscription (1/0): "]
    new_id = common.generate_random()
    new_data = ui.get_inputs(list_labels, "")
    new_data.insert(0, new_id)
    table = common.add_line_to_file("crm/customers.csv", new_data)
    return table


def remove(table, id_):
    for i in range(len(table)):
        if table[i][0] == id_:
            del table[i]
            break
    data_manager.write_table_to_file("crm/customers.csv", table)
    return table


def update(table, id_):
    for sublist in table:
        try:
            if id_[0] in sublist:
                inputs = ui.get_inputs(["Full name: ", "E-mail address: ", "Subscription (1/0): "], "")
                for item in range(len(sublist)):
                    sublist[item] = inputs[item]
        except KeyError as err:
            ui.print_error_message(str(err))

    data_manager.write_table_to_file("crm/customers.csv", table)

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    name = []
    for i, value in enumerate(table):
        name.append(value[1])
    longest_name = (max(name, key=len))
    for i, value in enumerate(table):
        if longest_name in value[1]:
            ui.print_result(value[0], label="")


def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    subscribed = []
    email = []
    for i, value in enumerate(table):
        if "1" in value:
            subscribed.append(value[1])
            email.append(value[2])
    subscribed_plebs = dict(zip(subscribed, email))
    subscribed_plebs = str(subscribed_plebs)
    ui.print_result(subscribed_plebs, label="")
