#!/usr/bin/env python
# coding: utf-8

# In[10]:
separators = "\"\\!?.,{};:'\n()[-–|'<>«»~%“”„”_=*¯#+/]\f\t\r\v"


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
    removes spaces not given in right places

    Arguments:
        tekst (str) -- given text to format

    Returns:
        str -- string without wrong whitespaces
    """
    tekst = tekst.replace(" ,", ",").replace(
        " )", ")").replace("( ", "(").replace(" .", ".")
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
    if tekst[0].islower():
        tekst = tekst[0].swapcase() + tekst[1:]
    for a in range(len(tekst)-1):
        if tekst[a] == ".":
            if tekst[a + 1] != " ":
                tekst = tekst[:a+1] + tekst[a+1].upper() + tekst[a+2:]
            else:
                if tekst[a + 2] != " ":
                    tekst = tekst[:a+2] + tekst[a+2].upper() + tekst[a+3:]
    exceptions = ["np.", "inż.", "godz.", "tel.", "płn.",
                  "ppoż.",                  "gosp.", "polit.", "ul."]
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
    with open("odm.txt") as file:
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
    for el in separators:
        text = text.replace(el, " ")
    words = len(text.replace("\n", " ").strip().split(
        " ")) if len(text) != 0 else 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = tekst.count("\n") + 1
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
    with open(path, "wt") as file:
        file.write(tekst)

# In[ ]:
