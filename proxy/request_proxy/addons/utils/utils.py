import re
from typing import List

def match_url(patterns: List[re.Pattern], string):
    return any([i.match(string) for i in patterns])

def match_word(words, string):
    return any([i in string for i in words])
