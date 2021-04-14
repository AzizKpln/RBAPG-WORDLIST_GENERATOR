
"""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _______     | || |   ______     | || |      __      | || |   ______     | || |    ______    | |
| | |_   __ \    | || |  |_   _ \    | || |     /  \     | || |  |_   __ \   | || |  .' ___  |   | |
| |   | |__) |   | || |    | |_) |   | || |    / /\ \    | || |    | |__) |  | || | / .'   \_|   | |
| |   |  __ /    | || |    |  __'.   | || |   / ____ \   | || |    |  ___/   | || | | |    ____  | |
| |  _| |  \ \_  | || |   _| |__) |  | || | _/ /    \ \_ | || |   _| |_      | || | \ `.___]  _| | |
| | |____| |___| | || |  |_______/   | || ||____|  |____|| || |  |_____|     | || |  `._____.'   | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
						BY:Aziz Kaplan
						Github:https://www.github.com/AzizKpln
						Youtube:https://www.youtube.com/channel/UCHGEA5g4iFDdBognYNWCJbA
						Note:Do not use it in illegal projects ;)
[!]To get help about usage, read the README.MD on github
https://www.github.com/AzizKpln/RBAPG
"""




"""
This simple script shows the usage of my RBAPG module.
See:https://github.com/AzizKpln/RBAPG   
"""

import RBAPG
import sys

RBAPG=RBAPG.RuleBasedAttackPasswordGenerator()

def set_a_name():
    wordlist_name=input("Input A Name For Wordlist\n->")
    RBAPG.setWordlistName(wordlist_name)
def set_a_length():
    length=int(input("Set a level for combination:min 2 - max 5\n->"))
    if length>5 or length<2:
        print("Max 5 Min 2")
        sys.exit()
    RBAPG.setLengthOfGeneratedPassword(int(length))
def wordlist_content():
    content=""
    name=input("Person's Name:")
    surname=input("Person's Surame:")
    birthday=input("Person's Birthday[blank_it_ifudk]:")
    pet=input("Person's Pet Name[blank_it_ifudk]:")
    if name=="":
        print("You left blank:Name")
    else:
        content+=name
    if surname=="":
        print("You left blank:Surname")
    else:
        content=content+" "+surname
    if birthday=="":
        print("You left blank:birthday")
    else:
        content=content+" "+birthday
    if pet=="":
        print("You left blank:Pet Name")
    else:
        content=content+" "+pet
    RBAPG.wordlist=content
    """You can add more options. There is no a stopping point in my RBAPG module"""
def combine_the_words():
    RBAPG.CombineTheWords()
def combine_the_words1():
    RBAPG.CombineCozily()
def generate_wordlist():
    RBAPG.generate_wordlist()

set_a_name()
set_a_length()
wordlist_content()
ask=input("Do You Want To Combine Each Of The Word(yes-no)?\n->")
if ask=="yes":
    combine_the_words()
ask2=input("Do you want to combine them with a spesific algorithm(yes-no)?\n->")
if ask2=="yes":
    combine_the_words1()
generate_wordlist()
