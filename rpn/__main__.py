import click
import sys

from rpn import __version__
import rpn.tools as tools
from .decorators import add_custom_help


@click.command()
@click.version_option(__version__, "-V", "--version", message="%(version)s")
@click.option(
    '--verbose',
    '-v',
    is_flag=True,
    help='Toggle verbose output.',
)
@click.option(
    '--ops',
    '-o',
    is_flag=True,
    help='Show available operations.',
)
@click.option(
    '--eg',
    '-e',
    is_flag=True,
    help='Show usage examples.',
)
@click.option(
    '--base',
    '-b',
    default='10',
    help='Set the default base.',
    type=click.Choice(['2', '8', '10', '16']),
)
@click.option(
    '--mode',
    '-m',
    default='h',
    help='Stack display mode.',
    type=click.Choice(['h', 'v']),
)
@click.argument('args', nargs=-1)
@add_custom_help
def main(verbose, ops, eg, base, mode, args):
    """Supports:\tcommand line mode, interactive mode, macros, variables.
Note:\t\tContents of ~/.rpnrc will be executed at the startup.
    """
    if ops:
        tools.show_ops()
    if eg:
        tools.show_examples()
    if verbose:
        tools.set_verbose()
    if base:
        tools.set_base(base)
    if mode:
        tools.set_mode(mode)

    # check if there ie ~/.rpnrc file and execute commands inside it
    tools.process_rpnrc()

    if (args):
        tools.command_line_mode(args)
    else:
        tools.interactive_mode()


if __name__ == '__main__':
    main()
