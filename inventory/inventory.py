""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used

Menu will look like:


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
                   "Which items have not exceeded their durability yet?",
                   "What are the average durability times for each manufacturer?"]
        ui.print_menu("Customer relationship manager", options, "Back to main menu")
        table = data_manager.get_table_from_file("inventory/inventory.csv")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        try:
            if option == "1":
                return show_table(table)
            elif option == "2":
                return add(table)
            elif option == "3":
                id_ = ui.get_inputs(["Please provide ID of customer to remove:   "], "")
                return remove(table, id_[0])
            elif option == "4":
                id_ = ui.get_inputs(["Please provide ID of customer to update:   "], "")
                return update(table, id_[0])
            elif option == "5":
                get_available_items(table)
                break
            elif option == "6":
                get_average_durability_by_manufacturers(table)
                break
            elif option == "0":
                break
        except KeyError as err:
            ui.print_error_message(str(err))


def show_table(table):
    table = data_manager.get_table_from_file("inventory/inventory.csv")
    title_list = ["ID", "Name", "Manufacturer", "Purchase Year", "Durability"]
    ui.print_table(table, title_list)
    return start_module()


def add(table):
    list_labels = ["Id: ",
                   "Console: ",
                   "Manufacturer: ",
                   "Release Fate: ",
                   "duability: "]
    new_id = common.generate_random()
    new_data = ui.get_inputs(list_labels, "")
    new_data.insert(0, new_id)
    table = common.add_line_to_file("inventory/inventory.csv", new_data)

    return table


def remove(table, id_):
    for i in range(len(table)):

        if table[i][0] == id_:
            del table[i]
            break
    data_manager.write_table_to_file("inventory/inventory.csv", table)
    return table

    # return table


def update(table, id_):
    for sublist in table:
        if id_[0] in sublist:
            inputs = ui.get_inputs(["ID", "Name", "Manufacturer", "Purchase Year", "Durability"], "")
            for item in range(len(sublist)):
                sublist[item] = inputs[item]

    data_manager.write_table_to_file("inventory/inventory.csv", table)
    return table


def get_available_items(table):
    available = []
    for i in range(len(table)):
        exceed_date = int(table[i][3]) + int(table[i][4])
        # print(exceed_date)
        if exceed_date > 2014:
            print(table[i])
            available.append(table[i])
    return available

    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table):
    manufacturer_all = []
    for i in range(len(table)):
        manufacturer_all.append(table[i][2])

    manu_0 = list(set(manufacturer_all))  # this is a list which contains one manufacturer only once.
    # print(genres_0)

    manu_sum = 0.0
    manu_avgs = []
    durability = []
    for i in range(len(manu_0)):
        manu_sum = 0.0
        durability = []
        product_quant_by_man = 0
        for j in range(len(table)):
            if table[j][2] == manu_0[i]:
                manu_sum += float(table[j][4])
                product_quant_by_man += 1
                durability.append(table[j][4])
                # print(manu_sum)
                # print(durability)
                # print(product_quant_by_man)
        current_avg = manu_sum/product_quant_by_man
        manu_avgs.append(current_avg)
    ui.print_result(dict(zip(manu_0, manu_avgs)), label="")

    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code


# start_module()
