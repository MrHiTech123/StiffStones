from ui.output import tutorial


def simple(result: str):
    return lambda x: result

def exit():
    raise SystemExit(0)

actions = {
    'exit': exit,
    'help': tutorial
}