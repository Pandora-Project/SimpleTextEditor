# Projekt_AIP

Arguments:
-s (removes extra white spaces)
-r (removes spaces in wrong places)
-l (fixes lowercases)
-e (checks text for errors)
-i (lists infromation about text)
-w path (writes file to given path)
Examples of use
Script in command line:

for text: ala , ma kota .a kot( ma Ale ). a ja np. nie . Proces Norymberski nie odbyl sie według ustalonej konwencji.
python ./IS19_AiP_Projekt01.py path_of_text -s -r -l -e -i

out: Mistakes were not found
Uppercase - 6
Lowercase - 72
Spaces - 16
Symbols - 102
Words - 24
Lines - 1
Ala, ma kota.A kot(ma Ale). A ja np. nie. Proces Norymberski nie odbyl sie według ustalonej konwencji.

if written with -w:
python ./IS19_AiP_Projekt01.py path_of_text -a

Enter file name: AAAAAAAAAAAA
Are sure you want to overwrite that file? [Y/N]
Y
File sucesfully saved

if written with -w and given option N:
python ./IS19_AiP_Projekt01.py path_of_text -a

Enter file name: sdfsdfsd
Are sure you want to overwrite that file? [Y/N]
N
Mistakes were not found
Uppercase - 6
Lowercase - 72
Spaces - 16
Symbols - 102
Words - 24
Lines - 1
Ala, ma kota.A kot(ma Ale). A ja np. nie. Proces Norymberski nie odbyl sie według ustalonej konwencji.
