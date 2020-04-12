'''
import morsenary
x = 'dsadasdas'                                           # example usage
print(morsenary.convert(x, 'b', spaces=True, beep=False)
'''


#-------import module-----#

import random
import winsound
from threading import Thread
import textwrap

#------set up classes------#

class configuration():
    def __init__(self,onefreq,zerofreq,onedura,zerodura,longfreq,shortfreq,longdura,shortdura,spacefreq,spacedura):
        self.onefreq = onefreq
        self.zerofreq = zerofreq
        self.onedura = onedura
        self.zerodura = zerodura
        self.longfreq = longfreq
        self.shortfreq = shortfreq
        self.longdura = longdura      #these stuff here are for the auditory parts of the module
        self.shortdura = shortdura
        self.spacefreq = spacefreq
        self.spacedura = spacedura
        self.elements = onefreq,zerofreq,onedura,zerodura,longfreq,shortfreq,longdura,shortdura

        
#default configuration, change the values to set it up for urself

beepo = configuration(2900,4400,250,200,    2500,2500, 500, 200, 3000,  1000)
#                       ^    ^   ^    ^      ^     ^    ^    ^     ^    ^
#                      one  zero one  zero   long shrt long shrt  spc   spc
#                      freq freq dura dura   freq freq dura dura  freq  dura

debugge = False

durationshortener = 1
#                    ^
#                 defaulted to 1


#---don't touch---#
durationshortener = float(1 / durationshortener)
mors={'a':'.- ','b':'-... ','c':'-.-. ','d':'-.. ','e':'. ','f':'..-. ','g':'--. ','h':'.... ','i':'.. ','j':'.--- ','k':'-.- ','l':'.-.. ','m':'-- ','n':'-. ','o':'--- ','p':'.--. ','q':'--.- ','r':'.-. ','s':'... ','t':'- ','u ':'..- ','v':'...- ','w':'.-- ','x':'-..- ','y':'-.-- ','z':'--.. ','1':'.---- ','2':'..--- ','3':'...-- ','4':'....- ','5':'..... ','6':'-.... ','7':'--... ','8':'---.. ','9':'----. ','0':'----- '}
beepo.onedura,beepo.zerodura,beepo.longdura,beepo.zerodura,beepo.spacedura = int(beepo.onedura * durationshortener), int(beepo.zerodura * durationshortener), int(beepo.longdura * durationshortener), int(beepo.shortdura * durationshortener), int(beepo.spacedura * durationshortener)
print(beepo.onedura, beepo.zerodura, beepo.longdura, beepo.shortdura) if debugge else None
settings = beepo.elements

#---loop---#
def binarybeeper(heh, space):
    heh = heh.replace(' ', '')
    for i in range(len(heh)):
        if heh[i] == '1':
            winsound.Beep(beepo.onefreq, beepo.onedura)
        if heh[i] == '0':
            winsound.Beep(beepo.zerofreq, beepo.zerodura)
    return

def morsebeeper(heh, space):
    heh = heh.replace('çç', ' ')
    if heh[-1] == ' ':
        heh = heh[:-1]
    for i in range(len(heh)):
        if heh[i] == '-':
            winsound.Beep(beepo.longfreq, beepo.longdura)
        if heh[i] == '.':
            winsound.Beep(beepo.shortfreq, beepo.shortdura)
        if heh[i] == ' ':
            winsound.Beep(beepo.spacefreq, beepo.spacedura)
    return
def convert(text, mb, spaces=True, beep=False):
    '''Returns the converted equalivent of text you entered according to the flags; mb (morse/binary), spaces and beep
    text is whatever you want to convert
    mb is the mode of the conversion
    spaces is if you want spaces in your conversion for example: 010101 10101 1010 instead of 010101101011010
    beep is if you want sound output upon finish of the function'''
    mors={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----'}
    if mb.lower() in ('binary', 'b'):     #   ^   morse code dict for   ^
        b = ''                            #   |   conversion            |
        for i in range(len(text)):
            b += f'{ord(text[i]):08b}'
        if beep == True:
            b = b.replace(' ', '')
            thread = Thread(target=binarybeeper, args=(b,1 if beep else None))
            thread.start()
        if spaces:
            b = ' '.join(textwrap.wrap(b, width=8))
            return b
        else: 
            return b
        
    elif mb.lower() in ('morse', 'm'):
        toreplace={ord('ğ'): 'g', ord('ü'): 'u', ord('ş'): 's', ord('ı'): 'i', ord('ö'): 'o', ord('ç'): 'c', ord('.'): '', ord(';'): '', ord(','): '', ord('*'): '', ord('-'): '',}
              # ^^ did these so non-ascii characters are converted to ascii, therefore the program doesnt raise any error
        text = str(text) # did that to fix 0 = ----- error
        text = text.lower(); text = text.translate(toreplace)
        b = ''
        for k in range(len(text)):
            b += mors[text[k]] + 'çç' #take the value of k'th element in text which is located in dictmors
        x = b                    #it iterates through str(text), not dict(mors)
        if beep == True: #      made this so normal spaces dont interfere with others
            b = b # we didnt replace this here
            thread = Thread(target=morsebeeper, args=(b,1 if spaces else None))
            thread.start()
        if not spaces:
            x = x.replace(' ', ''); x = x.replace('çç','')
            return x
        else:
            b = x.replace('çç', ' ')
            return b 
