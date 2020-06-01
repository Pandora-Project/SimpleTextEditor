#!/usr/bin/env python
# coding: utf-8

# In[10]:
import codecs
import os
import sys
import argparse

separators = "\"\\!?.,{};:'\n()[-–|'<>«»~%“”„”_=*¯#+/]\f\t\r\v"


def args():
    """
    Arguments parser for command-line
    """
    parser = argparse.ArgumentParser(
        description="Python text beautifier. Formats texts.",
        usage=f"python {sys.argv[0]} path/text [-a] [-s] [-sirr] [-lcs] [-e] [-i] [-w path]"
    )
    # Input file or text [required]
    parser.add_argument("tekst", metavar="path/text", nargs=1,
                        help="Path to source file/Text itself")
    # Switches on all options
    parser.add_argument("-a", "--all_in", required=False, action="store_const", const=True,
                        default=False, help="Switches on all options")
    # Formats double spaces [optional]
    parser.add_argument("-s", "--spaces", required=False, action="store_const", const=True,
                        default=False, help="Removes exta spaces.")
    # Formats wrong spaces [optional]
    parser.add_argument("-r", "--spaces_irr", required=False, action="store_const", const=True,
                        default=False, help="Formats spaces in the text.")
    # Formatss capital letters [optional]
    parser.add_argument("-l", "--lowercase", required=False, default=False, action="store_const",
                        const=True, help="Capitalizes the letters where it's needed.")
    # Finds errors [optional]
    parser.add_argument("-e", "--errors", required=False, default=False,
                        action="store_const", const=True, help="Finds Polish grammar mistakes.")
    # Prints info [optional]
    parser.add_argument("-i", "--info", required=False, default=False, action="store_const",
                        const=True, help="Returns the info about the text.")
    # Writes to file [optional]
    parser.add_argument("-w", "--write", required=False, metavar="path",
                        default=None, help="Path to output file('.txt')")

    args = parser.parse_args()
    tekst = args.tekst[0]
    all_in = args.all_in
    spaces = args.spaces
    spaces_irr = args.spaces_irr
    lowercase = args.lowercase
    errors = args.errors
    info = args.info
    write = args.write
    return tekst, all_in, spaces, spaces_irr, lowercase, errors, info, write


def text_open(tekst):
    """
    Opens text file

    Arguments:
        tekst (str) --  tekst file to be opened
    """

    with open(tekst, "rt", encoding="utf-8") as file:
        tekst = file.read()

    return tekst


def double_space_remover(tekst):
    """
    removes double spaces

    Arguments:
        tekst (str) -- given text to format

    Returns:
        str -- string without double whitespaces
    """
    tekst = " ".join(tekst.split())
    return tekst


def wrong_space_remover(tekst):
    """
    removes spaces not given in right places and fixes spaces after .?!,

    Arguments:
        tekst (str) -- given text to format

    Returns:
        str -- string without wrong whitespaces
    """
    tekst = tekst.replace(" ,", ",").replace(
        " )", ")").replace("( ", "(").replace(" .", ".")
    sentence_end = ".?!,"
    sentence_end = ",.?!"
    for i in range(len(tekst)):
        if tekst[i] in sentence_end:
            if tekst[i+1] != " ":
                tekst = tekst[:i] + tekst[i] + " " + tekst[i+1:]
    return tekst


def lowercase_fixer(tekst):
    """
    if letter after dot or dot and space is lowercase it will fix it
    with exceptions

    Arguments:
        tekst (str) -- given text to format

    Returns:
        str -- string without wrong lowercases
    """
    sentence_end = ".?!"
    if tekst[0].islower():
        tekst = tekst[0].swapcase() + tekst[1:]
    for a in range(len(tekst)-1):
        for j in sentence_end:
            if tekst[a] == j:
                if tekst[a + 1] != " ":
                    tekst = tekst[:a+1] + tekst[a+1].upper() + tekst[a+2:]
                else:
                    if tekst[a + 2] != " ":
                        tekst = tekst[:a+2] + tekst[a+2].upper() + tekst[a+3:]

    exceptions = ["np.", "inż.", "godz.", "tel.", "płn.",
                  "ppoż.", "gosp.", "polit.", "ul."]
    for k in exceptions:
        if tekst.find(k) == (-1):
            pass
        else:
            indx = tekst.find(k) + len(k)
            if tekst[indx + 1] != " ":
                tekst = tekst[:indx+1] + tekst[indx+1].lower() + tekst[indx+2:]
    return tekst


def check_mistakes(tekst):
    """
    checks for words in given dictionary and if they are not present adds them to mistakes

    Arguments:
        tekst (str) -- given text to check for mistakes

    Returns:
        str -- string with errors or one that says there are none
    """
    for el in separators:
        tekst = tekst.replace(el, " ")

    tekst = tekst.lower().split()
    with open("odm.txt", encoding="utf-8") as file:
        dictionary = file.read()

    mistakes = []

    for x in tekst:
        if x not in dictionary:
            mistakes.append(x)
    if len(mistakes) == 0:
        return "Mistakes were not found"
    else:
        return "These are found mistakes", mistakes


def info(tekst):
    """
    counts uppercases, lowercases, spaces, symbols, words and lines

    Arguments:
        tekst (str) -- given text to count

    Returns:
        str -- string with info
    """
    text = tekst
    count5 = text.count("\n") + 1
    for el in separators:
        text = text.replace(el, " ")
    words = len(text.replace("\n", " ").strip().split(
        " ")) if len(text) != 0 else 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    if len(tekst) == 0:
        count5 = 0
    for a in tekst:
        count4 += 1
        if a.isupper():
            count1 += 1
        elif a.islower():
            count2 += 1
        elif a.isspace():
            count3 += 1
    text_info = "\nUppercase - " + str(count1) + "\n"
    text_info += "Lowercase - " + str(count2) + "\n"
    text_info += "Spaces - " + str(count3) + "\n"
    text_info += "Symbols - " + str(count4) + "\n"
    text_info += "Words - " + str(words) + "\n"
    text_info += "Lines - " + str(count5) + "\n"
    return text_info


def write_txt(path, tekst):
    """
    writes txt files with errors, formated text and info about said text
    Arguments:
        path (str) -- path to given folder
        tekst (str) -- text with info, mistakes and formated text
    """
    file_name = input("Enter file name: ")
    fname = str(path) + "/" + f"{file_name}.txt"
    if not os.path.exists(path):
        os.makedirs(path)
        print("Path is created")
        with open(fname, "w", encoding="utf-8") as x:
            x.write(tekst)
    else:
        print("Are sure you want to overwrite that file? [Y/N]")
        answer = str(input())
        if answer == "Y" or "y":
            with open(fname, "w", encoding="utf-8") as x:
                x.write(tekst)
        elif answer == "N" or "n":
            return tekst
        else:
            print("Answer is not correct, try again")

  # In[ ]:


# %%
