import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from BachVisitor import BachVisitor

input_stream = FileStream(sys.argv[1])

lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)

parser = ExprParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))

visitor = BachVisitor()
visitor.visit(tree)