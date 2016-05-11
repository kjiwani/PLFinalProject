import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens


def p_ast_let(p):
    '''ast : let simb simb num 
           | let simb simb text
    '''
    ast = [p[1], p[2], p[3], p[4]]
    p[0] = ast

<<<<<<< HEAD
def p_ast_print(p):
    'ast : print lparen simb rparen'
    ast = [p[1], p[3]]
    p[0] = ast

=======
# func_dict = {}

# def let(x1, x2, x3):
#     if x1 in func_dict: 
#         return "this variable is already taken"
#     else: 
#         func_dict[x1] = x3



# name = {}
# let_dict = {} 

# global ast
# ast = []

# def cons(l):
#     return [l[0]] + l[1]

# name['cons'] = cons

# def concat(l):
#     return l[0] + l[1]

# name['concat'] = concat

# def listar(l):
#     return l

# name['list'] = listar

# def car(l):
#     return l[0][0]

# name['car'] = car

# def cdr(l):
#     return l[0][1:]

# name['cdr'] = cdr

# def eq(l):
#     return l[0] == l[1]

# name['eq'] = eq
# name['='] = eq

# def _and(l):
#     return not False in l

# name['and'] = _and

# def _or(l):
#     return True in l

# name['or'] = _or

# def cond(l):
#     if l[0]:
#         return l[1]

# name['cond'] = cond

# def add(l):
#     return sum(l)

# name['+'] = add

# def minus(l):
#     '''Unary minus'''
#     return -l[0]

# name['-'] = minus

# def _print(l):
#     print lisp_str(l[0])

# name['print'] = _print

# #  Evaluation functions

# def lisp_eval(simb, items):
#    if simb in name:
#        return call(name[simb], eval_lists(items))
#    else:
#     return [simb] + items

# def call(f, l):
#     try:
#         return f(eval_lists(l))
#     except TypeError:
#         return f

# def eval_lists(l):
#     r = []
#     for i in l:
#         if is_list(i):
#             if i:
#                 r.append(lisp_eval(i[0], i[1:]))
#             else:
#                 r.append(i)
#         else:
#             r.append(i)
#     return r

# # Utilities functions

# def is_list(l):
#     return type(l) == type([])

# def lisp_str(l):
#     if type(l) == type([]):
#         if not l:
#             return "()"
#         r = "("
#         for i in l[:-1]:
#             r += lisp_str(i) + " "
#         r += lisp_str(l[-1]) + ")"
#         return r
#     elif l is True:
#         return "#t"
#     elif l is False:
#         return "#f"
#     elif l is None:
#         return 'nil'
#     else:
#         return str(l)

# BNF



# def p_exp_atom(p):
#     'exp : atom'
#     p[0] = p[1]
    
# def p_exp_qlist(p):
#     'exp : quoted_list'
#     p[0] = p[1]

# def p_exp_call(p):
#     'exp : call'
#     p[0] = p[1]

# def p_quoted_list(p):
#     'quoted_list : QUOTE list'
#     #p[0] = p[2]
#     p[0] = ["quote"] + [p[2]]

# def p_list(p):
#     'list : items'
#     p[0] = p[2]

# def p_items(p):
#     'items : item items'
#     p[0] = [p[1]] + p[2]

# def p_items_empty(p):
#     'items : empty'
#     p[0] = []

# def p_empty(p):
#     'empty :'
#     pass

# def p_item_atom(p):
#     'item : atom'
#     p[0] = p[1]

# def p_item_list(p):
#     'item : list'
#     p[0] = p[1]

# def p_item_list(p):
#     'item : quoted_list'
#     p[0] = p[1]
        
# def p_item_call(p):
#     'item : call'
#     p[0] = p[1]

# def p_item_empty(p):
#     'item : empty'
#     p[0] = p[1]

# def p_call(p):
#     'call : SIMB items'
#     global ast
#     # if DEBUG: print "Calling", p[1], "with", p[2] 
#     #p[0] = lisp_eval(p[2], p[3])
#     ast = [p[1], [p[2]]]
#     return ast
#     print "ast is: ", ast
#     p[0] = ast

def p_ast(p):
    'ast : let simb simb num'
    ast = [p[1], p[2], p[3], p[4]]
    p[0] = ast

# def p_simbs(p):
#     'simbs : SIMB SIMB'
#     p[0] = [p[1], p[2]]

>>>>>>> 4750050fe165cb8237bc2ac477de6e3401e70900
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

<<<<<<< HEAD
def p_text(p):
    'text : TEXT'
    p[0] = p[1]

def p_print(p):
    'print : PRINT'
=======
# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ",p

def p_let(p):
    'let : LET'
>>>>>>> 4750050fe165cb8237bc2ac477de6e3401e70900
    p[0] = p[1]

def p_lparen(p):
    'lparen : LPAREN'
    p[0] = p[1]

def p_rparen(p):
    'rparen : RPAREN'
    p[0] = p[1]

<<<<<<< HEAD
yacc.yacc()


=======
# Build the parser
# Use this if you want to build the parser using SLR instead of LALRf
# yacc.yacc(method="SLR")
yacc.yacc()
>>>>>>> 4750050fe165cb8237bc2ac477de6e3401e70900
