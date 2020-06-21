from . import __version__, __author__


def add_custom_help(f):
    """
    Add the version of the tool to the help heading.
    :param f: function to decorate
    :return: decorated function
    """
    doc = f.__doc__
    f.__doc__ = f"""
Reverse Polish Notation Calculator (v{__version__}) by {__author__}

{doc}"""

    return f
