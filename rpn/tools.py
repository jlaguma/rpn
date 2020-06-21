import sys
import os
import re
import math
import click

from . import settings
from .stack import stack
from .ops import ops as operations


def show_ops():
    operations.show_ops()


def show_examples():
    """Show some usage examples."""
    click.echo(f"""
USAGE EXAMPLES.

rpn                       - launch in interactive mode
rpn [expression]          - evaluate a one line expression

NOTE:
rpn will execute the contents of ~/.rpnrc at startup if it exists.

One line expression examples:
-----------------------------
$ rpn 1 2 +
$ rpn 1 2 + dup * 3 repeat dup * * swap drop sqrt pi * 20 / round 1024 1024 * *

Interactive mode example:
-----------------------------
$ rpn
> 1 2 +
[3]> dup
[3 3]> *
[9]> 3 repeat dup * *
[9 729]> swap drop
[729]> sqrt
[27.0]> pi *
[84.82300164692441]> 20 /
[4.241150082346221]> round
[4]> macro kb 1024 *
[4]> macro mb 1024 1024 * *
[4]> dbg
kb=1024 *, mb=1024 1024 * * [4]> dbg
[4]> mb
[4194304]> x=
> dbg
kb=1024 *, mb=1024 1024 * *, x=4194304 > x x +
kb=1024 *, mb=1024 1024 * *, x=4194304 [8388608]> stack
Variables:
================
kb=1024 *
mb=1024 1024 * *
x=4194304
Stack:
================
8388608
--------
> 1 mb /
Variables:
================
kb=1024 *
mb=1024 1024 * *
x=4194304
Stack (upside down):
================
8.0
--------
> clr
Variables:
================
kb=1024 *
mb=1024 1024 * *
x=4194304
> clv
>
> exit
$
    """)


def generate_prompt():
    """Generate interactive mode prompt output."""
    dbg_output = ''
    stack_output = ''
    cur_stack = stack.dump()
    # format verbose output
    if settings.verbose and settings.stack_mode == 'h':
        tmp = []
        for k, v in settings.vars.items():
            tmp.append(f'{k}={v}')
        dbg_output = ', '.join(tmp)
        if dbg_output:
            dbg_output += ' '
    elif settings.verbose and settings.stack_mode == 'v':
        tmp = []
        dbg_output = 'Variables:\n================\n'
        for k, v in settings.vars.items():
            tmp.append(f'{k}={v}')
        dbg_output += '\n'.join(tmp)
    # format stack output
    if settings.stack_mode == 'h':
        stack_output = [apply_base(n) for n in cur_stack]
    elif settings.stack_mode == 'v':
        stack_output = '\nStack:\n================\n'
        for val in cur_stack:
            stack_output += f'{apply_base(val)}\n--------\n'
    return f"{dbg_output}{stack_output}"


def set_base(base):
    if base == '2':
        settings.base = 'b'
    elif base == '8':
        settings.base = 'o'
    elif base == '10':
        settings.base = 'd'
    elif base == '16':
        settings.base = 'x'


def set_mode(mode):
    settings.stack_mode = mode


def set_verbose():
    settings.verbose = True


def apply_base(n):
    """Convert integer into a particular base number."""
    # We can't convert floats, so we return them as is.
    if isinstance(n, float):
        return n
    else:
        return f'{n:{settings.base}}'


def is_number(n):
    return is_bin(n) or is_oct(n) or is_dec(n) or is_hex(n)


def is_bin(n):
    try:
        int(n, 2)
        return True
    except ValueError:
        return False


def is_oct(n):
    try:
        int(n, 8)
        return True
    except ValueError:
        return False


def is_dec(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def is_hex(n):
    try:
        int(n, 16)
        return True
    except ValueError:
        return False


def str_to_num(s):
    # if number is a decimal with .0, we convert it to integer
    if is_dec(s):
        n = float(s)
        if math.modf(n)[0] == 0.0:
            return int(n)
        return n
    elif is_bin(s):
        return int(s, 2)
    elif is_oct(s):
        return int(s, 8)
    elif is_hex(s):
        return int(s, 16)


def is_variable(v):
    """Checks if argument is the variable or a macro."""
    if v in settings.vars:
        return True
    return False


def save_variable(var):
    """Save variable."""
    settings.vars[var] = stack.pop()


def save_macro(data):
    """Save macro."""
    macro_name, macro_data = data[0], ' '.join(data[1:])
    settings.vars[macro_name] = macro_data


def process_rpnrc():
    """Read commands from ~/.rpnrc and execute them."""
    home = os.path.expanduser('~')
    path = os.path.join(home, '.rpnrc')
    if os.path.isfile(path):
        with open(path) as fp:
            for line in fp:
                digest_input(line.split())


def digest_input(commands):
    """Digest entire input string."""
    try:
        reg = re.compile('^[A-Za-z0-9_-]*=$')
        # detect macro command: eg. macro kb 1024 *
        if commands[0] == 'macro':
            save_macro(commands[1:])
        # detecting "x=" command
        elif reg.match(commands[0]):
            save_variable(commands[0][:-1])
        else:
            for command in commands:
                digest_command(command)
    except ValueError:
        if settings.verbose:
            click.echo('Something went wrong. Please check your arguments.')


def digest_command(command):
    """Digest a single command."""
    if is_number(command):
        stack.push(str_to_num(command))
    elif is_variable(command):
        variable_value = str(settings.vars[command])
        digest_input(variable_value.split())
    elif operations.is_operator(command):
        op = operations.ops()[command].op_function
        if command == 'repeat':
            op()
        else:
            for _ in range(settings.repeat):
                op()
            settings.repeat = 1
    else:
        click.echo(
            f'ERROR: {command} is not a number or a supported operator.')
        sys.exit(2)


def command_line_mode(commands):
    digest_input(commands)
    if settings.verbose:
        click.echo(generate_prompt())
    if (stack.size() > 0):
        click.echo(apply_base(stack.pop()))


def interactive_mode():
    while True:
        try:
            prompt = generate_prompt()
            data = input(f'{prompt}> ')
            if len(data.strip()):
                digest_input(data.split())
        except:
            # to exit cleanly at ctrl+c or ctrl+z
            sys.exit()
