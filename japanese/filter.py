import japanese
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter
import gc

t = Tokenizer(mmap=True)


def part(string: str, type: list or str) -> list:
    # check all items in the list are str
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


class FilteredObject():
    def __init__(self, string: str):
        global t
        word_list = t.tokenize(string, stream=False)

        del string
        gc.collect()

        self.noun = [obj.surface for obj in list(
            filter(lambda word: word.part_of_speech.split(',')[0] == '名詞', word_list))]
        self.verb = [obj.surface for obj in list(
            filter(lambda word: word.part_of_speech.split(',')[0] == '動詞', word_list))]
        self.postposition = [obj.surface for obj in list(
            filter(lambda word: word.part_of_speech.split(',')[0] == '助詞', word_list))]
        self.auxiliaryverb = [obj.surface for obj in list(
            filter(lambda word: word.part_of_speech.split(',')[0] == '助動詞', word_list))]
        self.adjective = [obj.surface for obj in list(
            filter(lambda word: word.part_of_speech.split(',')[0] == '形容詞', word_list))]
        self.conjunction = [obj.surface for obj in list(
            filter(lambda word: word.part_of_speech.split(',')[0] == '接続詞', word_list))]
        self.adverb = [obj.surface for obj in list(
            filter(lambda word: word.part_of_speech.split(',')[0] == '副詞', word_list))]
        self.filler = [obj.surface for obj in list(
            filter(lambda word: word.part_of_speech.split(',')[0] == 'フィラー', word_list))]
        self.symbol = [obj.surface for obj in list(
            filter(lambda word: word.part_of_speech.split(',')[0] == '記号', word_list))]
        self.prefix = [obj.surface for obj in list(
            filter(lambda word: word.part_of_speech.split(',')[0] == '接頭詞', word_list))]
        self.adnominal = [obj.surface for obj in list(
            filter(lambda word: word.part_of_speech.split(',')[0] == '連体詞', word_list))]
        self.interjection = [obj.surface for obj in list(
            filter(lambda word: word.part_of_speech.split(',')[0] == '感動詞', word_list))]
        
        del word_list
        gc.collect()


