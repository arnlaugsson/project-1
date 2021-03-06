# Compilers - Project 1
# Reykjavik University, Spring 2010
# Haukur Jonasson, Skuli Arnlaugsson

# This is the lexical analyser file as requested in part 3 of the assignment.
# -*- coding: utf-8 -*-
reserved = {
    'program'   : 'tc_PROGRAM',
    'var'       : 'tc_VAR',
    'array'     : 'tc_ARRAY',
    'of'        : 'tc_OF',
    'integer'   : 'tc_INTEGER',
    'real'      : 'tc_REAL',
    'function'  : 'tc_FUNCTION',
    'procedure' : 'tc_PROCEDURE',
    'begin'     : 'tc_BEGIN',
    'end'       : 'tc_END',
    'if'        : 'tc_IF',
    'then'      : 'tc_THEN',
    'else'      : 'tc_ELSE',
    'while'     : 'tc_WHILE',
    'do'        : 'tc_DO',
    'not'       : 'tc_NOT',
    'none'      : 'tc_NONE',
}

tokens = [
    'tc_ID',
    'tc_NUMBER',
    'tc_INT_NUM',
    'tc_REAL_NUM',
    'tc_ASSIGNOP',
    'tc_RELOP',
    'tc_ADDOP',
    'tc_MULOP',
    'tc_SEMICOL',
    'tc_COLON',
    'tc_COMMA',
    'tc_DOT',
    'tc_DOTDOT',
    'tc_LPAREN',
    'tc_LBRACKET',
    'tc_RPAREN',
    'tc_RBRACKET',
    'tc_ERROR',
] + list(reserved.values()) # NB: we also have the reserved keywords as tokens.


# Op_Type are the possible op types.
#   NB: Not all tokens have op types (default is null, not op_NONE).
op_Type = {
    '+'     : 'op_PLUS',
    '-'     : 'op_MINUS',
    'or'    : 'op_OR',
    '*'     : 'op_MULT',
    '/'     : 'op_DIVIDE',
    'and'   : 'op_AND',
    'div'   : 'op_DIV',
    'mod'   : 'op_MOD',
    '<'     : 'op_LT',
    '>'     : 'op_GT',
    '<='    : 'op_LE',
    '>='    : 'op_GE',
    '='     : 'op_EQ',
    '<>'    : 'op_NE',
    ':='    : 'op_NONE',
}

dataType = (
    'dt_INTEGER',
    'dt_REAL',
    'dt_ID',
    'dt_KEYWORD',
    'dt_OP',
    'dt_NONE',
)

class Token:
    def __init__(self, type, dataValue, dataType):
        self.TokenCode          = type
        self.DataValue          = dataValue
        self.DataType           = dataType

    def setSymTabEntry(self, entryNum):
        self.SymbolTableEntry   = entryNum

    def __repr__(self):
        if self.TokenCode == 'tc_ID':
            print self.TokenCode[3:] + '(' + self.DataValue[0].lower() + ')',
        elif self.TokenCode == 'tc_NUMBER':
            print self.TokenCode[3:] + '(' + self.DataValue[0] + ')',
        elif self.TokenCode in ('tc_RELOP','tc_ADDOP','tc_MULOP','tc_ASSIGNOP'):
            print self.TokenCode[3:] + '(' + self.DataValue[1][3:] + ')',
        else:
            print self.TokenCode[3:],
        


