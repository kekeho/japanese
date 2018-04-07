import japanese
pass_chars = ['。', '、', ' ', '\n', '\t', '\b', '\r', '\f']


def upper(string: str or list) -> str or list:
    """Convert to Ōmoji every char.
    Args:
        string(str or list[str]): Check string (or list)
    Returns:
        Converted string(str or list)
    """
    if(isinstance(string, str)):  # string is str
        for char in string:
            if(char in japanese.komoji_to_omoji_dict):
                # replace komoji to omoji
                string = string.replace(
                    char, japanese.komoji_to_omoji_dict[char])
        return string

    elif(isinstance(string, list)):  # string is list
        string_list = string
        return_list = []
        for string in string_list:
            for char in string:
                if(char in japanese.komoji_to_omoji_dict):
                    string = string.replace(
                        char, japanese.komoji_to_omoji_dict[char])
            return_list.append(string)
        return return_list


def lower(string: str or list) -> str or list:
    """Convert to Komoji every char.
    Args:
        string(str or list[str]): Check string (or list)
    Returns:
        Converted string(str or list)
    """
    if(isinstance(string, str)):  # string is str
        for char in string:
            if(char in japanese.omoji_to_komoji_dict):
                # replace omoji to komoji
                string = string.replace(
                    char, japanese.omoji_to_komoji_dict[char])
        return string

    elif(isinstance(string, list)):  # string is list
        string_list = string
        return_list = []
        for string in string_list:
            for char in string:
                if(char in japanese.omoji_to_komoji_dict):
                    string = string.replace(
                        char, japanese.omoji_to_komoji_dict[char])
            return_list.append(string)
        return return_list
