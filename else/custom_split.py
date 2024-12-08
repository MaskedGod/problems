"""
Implement a function that works the same as str.split method
(without using str.split itself, ofcourse).
Pay attention to strings with multiple spaces. For example: '    Hi     Python    world!'
Example:

    def split(data: str, sep=None, maxsplit=-1):"""


def split(data: str, sep=None, maxsplit=-1):
    # Raise an error if the separator is an empty string
    if sep == "":
        raise ValueError("separator cannot be an empty string")

    result = []  # List to store the resulting splits
    start_index = 0  # Starting index for the current split

    # If no separator is provided (None), split by whitespace
    if sep is None:
        looking_for_space = True  # Initially, we are looking for spaces
        for current_index, current_char in enumerate(
            data
        ):  # Loop over each character in the string
            # Check if the character matches the current state (looking for space or non-space)
            if current_char.isspace() == looking_for_space:
                if (
                    looking_for_space and start_index < current_index
                ):  # If we are at a space and have found a word
                    # If maxsplit is reached, stop adding more splits
                    if len(result) == maxsplit:
                        break
                    result.append(
                        data[start_index:current_index]
                    )  # Add the word (from start to current index)
                start_index = (
                    current_index  # Update the starting index for the next word
                )
                looking_for_space = (
                    not looking_for_space
                )  # Switch between looking for space or non-space
        # Append the final word if there's any remaining
        if looking_for_space and start_index < len(data):
            result.append(data[start_index:])
    else:
        # If a separator is provided, split by that separator
        while len(result) != maxsplit:  # Loop until we reach maxsplit
            try:
                current_index = data.index(
                    sep, start_index
                )  # Find the next occurrence of the separator
            except ValueError:  # If no more separators are found, stop
                break
            result.append(
                data[start_index:current_index]
            )  # Add the part before the separator
            start_index = current_index + len(
                sep
            )  # Update the starting index to after the separator
        # Append the remaining part after the last separator
        result.append(data[start_index:])

    return result  # Return the list of splits


print(split("    Hi     Python    world!"))
print(split("1<>2<>3<4", sep="<>"))
print(split("apple,orange,banana", sep=","))
print(split("1,,2", sep=","))
print(split("Python    2     3", maxsplit=1))
print(split(",123,", sep=","))
# assert split("") == []
# assert split(",123,", sep=",") == ["", "123", ""]
# assert split("test") == ["test"]
# assert split("Python    2     3", maxsplit=1) == ["Python", "2     3"]
# assert split("    test     6    7", maxsplit=1) == ["test", "6    7"]
# assert split("    Hi     8    9", maxsplit=0) == ["Hi     8    9"]
# assert split("    set   3     4") == ["set", "3", "4"]
# assert split("set;:23", sep=";:", maxsplit=0) == ["set;:23"]
# assert split("set;:;:23", sep=";:", maxsplit=2) == ["set", "", "23"]
"""
def split(data: str, sep=None, maxsplit=-1):
    # Raise an error if the separator is an empty string
    if sep == "":
        raise ValueError("separator cannot be an empty string")

    my_list = []  # List to store the resulting splits
    start = 0  # Starting index for the current split

    # If no separator is provided (None), split by whitespace
    if sep is None:
        wantspace = True  # Initially, we are looking for spaces
        for i, ch in enumerate(data):  # Loop over each character in the string
            # Check if the character matches the current state (looking for space or non-space)
            if ch.isspace() == wantspace:
                if wantspace and start < i:  # If we are at a space and have found a word
                    # If maxsplit is reached, stop adding more splits
                    if len(my_list) == maxsplit:
                        break
                    my_list.append(data[start:i])  # Add the word (from start to current index)
                start = i  # Update the starting index for the next word
                wantspace = not wantspace  # Switch between looking for space or non-space
        # Append the final word if there's any remaining
        if wantspace and start < len(data):
            my_list.append(data[start:])
    else:
        # If a separator is provided, split by that separator
        while len(my_list) != maxsplit:  # Loop until we reach maxsplit
            try:
                i = data.index(sep, start)  # Find the next occurrence of the separator
            except ValueError:  # If no more separators are found, stop
                break
            my_list.append(data[start:i])  # Add the part before the separator
            start = i + len(sep)  # Update the starting index to after the separator
        # Append the remaining part after the last separator
        my_list.append(data[start:])

    return my_list  # Return the list of splits

"""
