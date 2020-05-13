#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# In[188]:

import sys
import module
import pathlib


def stedtxt(tekst, space, space_irr, lowercase, errors, info, write):
    assert type(tekst) is str
    assert type(space) and type(space_irr) and type(lowercase) and type(
        errors) and type(info) and type(write) is bool
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
        tekst = str(error) + str(information) + str(tekst)
        if write:
            module.write_txt(pathlib.Path().absolute(), tekst)
        else:
            return tekst


print(stedtxt("ala ,  ma  kota .a kot( ma Ale ). a ja np. nie . Proces Norymberski nie odbyl sie według ustalonej konwencji.",
              space=True, space_irr=True, lowercase=True, errors=True, info=True, write=False))


# In[ ]:
