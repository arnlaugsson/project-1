# Compilers - Project 1
# Reykjavik University, Spring 2010
# Haukur Jonasson, Skuli Arnlaugsson

# This is the lexical analyser file as requested in part 2 of the assignment.
# -*- coding: utf-8 -*-
import ply.lex
import flex
from token import Token

class Scanner:
    """ The scanner class has a lexer and can deliver tokens on request."""
    def __init__(self,input='input/input.txt',module=flex):
        """ Initializes a scanner instance.

        @optional: input    is the input file to read from
        @optional: module   is the lexical rules .py file to be used

        """
        self.lexer = ply.lex.lex(module=flex)
        self.lexer.input(open(input).read())

    def nextToken(self):
        """ Returns the next token in the input file from the lexer."""
        lexeme = self.lexer.token()

        if not lexeme:
            # If no token was returned, EOF reached, break loop.
            token = Token('tc_EOF',('','op_NONE'),'dt_NONE')
            return token

        TokenCode = lexeme.type


        try:
            opType = lexeme.OpType
        except:
            opType = 'op_NONE'
        DataValue = lexeme.value,opType


        try:
            DataType = lexeme.DataType
        except:
            DataType = 'dt_NONE'

        token = Token(TokenCode, DataValue, DataType)
        

        return token

