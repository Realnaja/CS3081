from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")
CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0: A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1: A says "We are both knaves." B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2: A says "We are the same kind." B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3 
# A says either "I am a knight" or "I am a knave"
# B says "A said 'I am a knave'" and "C is a knave." C says "A is a knight."

knowledge3 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),   
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),   
    Or(CKnight, CKnave), Not(And(CKnight, CKnave)), 

    # B says "A said 'I am a knave'"
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    # B says "C is a knave"
    Biconditional(BKnight, CKnave),
    # C says "A is a knight"
    Biconditional(CKnight, AKnight)
)

# Print every fact that must be true in each puzzle

print("Puzzle 0")
for symbol in [AKnight, AKnave]:
    if model_check(knowledge0, symbol):
        print(symbol)

print("Puzzle 1")
for symbol in [AKnight, AKnave, BKnight, BKnave]:
    if model_check(knowledge1, symbol):
        print(symbol)

print("Puzzle 2")
for symbol in [AKnight, AKnave, BKnight, BKnave]:
    if model_check(knowledge2, symbol):
        print(symbol)

print("Puzzle 3")
for symbol in [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]:
    if model_check(knowledge3, symbol):
        print(symbol)
