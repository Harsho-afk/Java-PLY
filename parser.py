import ply.yacc as yacc
import ply.lex as lex

# Tokens
tokens = [
    'IDENTIFIER', 'NUMBER', 'EQUALS', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE', 'SEMICOLON', 'LESS', 'GREATER', 'AND', 'OR', 'NOT', 'EQEQ', 'NOTEQ', 'COMMA','SLBRACE','SRBRACE'
]

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'int': 'INT',
    'float': 'FLOAT',
    'boolean': 'BOOLEAN',
    'true': 'TRUE',
    'false': 'FALSE',
    'return': 'RETURN'
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
t_COMMA = r','
t_LESS = r'<'
t_GREATER = r'>'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_EQEQ = r'=='
t_NOTEQ = r'!='
t_SLBRACE = r'\['
t_SRBRACE = r'\]'

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

# Grammar rules
def p_program(p):
    '''program : statement
               | program statement'''
    pass

# Grammar rule for return statements
def p_return_statement(p):
    '''return_statement : RETURN expression SEMICOLON'''
    pass

# Grammar rule for statements
def p_statement(p):
    '''statement : variable_declaration
                 | array_declaration
                 | if_statement
                 | while_statement
                 | expression EQUALS expression SEMICOLON
                 | function_declaration
                 | return_statement'''
    pass

# Grammar rule for variable declarations
def p_variable_declaration(p):
    '''variable_declaration : type IDENTIFIER EQUALS expression SEMICOLON
                            | type IDENTIFIER SEMICOLON'''
    pass

# Grammar rule for array declarations
def p_array_declaration(p):
    '''array_declaration : type IDENTIFIER SLBRACE NUMBER SRBRACE SEMICOLON
                         | type IDENTIFIER SLBRACE SRBRACE EQUALS LBRACE array_elements RBRACE SEMICOLON'''
    pass

# Grammar rule for array elements
def p_array_elements(p):
    '''array_elements : expression
                      | array_elements COMMA expression'''
    pass

# Grammar rule for function declarations
def p_function_declaration(p):
    '''function_declaration : type IDENTIFIER LPAREN parameter_list RPAREN LBRACE program RBRACE
                            | type IDENTIFIER LPAREN RPAREN LBRACE program RBRACE'''
    pass

# Grammar rule for parameter list
def p_parameter_list(p):
    '''parameter_list : type IDENTIFIER
                      | parameter_list COMMA type IDENTIFIER'''
    pass

# Grammar rule for types
def p_type(p):
    '''type : INT
            | FLOAT
            | BOOLEAN'''
    pass

# Grammar rule for expressions
def p_expression(p):
    '''expression : NUMBER
                  | IDENTIFIER
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | LPAREN expression RPAREN
                  | expression GREATER expression
                  | expression LESS expression
                  | expression AND expression
                  | expression OR expression
                  | expression EQEQ expression
                  | expression NOTEQ expression
                  | TRUE
                  | FALSE
                  | NOT expression'''
    pass

# Grammar rule for if statements
def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN LBRACE program RBRACE
                    | IF LPAREN expression RPAREN LBRACE program RBRACE ELSE LBRACE program RBRACE'''
    pass

# Grammar rule for while statements
def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN LBRACE program RBRACE'''
    pass

# Error handling rule
error = False

def p_error(p):
    global error
    error = True
    if p:
        print(f"Syntax error at token {p.type}, value: '{p.value}', line: {p.lineno}")
    else:
        print("Syntax error at end of input.")

# Build the parser
parser = yacc.yacc()

# Java code
data = ''''''

print(data)
result = parser.parse(data)
if error:
    print("Parsing encountered syntax errors")
else:
    print("Parsing completed successfully")
