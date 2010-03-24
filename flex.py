# Compilers - Project 1
# Reykjavik University, Spring 2010
# Haukur Jonasson, Skuli Arnlaugsson

# This is the lexical analyser file as requested in part 1 of the assignment.
# -*- coding: utf-8 -*-
import ply.lex as lex
from token import tokens, reserved, op_Type

# Grammar rules from the project's description
#   NB: these rules need the @TOKEN to be implemented (see below).
letter              = r'[a-zA-Z]'
digit               = r'[0-9]'
digits              = digit + r'(' + digit + r')*'
int_num             = digits
optional_fraction   = r'\.'+int_num
optional_exponent   = r'[Ee]' + int_num
real_num            = int_num + r'(' + optional_fraction + r')?(' + optional_exponent + r')?'
identifier          = letter + r'(' + letter + r'|' + digit + r')*'

relop       = r'(\=)|(<\=)|(<)|(<>)|(>=)|(>)'
addop       = r'(\+)|(-)|(or)'
mulop       = r'(\*)|(/)|(div)|(mod)|(and)'
assignop    = r':\='

# Simple regular expressions for tokens that have no datatype and no optype.
# These can be defined directly by saying t_NAME = r'xxx' <= but this prevents us from
# adding special notes such as dt or opType.
t_tc_SEMICOL   = r';'
t_tc_COLON     = r':'
t_tc_COMMA     = r','
t_tc_DOTDOT    = r'\.\.'
t_tc_DOT       = r'\.'
t_tc_LPAREN    = r'\('
t_tc_LBRACKET  = r'\['
t_tc_RPAREN    = r'\)'
t_tc_RBRACKET  = r'\]'


# For more complicated items, such as ID, Keywords, Number and Ops we need rules like the following:
@lex.TOKEN(relop)
def t_tc_RELOP(t):
    t.OpType = op_Type.get(t.value)
    t.DataType = 'dt_OP'
    return t

@lex.TOKEN(addop)
def t_tc_ADDOP(t):
    t.OpType = op_Type.get(t.value)
    t.DataType = 'dt_OP'
    return t

@lex.TOKEN(mulop)
def t_tc_MULOP(t):
    t.OpType = op_Type.get(t.value)
    t.DataType = 'dt_OP'
    return t

@lex.TOKEN(assignop)
def t_tc_ASSIGNOP(t):
    t.OpType = op_Type.get(t.value)
    t.DataType = 'dt_OP'
    return t

@lex.TOKEN(real_num)
def t_tc_REAL_NUM(t):
    t.type = 'tc_NUMBER' # Change token type to Number (according to the project's description).
    t.DataType = 'dt_REAL'
    return t

@lex.TOKEN(int_num)
def t_tc_INT_NUM(t):
    t.type = 'tc_NUMBER' # Same as above.
    t.DataType = 'dt_INTEGER'
    t.OpType = 'op_NONE'
    return t

@lex.TOKEN(identifier)
def t_tc_ID(t):
    if t.value.lower() in reserved:
        # Check if id.value is a keyword, if so change type and datatype.
        t.type = reserved.get(t.value.lower())
        t.DataType = 'dt_KEYWORD'
    else:
        # Plain old ID, add the datatype flag.
        t.DataType = 'dt_ID'
    return t


def t_newline(t):
    # Instead of just discarding line no's, we count them to give better error messages.
    # This will help greatly with our parser project! Thank you Python!
    r'\n+'
    t.lexer.lineno += len(t.value)

# But we want to ignore whitespaces.
t_ignore  = ' \t'

def t_COMMENT(t):
    # And comments starting with '{' and ending with '}'.
    r'\{.*\}'
    pass

def t_error(t):
    # Mark as error, skip over and return ERROR token.
    t.type = 'tc_ERROR'
    t.DataType = 'dt_NONE'
    t.lexer.skip(1)
    return t