# Compilers - Project 1
# Reykjavik University, Spring 2010
# Haukur Jonasson, Skuli Arnlaugsson

# This is the lexical analyser file as requested in part 5 of the assignment.
# -*- coding: utf-8 -*-

# Haukur to github, hello, do you read me? Over!

import sys
import ply.lex as lex
from scanner import Scanner
from symbolTable import SymbolTable

def main(*args):
    scanner = Scanner()
    symbolTable = SymbolTable()

    while True:
        # Get the next token from scanner
        token = scanner.nextToken()

        # Pretty print the token
        token.__repr__()


        if token.TokenCode == 'tc_ID':
            # Check if token exists in SymbolTable
            entry = symbolTable.lookup(token.DataValue[0].lower())

            if entry == -1 :  # -1 means not found in table
                # Entry does not exist -> add it!
                num = symbolTable.insert(token.DataValue[0].lower())

                # Associate the token with the entry
                token.setSymTabEntry(num)
            else:
                # Token exists:
                # Associate the token with the entry
                token.setSymTabEntry(entry)

        elif token.TokenCode == 'tc_NUMBER':
            # Same as for entry ..
            entry = symbolTable.lookup(token.DataValue[0].lower())
            if entry == -1:
                num = symbolTable.insert(token.DataValue[0].lower())
                token.setSymTabEntry(num)
            else:
                token.setSymTabEntry(entry)
                
        elif token.TokenCode == 'tc_EOF':
            # Reached end of input -> quit loop!
            break

    # Pretty print our table
    symbolTable.__repr__()

if __name__ == '__main__':
	sys.exit(main(*sys.argv))