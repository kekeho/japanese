import japanese
pass_chars = ['。', '、', ' ', '\n', '\t', '\b', '\r', '\f']

def hiragana(string: str) -> bool:
    for char in string:
        if(char in pass_chars or char in japanese.hira_to_katakana_dict):
            pass
        else:
            return False
    # every char is Hiragana
    return True


def katakana(string: str) -> bool:
    for char in string:
        if(char in pass_chars or char in japanese.katakana_to_hira_dict):
            pass
        else:
            return False
    # every char is Katakana
    return True
