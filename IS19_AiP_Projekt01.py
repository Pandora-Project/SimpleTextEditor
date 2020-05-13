#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[188]:


import module


def stedtxt(tekst, space, space_irr, lowercase, errors, info):
    assert tekst is list
    if space:
        tekst = module.double_space_remover(tekst)
    elif space_irr:
        tekst = module.wrong_space_remover(tekst)
    elif lowercase:
        tekst = module.lowercase_fixer(tekst)
    elif errors:
        error = module.checkmistakes(tekst)
    elif info:
        information = module.info(tekst)
  
    return tekst
stedtxt("ala , ma  kota .a kot( ma Ale ). a ja np. już nie :[[ ",
        space = True, space_irr = True, lowercase = True, errors = True, info = True)


# In[ ]:




