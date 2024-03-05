import ttg, re
from calculator import *

argumento = input("insert the thing: ")

valores = re.findall(r"\b(?!and\b|or\b|not\b)\w+\b", argumento)

proposicoes = list(dict.fromkeys(valores))

# print(ttg.Truths(proposicoes, [argumento]))

calculator = Calculator()

calculator.set_expression(argumento)

print(calculator.get_propositions())

print(calculator.get_truth_table())