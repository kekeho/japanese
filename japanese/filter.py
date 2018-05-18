import japanese
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter

t = Tokenizer(mmap=True)

def part(string: str, type: list or str) -> list:
    #check all items in the list are str
    def checkListTypeIsStr(in_list: list) -> bool:
        if(not isinstance(in_list, list)):
            return False
        for item in in_list:
            if(not isinstance(item, str)):
                return False
            
        return True
    
    if isinstance(type, (str)) or checkListTypeIsStr(type):
        global t
        filter = [POSKeepFilter(type)]
        analyzer = Analyzer([], t, filter)
        return [token.surface for token in analyzer.analyze(string)]
    else:
        raise ValueError('arg must be list[str] or str')
