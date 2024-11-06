import ply.lex as lex

tokens = [
    'IDENTIFIER', 'NUMBER', 'EQUALS', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE', 'SEMICOLON', 'LESS', 'GREATER', 'AND', 'OR', 'NOT'
]

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'int': 'INT',
    'float': 'FLOAT',
    'boolean': 'BOOLEAN',
    'true': 'TRUE',
    'false': 'FALSE'
}

tokens = tokens + list(reserved.values())

# Regular expressions for each token type
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_LESS = r'<'
t_GREATER = r'>'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

# Regular expression for IDENTIFIER
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')    
    return t

# Regular expression for NUMBER
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
