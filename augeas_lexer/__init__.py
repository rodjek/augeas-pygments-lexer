from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

class AugeasLexer(RegexLexer):
    """
    Lexer for Augeas modules
    """

    name = 'Augeas'
    aliases = ['augeas', 'aug']
    filenames = ['*.aug']

    tokens = {
        'root': [
            (r'(module)(\s*)([^\s=]+)', bygroups(Keyword.Namespace, Text, Name.Namespace)),
            (r'(let)(\s*)([^\s=]+)', bygroups(Keyword.Declaration, Text, Name.Variable)),
            (r'(del|store|value|counter|seq|key|label|autoload|incl|excl|transform|test|get|put)(\s+)', bygroups(Name.Builtin, Text)),
            (r'(\()([^\:]+)(\:)(unit|string|regexp|lens|tree|filter)(\))', bygroups(Punctuation, Name.Variable, Punctuation, Keyword.Type, Punctuation)),
            (r'\(\*', Comment.Multiline, 'comment'),
            (r'[\+=\|\.\*\;\?-]', Operator),
            (r'[\[\]\(\)\{\}]', Operator),
            (r'"', String.Double, 'string'),
            (r'\/', String.Regex, 'regex'),
            (r'([A-Z]\w*)(\.)(\w+)', bygroups(Name.Namespace, Punctuation, Name.Variable)),
            (r'.', Name.Variable),
            (r'\s', Text),
        ],
        'string': [
            (r'\\.', String.Escape),
            (r'[^"]', String.Double),
            (r'"', String.Double, '#pop'),
        ],
        'regex': [
            (r'\\.', String.Escape),
            (r'[^\/]', String.Regex),
            (r'\/', String.Regex, '#pop'),
        ],
        'comment': [
            (r'[^*\)]', Comment.Multiline),
            (r'\(\*', Comment.Multiline, '#push'),
            (r'\*\)', Comment.Multiline, '#pop'),
            (r'[\*\)]', Comment.Multiline)
        ],
    }

class AugtoolShellLexer(RegexLexer):
    """
    Lexer for Augtool shell sessions.
    """

    name = 'AugtoolShell'
    aliases = ['augtool-shell']
    filenames = ['*.augtoolshell']

    tokens = {
        'root': [
            (r'^\s+$', Text),           # empty line
            (r'^[;#].*?$', Comment),    # comment
            (r'^(rm\s+:.*)', Text),     # removed nodes
            (r'^(Saved.*)', Text),      # saved
            (r'^(augtool\>)(\s+)(\S+)(?:(\s+)(.*))?$',   # augtool prompt
             bygroups(Generic.Prompt, Whitespace, Keyword, Whitespace, String)),
            (r'^([^=]+)(?:(\s+)(=)(\s+)(.*))?$',    # ls/get/print
             bygroups(String, Whitespace, Operator, Whitespace, String)),
            (r'^(\S+)(\s+)(label)(=)(\S+)(\s+)(value)(=)(\S+)(\s+)(span)(=)(\S+)$',  # span output
             bygroups(String, Whitespace, Keyword, Operator, String, Whitespace,
                                    Keyword, Operator, String, Whitespace,
                                    Keyword, Operator, String)),
        ]
    }


class AugtoolLexer(RegexLexer):
    """
    Lexer for Augtool commands
    """

    name = 'Augtool'
    aliases = ['augtool']
    filenames = ['*.augtool']

    tokens = {
        'root': [
            (r'^\s+$', Text),            # empty line
            (r'[;#].*?$', Comment),      # comment
            (r'^(\S+)(?:(\s+)(.*))?$',   # augtool command
             bygroups(Keyword, Whitespace, String)),
        ]
    }


class PuppetAugeasLexer(RegexLexer):
    """
    Lexer for the Puppet Augeas type
    """

    name = 'PuppetAugeas'
    aliases = ['puppet-augeas']
    filenames = ['*.pp-aug']

    tokens = {
        'root': [
            (r'^\s+$', Text),            # empty line
            (r'[;#].*?$', Comment),
            (r'[\[\]{}]', Operator),
            (r'=>', Operator),
            (r',', Text),
            (r'(\w+)(\s+)({)(\s+)(".*")(:)',
             bygroups(Keyword, Whitespace, Operator,
                      Whitespace, Name.Namespace, Text)),
            (r'(\s*)(context)(\s+)(=>)(\s+)(".*")(,)?',
             bygroups(Whitespace, Keyword, Whitespace, Operator,
                      Whitespace, String, Text)),
            (r'(\s*)(changes)(\s+)(=>)(\s+)(\[)',
             bygroups(Whitespace, Keyword, Whitespace, Operator,
                      Whitespace, Operator)),
            (r'(\s*)(onlyif)(\s+)(=>)(\s+)(".*")(,)?',
             bygroups(Whitespace, Keyword, Whitespace, Operator,
                      Whitespace, String, Text)),
            (r'(\s*)(".*")(,)?',
             bygroups(Whitespace, String, Text)),
            (r'(\s*)(\])(,)?',
             bygroups(Whitespace, Operator, Text)),
        ]
    }


