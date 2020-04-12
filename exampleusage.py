import morsenary
variables = mode, space, bee = 0,0,0

def main():
    global variables
    global text
    mode = input('Mode? Morse/Binary: ')
    if mode.lower() in('m', 'morse', 'b', 'binary'):
        space = True
        # space = input('Do u want Spaces? Blank if you dont: ')
        # if space != '':                                        # did these so there wouldn't be any problems with morse
        #     space = True                                       # for it is defaulted to True for binary anyway
        # else:
        #     space = False
        bee = input('Do u want audio output? Blank if you dont: ')
        if bee != '':
            bee = True
        else:
            bee = False
        print(morsenary.convert(text, mode, spaces=space, beep=bee))
        declare()
    else:
        main()
def declare():
    global variables
    global text
    text = input('Input whatever you want to be converted: ')
    main()

if __name__ == '__main__':
    declare()
## spaces flag doesnt work well with morse
