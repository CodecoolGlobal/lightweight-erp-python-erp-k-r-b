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
        options = ["Who didn't buy nothing?",
                   "Last buyer name",
                   "Last buyer ID",
                   "The buyer who spent the most, and the money",
                   "The ID who spent the most, and the money",
                   "Most frequent buyers ",
                   "Most frequent buyers, ID"]
        ui.print_menu("Data_analyser", options, "Back to main menu")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        try:
            if option == "1":
                customers_who_did_not_buy_nothing()
                break
            elif option == "2":
                return get_the_last_buyer_name()
            elif option == "3":
                get_the_last_buyer_id()
                break
            elif option == "4":
                get_the_buyer_name_spent_most_and_the_money_spent()
            elif option == "5":
                get_the_buyer_id_spent_most_and_the_money_spent()
                break
            elif option == "6":
                get_the_most_frequent_buyers_names(num=1)
                break
            elif option == "7":
                get_the_most_frequent_buyers_ids(num=1)
                break
            elif option == "0":
                break
        except KeyError as err:
            ui.print_error_message(str(err))


def customers_who_did_not_buy_nothing():
    """"""


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
