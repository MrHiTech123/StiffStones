from ui.output import SlowPrinter, thing


if __name__ == '__main__':
    SlowPrinter.print(1, 3, 'hello', end='\n')
    name = SlowPrinter.input('Hello, enter your name: ')
    
    SlowPrinter.print("Hello,", thing(name))
