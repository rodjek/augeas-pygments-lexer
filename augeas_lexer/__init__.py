from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

class AugeasLexer(RegexLexer):
    name = 'Augeas'
    aliases = ['augeas']
    filenames = ['*.aug']

    tokens = {
        'root': [
        ],
