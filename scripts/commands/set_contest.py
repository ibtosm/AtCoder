import sys

from .create_snippets import main as create_snippets
from .update_contestid import main as update_contestid


def main(*args):
    msg = []
    if len(args):
        msg.append(update_contestid(args[0]))
    msg.append(create_snippets())

    return "\n".join(msg)


if __name__ == "__main__":
    # python -m scripts.commands.set_contest abc123
    print(main(*sys.argv[1:]))
