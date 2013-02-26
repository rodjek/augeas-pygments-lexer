"""
Augeas syntax highlighting for Pygments.
"""

from setuptools import setup
 
__author__ = 'tim@sharpe.id.au'
 
setup(
    name='Augeas Pygments Lexer',
    version='0.0.1',
    description=__doc__,
    author=__author__,
    packages=['augeas_lexer'],
    entry_points='''[pygments.lexers]
augeas = augeas_lexer:AugeasLexer
augtool-shell = augeas_lexer:AugtoolShellLexer
augtool = augeas_lexer:AugtoolLexer
puppet-augeas = augeas_lexer:PuppetAugeasLexer
'''
)
