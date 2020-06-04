#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# In[188]:

import sys
import module
import pathlib


def stedtxt(tekst, all_in=False, space=False, space_irr=False, lowercase=False, errors=False, info=False, outpath=False):
    """
    text editor

    Arguments:
        tekst (str) -- text given to format
        all_in (bool) -- if True: switches to True all other options
        space (bool) -- if True: removes two whitespaces
        space_irr (bool) -- if True: removes spaces not given in right places and fixes them afet ,.!?
        lowercase (bool) -- if True: fixes wrong lowercases
        errors (bool) -- if True: returns list of mistakes
        info (bool) -- if True: gives info on formated text
        outpath (bool) -- if True: writes return to .txt


        str -- string with all the options given in arguments
    """
    tekst = module.text_open(tekst)
    assert type(tekst) is str
    if len(tekst) == 1:
        return tekst
    else:
        if all_in:
            space = space_irr = lowercase = errors = info = True
        if space:
            tekst = module.double_space_remover(tekst)
        if space_irr:
            tekst = module.wrong_space_remover(tekst)
        if lowercase:
            tekst = module.lowercase_fixer(tekst)
        if errors:
            error = module.check_mistakes(tekst)
        if info:
            information = module.info(tekst)
        if errors and info:
            tekst = str(error) + str(information) + str(tekst)
        elif errors:
            tekst = str(error) + str(tekst)
        elif info:
            tekst = str(information) + str(tekst)
        if outpath:
            x = module.write_txt(tekst, pathlib.Path().absolute())
            if x == tekst:
                return tekst
            else:
                return "File sucesfully saved"
        else:
            return tekst


if __name__ == '__main__':
    args = module.args()
    print(stedtxt(*args))
