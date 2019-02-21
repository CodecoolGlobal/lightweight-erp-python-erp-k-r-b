""" User Interface (UI) module """


def print_table(table, title_list):
    table.insert(0, title_list)
    # length_list = []
    # for lines in table:
    #     for items in lines:
    #         length_list.append(items)
    # longest_words_length = len(max(length_list, key=len))   # get the longest word in the new list
    # multiplier = len(title_list)*(longest_words_length)   # multiply it by the number of columns

    # for sublist in table:
    #    # print("\n")
    #    print("\n", "-" * multiplier)
    #    for j in sublist:
    #        for subj in j:
    #            len_of = len(subj)
    #            longest_smallest = len_of*longest_words_length
    #        print(f"|", f"{j:^15}", end=" "*len_of)
    #         print(f"|{j:^}",end =" "(longest_words_length-len(j)))
    #    print("\n", "-" * multiplier)
    # print("\n")
    columns = list(zip(*table))
    col_widths = [max(len(item)for item in rows) for rows in columns]

    for row in table:
        print("-"*sum(col_widths)+"-"*len(col_widths))
        print("|".join(word.rjust(width) for word, width in zip(row, col_widths)))
    print("-"*sum(col_widths)+"-"*len(col_widths), "\n")

    # for row in table:
    #     print("  ".join(word.rjust(width) for word, width in zip(row, col_widths)))


def print_result(result, label):
    # your code
    print("\n", result)
    print(label)


def print_menu(title, list_options, exit_message):
    # your code
    print(title)
    for i, v in enumerate(list_options, 1):
        print(i, v)
    print("0", exit_message)


def get_inputs(list_labels, title):
    inputs = []
    for i in range(len(list_labels)):
        answer = input(list_labels[i])
        inputs.append(answer)
    return inputs


def print_error_message(message):
    # your code
    print(str(message))
