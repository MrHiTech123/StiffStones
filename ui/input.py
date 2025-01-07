

def linput(__prompt):
    """Returns a lowercase inputted value"""
    return input(__prompt).lower()

def wait_for_continue():
    while linput("Type \"continue\" to continue:\n") != 'continue':
        pass