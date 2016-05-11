import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens


def p_ast_let(p):
    '''ast : let simb simb num 
           | let simb simb text
    '''
    ast = [p[1], p[2], p[3], p[4]]
    p[0] = ast

def p_ast_print(p):
    'ast : print lparen simb rparen'
    ast = [p[1], p[3]]
    p[0] = ast

def p_simbol(p):
    'simb : SIMB'
    p[0] = p[1]


def p_num(p):
    'num : NUM'
    p[0] = p[1]


# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ",p

def p_let(p):
    'let : LET'
    p[0] = p[1]

def p_text(p):
    'text : TEXT'
    p[0] = p[1]

def p_print(p):
    'print : PRINT'
    p[0] = p[1]

def p_lparen(p):
    'lparen : LPAREN'
    p[0] = p[1]

def p_rparen(p):
    'rparen : RPAREN'
    p[0] = p[1]

yacc.yacc()


