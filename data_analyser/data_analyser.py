"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoud using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm


def start_module():
    while True:
        options = ["Get the last buyer name",
                   "Get the last buyer ID",
                   "Get the buyer name spent most and the money spent",
                   "Get the buyer ID spent most and the money spent",
                   "What is the id of the customer with the longest name?",
                   "Which customers has subscribed to the newsletter?"]
        ui.print_menu("Customer relationship manager", options, "Back to main menu")
        table = data_manager.get_table_from_file("crm/customers.csv")

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


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    # your code


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    # your code


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    # your code


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    # your code


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    # your code


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    # your code
