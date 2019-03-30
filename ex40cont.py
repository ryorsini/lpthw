class Idiot(object):

    def __init__(screech, sir):
        screech.sir = sir

    def a_man(screech):
        for i in screech.sir:
            print(i)

idiot1 = Idiot(["I am an idiot"])

idiot1.a_man()
