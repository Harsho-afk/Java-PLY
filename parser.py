import ply.yacc as yacc

from lexer import tokens

# Grammar rule for the start symbol
def p_program(p):
    '''program : statement
               | program statement'''
    pass

# Grammar rule for different types of statements
def p_statement(p):
    '''statement : variable_declaration
                 | if_statement
                 | while_statement'''
    pass

# Grammar rule for variable declarations
def p_variable_declaration(p):
    '''variable_declaration : INT IDENTIFIER EQUALS expression SEMICOLON
                            | INT IDENTIFIER SEMICOLON
                            | FLOAT IDENTIFIER EQUALS expression SEMICOLON
                            | FLOAT IDENTIFIER SEMICOLON
                            | BOOLEAN IDENTIFIER EQUALS expression SEMICOLON
                            | BOOLEAN IDENTIFIER SEMICOLON'''
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
                  | TRUE
                  | FALSE
                  | NOT expression'''
    pass

# Grammar rule for if else statements
def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN LBRACE program RBRACE
                    | IF LPAREN expression RPAREN LBRACE program RBRACE ELSE LBRACE program RBRACE'''
    pass

# Grammar rule for while statements
def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN LBRACE program RBRACE'''
    pass

error = False
# Error handling rule for syntax errors
def p_error(p):
    global error
    error = True
    if p:
        print(f"Syntax error at token {p.type}, value: '{p.value}', line: {p.lineno}")
    else:
        print("Syntax error at end of input.")

parser = yacc.yacc()

data = '''int x = 5;'''

result = parser.parse(data)

if error:
    print("Parsing encountered syntax errors")
else:
    print("Parsing completed successfully")
