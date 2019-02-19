""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
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
                   "What is the id of the item that was sold for the lowest price?",
                   "Which items are sold between two given dates? "]
        ui.print_menu("Sales", options, "Back to main menu")

        table = data_manager.get_table_from_file("sales/sales.csv")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        try:
            if option == "1":
                show_table(table)
                break
            elif option == "2":
                return add(table)
            elif option == "3":
                id_ = ui.get_inputs(["Please give me an ID to delete: "], "")
                remove(table, id_)
                break
            elif option == "4":
                id_ = ui.get_inputs(["Please give me an ID to update: "], "")
                update(table, id_,)
            elif option == "5":
                get_lowest_price_item_id(table)
                break
            elif option == "6":
                # table, month_from, day_from, year_from, month_to, day_to, year_to = ui.get_inputs(
                # ["month_from", "day_from", "year_from", "month_to", "day_to", "year_to"], "")
                get_items_sold_between(table)
                break
            elif option == "0":
                break
        except KeyError as err:
            ui.print_error_message(str(err))


def show_table(table):
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year", "Customer ID"]
    ui.print_table(table, title_list)
    return start_module()


def add(table):
    list_labels = ["Title",
                   "Price",
                   "Month",
                   "Day",
                   "Year"]
    new_id = common.generate_random()
    new_data = ui.get_inputs(list_labels, "")
    new_data.insert(0, new_id)
    table = common.add_line_to_file("sales/sales.csv", new_data)
    return table


def remove(table, id_):
    for i in range(len(table)):
        if table[i][0] == id_:
            del table[i]
            break
        data_manager.write_table_to_file("sales/sales.csv", table)
        return table


def update(table, id_):
    for sublist in table:
        if id_[0] in sublist:
            inputs = ui.get_inputs(["ID", "Title", "Price", "Month", "Day", "Year"], "")
            for item in range(len(sublist)):
                sublist[item] = inputs[item]

    data_manager.write_table_to_file("sales/sales.csv", table)
    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    price = []
    for i, value in enumerate(table):
        price.append(value[2])
    lowest_sold = min(price)
    for i, value in enumerate(table):
        if lowest_sold in value[2]:
            # print(value[0])
            ui.print_result(value[0], label="")


def get_items_sold_between(table):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code


# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_title_by_id_from_table(table, id):
    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    # your code


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    # your code


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    # your code


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    # your code


def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
