#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# In[188]:

import sys
import module
import pathlib


def stedtxt(tekst, space=False, space_irr=False, lowercase=False, errors=False, info=False, write=False):
    """
    text editor

    Arguments:
        tekst (str) -- text given to format
        space (bool) -- if True: removes two whitespaces
        space_irr (bool) -- if True: removes spaces not given in right places
        lowercase (bool) -- if True: fixes wrong lowercases
        errors (bool) -- if True: returns list of mistakes
        info (bool) -- if True: gives info on formated text
        write (bool) -- if True: writes return to .txt


        str -- string with all the options given in arguments
    """
    tekst = module.text_open(tekst)
    assert type(tekst) is str
    if len(tekst) == 1:
        return tekst
    else:
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
        if write:
            module.write_txt(pathlib.Path().absolute(), tekst)
            return ("File succesfully saved")
        else:
            return tekst


if __name__ == '__main__':
    args = module.args()
    print(stedtxt(*args))

# In[ ]:
