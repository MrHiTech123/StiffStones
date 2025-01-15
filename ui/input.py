import consts

def linput(__prompt=""):
    """Returns a lowercase inputted value"""
    return input(__prompt).lower()

def enter_press(__prompt=""):
    """Takes user input but moves the text cursor back to the start of the previous line before returning"""
    to_return = input(__prompt)
    print(consts.escape_code.start_prev_line, end='')
    return to_return


def wait_for_continue():
    """Waits for the user to input "continue" """
    while linput("Type \"continue\" to continue:\n") != 'continue':
        pass