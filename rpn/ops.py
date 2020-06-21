import operator
import math
import socket
import random
import secrets
import sys
import click
from . import settings
from .stack import stack
from collections import namedtuple


class Operations:
    """Class for all operator functions."""
    def ops(self):
        Operation = namedtuple(
            'op',
            ['op_function', 'op_type', 'op_description']
        )
        return {
            '+': Operation(
                op_function=self.add,
                op_type='arithmetic',
                op_description='Add 2 top numbers on the stack.'
            ),
            '-': Operation(
                op_function=self.sub,
                op_type='arithmetic',
                op_description='Subtract 2 top numbers on the stack.'
            ),
            '/': Operation(
                op_function=self.div,
                op_type='arithmetic',
                op_description='Divide 2 top numbers on the stack.'
            ),
            '*': Operation(
                op_function=self.mul,
                op_type='arithmetic',
                op_description='Multiply 2 top numbers on the stack.'
            ),
            '%': Operation(
                op_function=self.mod,
                op_type='arithmetic',
                op_description='Modulus 2 top numbers on the stack.'
            ),
            '++': Operation(
                op_function=self.increment,
                op_type='arithmetic',
                op_description='Increment top number on the stack.'
            ),
            '--': Operation(
                op_function=self.decrement,
                op_type='arithmetic',
                op_description='Decrement top number on the stack.'
            ),
            'ceil': Operation(
                op_function=self.ceil,
                op_type='numeric',
                op_description='Apply Ceiling to a top number on the stack.'
            ),
            'floor': Operation(
                op_function=self.floor,
                op_type='numeric',
                op_description='Apply Floor to a top number on the stack.'
            ),
            'round': Operation(
                op_function=self.round,
                op_type='numeric',
                op_description='Round off top number on the stack.'
            ),
            'ip': Operation(
                op_function=self.ip,
                op_type='numeric',
                op_description='Get Integer part from the top number on the stack.'
            ),
            'fp': Operation(
                op_function=self.fp,
                op_type='numeric',
                op_description='Get Fraction part from the top number on the stack.'
            ),
            'sign': Operation(
                op_function=self.sign,
                op_type='numeric',
                op_description='Copy sign from 1 number to next.'
            ),
            'abs': Operation(
                op_function=self.abs,
                op_type='numeric',
                op_description='Get Absolute value of the top number on the stack.'
            ),
            'max': Operation(
                op_function=self.max,
                op_type='numeric',
                op_description='Get the biggest number out of the 2 top numbers.'
            ),
            'min': Operation(
                op_function=self.min,
                op_type='numeric',
                op_description='Get the smallest number out of the 2.'
            ),
            'exp': Operation(
                op_function=self.exp,
                op_type='mathematic',
                op_description='Apply Exponentiation to a top number on the stack.'
            ),
            'fact': Operation(
                op_function=self.fact,
                op_type='mathematic',
                op_description='Apply Factorial to a top number on the stack.'
            ),
            'sqrt': Operation(
                op_function=self.sqrt,
                op_type='mathematic',
                op_description='Square Root top number on the stack.'
            ),
            'ln': Operation(
                op_function=self.nlog,
                op_type='mathematic',
                op_description='Apply Natural Logarithm to a top number on the stack.'
            ),
            'log': Operation(
                op_function=self.log,
                op_type='mathematic',
                op_description='Apply Logarithm to a top number of the stack.'
            ),
            'pow': Operation(
                op_function=self.pow,
                op_type='mathematic',
                op_description='Apply power to the top number on the stack'
            ),
            'sin': Operation(
                op_function=self.sin,
                op_type='trigonometric',
                op_description='Applies Sin to the top number of the stack.'
            ),
            'asin': Operation(
                op_function=self.asin,
                op_type='trigonometric',
                op_description='Applies Asin to the top number of the stack.'
            ),
            'sinh': Operation(
                op_function=self.sinh,
                op_type='trigonometric',
                op_description='Applies Sinh to the top number of the stack.'
            ),
            'asinh': Operation(
                op_function=self.asinh,
                op_type='trigonometric',
                op_description='Applies Asinh to the top number of the stack.'
            ),
            'cos': Operation(
                op_function=self.cos,
                op_type='trigonometric',
                op_description='Applies Cos to the top number of the stack.'
            ),
            'acos': Operation(
                op_function=self.acos,
                op_type='trigonometric',
                op_description='Applies Acos to the top number of the stack.'
            ),
            'cosh': Operation(
                op_function=self.cosh,
                op_type='trigonometric',
                op_description='Applies Cosh to the top number of the stack.'
            ),
            'acosh': Operation(
                op_function=self.acosh,
                op_type='trigonometric',
                op_description='Applies Acosh to the top number of the stack.'
            ),
            'tan': Operation(
                op_function=self.tan,
                op_type='trigonometric',
                op_description='Applies Tan to the top number of the stack.'
            ),
            'atan': Operation(
                op_function=self.atan,
                op_type='trigonometric',
                op_description='Applies Atan to the top number of the stack.'
            ),
            'tanh': Operation(
                op_function=self.tanh,
                op_type='trigonometric',
                op_description='Applies Tanh to the top number of the stack.'
            ),
            'atanh': Operation(
                op_function=self.atanh,
                op_type='trigonometric',
                op_description='Applies Atanh to the top number of the stack.'
            ),
            'pi': Operation(
                op_function=self.pi,
                op_type='constants',
                op_description='Puts the PI constant on top of the stack.'
            ),
            'e': Operation(
                op_function=self.e,
                op_type='constants',
                op_description='Puts the E constant on top of the stack.'
            ),
            'rand': Operation(
                op_function=self.rand,
                op_type='random',
                op_description='Puts a random number on top of the stack.'
            ),
            '&': Operation(
                op_function=self.bit_and,
                op_type='bitwise',
                op_description='Performs Bitwise AND on 2 top numbers on the stack.'
            ),
            '|': Operation(
                op_function=self.bit_or,
                op_type='bitwise',
                op_description='Performs Bitwise OR on 2 top numbers on the stack.'
            ),
            '^': Operation(
                op_function=self.bit_xor,
                op_type='bitwise',
                op_description='Performs Bitwise XOR on 2 top numbers on the stack.'
            ),
            '~': Operation(
                op_function=self.bit_not,
                op_type='bitwise',
                op_description='Performs Bitwise NOT on 2 top numbers on the stack.'
            ),
            '>>': Operation(
                op_function=self.bit_rshift,
                op_type='bitwise',
                op_description='Performs Bitwise Right Shift on 2 top numbers on the stack.'
            ),
            'rshft': Operation(
                op_function=self.bit_rshift,
                op_type='bitwise',
                op_description='Performs Bitwise Right Shift on 2 top numbers on the stack.'
            ),
            '<<': Operation(
                op_function=self.bit_lshift,
                op_type='bitwise',
                op_description='Performs Bitwise Left Shift on 2 top numbers on the stack.'
            ),
            'lshft': Operation(
                op_function=self.bit_lshift,
                op_type='bitwise',
                op_description='Performs Bitwise Left Shift on 2 top numbers on the stack.'
            ),
            '&&': Operation(
                op_function=self.bool_and,
                op_type='boolean',
                op_description='Performs Boolean AND on 2 top numbers on the stack.'
            ),
            'and': Operation(
                op_function=self.bool_and,
                op_type='boolean',
                op_description='Performs Boolean AND on 2 top numbers on the stack.'
            ),
            '||': Operation(
                op_function=self.bool_or,
                op_type='boolean',
                op_description='Performs Boolean OR on 2 top numbers on the stack.'
            ),
            'or': Operation(
                op_function=self.bool_or,
                op_type='boolean',
                op_description='Performs Boolean OR on 2 top numbers on the stack.'
            ),
            '!': Operation(
                op_function=self.bool_not,
                op_type='boolean',
                op_description='Performs Boolean NOT on 2 top numbers on the stack.'
            ),
            'not': Operation(
                op_function=self.bool_not,
                op_type='boolean',
                op_description='Performs Boolean NOT on 2 top numbers on the stack.'
            ),
            '^^': Operation(
                op_function=self.bool_xor,
                op_type='boolean',
                op_description='Performs Boolean XOR on 2 top numbers on the stack.'
            ),
            'less': Operation(
                op_function=self.less,
                op_type='comparison',
                op_description='Applies "<" logic on 2 top numbers on the stack.'
            ),
            '<': Operation(
                op_function=self.less,
                op_type='comparison',
                op_description='Applies "<" logic on 2 top numbers on the stack.'
            ),
            'lesseq': Operation(
                op_function=self.less_equals,
                op_type='comparison',
                op_description='Applies "<=" logic on 2 top numbers on the stack.'
            ),
            '<=': Operation(
                op_function=self.less_equals,
                op_type='comparison',
                op_description='Applies "<=" logic on 2 top numbers on the stack.'
            ),
            '==': Operation(
                op_function=self.equals,
                op_type='comparison',
                op_description='Applies "==" logic on 2 top numbers on the stack.'
            ),
            'eq': Operation(
                op_function=self.equals,
                op_type='comparison',
                op_description='Applies "==" logic on 2 top numbers on the stack.'
            ),
            '!=': Operation(
                op_function=self.not_equals,
                op_type='comparison',
                op_description='Applies "!=" logic on 2 top numbers on the stack.'
            ),
            'neq': Operation(
                op_function=self.not_equals,
                op_type='comparison',
                op_description='Applies "!=" logic on 2 top numbers on the stack.'
            ),
            '>': Operation(
                op_function=self.more,
                op_type='comparison',
                op_description='Applies ">" logic on 2 top numbers on the stack.'
            ),
            'more': Operation(
                op_function=self.more,
                op_type='comparison',
                op_description='Applies ">" logic on 2 top numbers on the stack.'
            ),
            '>=': Operation(
                op_function=self.more_equals,
                op_type='comparison',
                op_description='Applies ">=" logic on 2 top numbers on the stack.'
            ),
            'moreeq': Operation(
                op_function=self.more_equals,
                op_type='comparison',
                op_description='Applies ">=" logic on 2 top numbers on the stack.'
            ),
            'hnl': Operation(
                op_function=self.hnl,
                op_type='networking',
                op_description='Convert Host to network long.'
            ),
            'hns': Operation(
                op_function=self.hns,
                op_type='networking',
                op_description='Convert Host to network short.'
            ),
            'nhl': Operation(
                op_function=self.nhl,
                op_type='networking',
                op_description='Convert Network to host long.'
            ),
            'nhs': Operation(
                op_function=self.nhs,
                op_type='networking',
                op_description='Convert Network to host short.'
            ),
            'pick': Operation(
                op_function=self.pick,
                op_type='stack',
                op_description='Pick the -nth item from the stack.'
            ),
            'depth': Operation(
                op_function=self.depth,
                op_type='stack',
                op_description='Push the current stack depth.'
            ),
            'drop': Operation(
                op_function=self.drop,
                op_type='stack',
                op_description='Drops the top item from the stack.'
            ),
            'dropn': Operation(
                op_function=self.dropn,
                op_type='stack',
                op_description='Drops n items from the stack.'
            ),
            'dup': Operation(
                op_function=self.dup,
                op_type='stack',
                op_description='Duplicates the top stack item.'
            ),
            'dupn': Operation(
                op_function=self.dupn,
                op_type='stack',
                op_description='Duplicates the top n stack items in order.'
            ),
            'roll': Operation(
                op_function=self.roll,
                op_type='stack',
                op_description='Roll the stack upwards by n.'
            ),
            'rolld': Operation(
                op_function=self.rolld,
                op_type='stack',
                op_description='Roll the stack downwards by n.'
            ),
            'swap': Operation(
                op_function=self.swap,
                op_type='stack',
                op_description='Swap the top 2 stack items'
            ),
            'cla': Operation(
                op_function=self.cla,
                op_type='stack',
                op_description='Clear stack and variables.'
            ),
            'clr': Operation(
                op_function=self.clr,
                op_type='stack',
                op_description='Clear stack.'
            ),
            'clv': Operation(
                op_function=self.clv,
                op_type='stack',
                op_description='Clear variables.'
            ),
            'repeat': Operation(
                op_function=self.repeat,
                op_type='extra',
                op_description='Repeat next operation number of times.'
            ),
            'stack': Operation(
                op_function=self.toggle_stack,
                op_type='extra',
                op_description='Toggle stack display mode. Horizontal (default) or Vertical.'
            ),
            'mode': Operation(
                op_function=self.toggle_stack,
                op_type='extra',
                op_description='Toggle stack display mode. Horizontal (default) or Vertical.'
            ),
            'verbose': Operation(
                op_function=self.toggle_verbose,
                op_type='extra',
                op_description='Toggle verbose mode.'
            ),
            'debug': Operation(
                op_function=self.toggle_verbose,
                op_type='extra',
                op_description='Toggle verbose mode.'
            ),
            'dbg': Operation(
                op_function=self.toggle_verbose,
                op_type='extra',
                op_description='Toggle verbose mode.'
            ),
            'vars': Operation(
                op_function=self.show_vars,
                op_type='extra',
                op_description='Show current variables.'
            ),
            'binary': Operation(
                op_function=self.toggle_bin,
                op_type='extra',
                op_description='Toggle binary mode.'
            ),
            'bin': Operation(
                op_function=self.toggle_bin,
                op_type='extra',
                op_description='Toggle binary mode.'
            ),
            'octal': Operation(
                op_function=self.toggle_oct,
                op_type='extra',
                op_description='Toggle octal mode.'
            ),
            'oct': Operation(
                op_function=self.toggle_oct,
                op_type='extra',
                op_description='Toggle octal mode.'
            ),
            'decimal': Operation(
                op_function=self.toggle_dec,
                op_type='extra',
                op_description='Show decimal mode.'
            ),
            'hexadecimal': Operation(
                op_function=self.toggle_hex,
                op_type='extra',
                op_description='Show hexadecimal mode.'
            ),
            'hex': Operation(
                op_function=self.toggle_hex,
                op_type='extra',
                op_description='Show hexadecimal mode.'
            ),
            'macro': Operation(
                op_function=None,
                op_type='extra',
                op_description=
                'Store a Macro inside a variable. Available only in interactive mode. Eg. macro mcr_name 1 2 +'
            ),
            'var=': Operation(
                op_function=None,
                op_type='extra',
                op_description=
                'Store the number on top of the stack into "var" variable. Available only in interactive mode. Eg. some_var='
            ),
            'exit': Operation(
                op_function=self.exit,
                op_type='extra',
                op_description='Exit interactive mode.'
            ),
            'quit': Operation(
                op_function=self.exit,
                op_type='extra',
                op_description='Exit interactive mode.'
            ),
        }

    def show_ops(self):
        """Show all available operations."""
        current_section = None
        click.echo()
        click.echo('AVAILABLE OPERATORS.')
        for k, v in self.ops().items():
            if current_section != v.op_type:
                click.echo(f'\n{v.op_type.capitalize()} Operators')
                click.echo('=' * 79)
                current_section = v.op_type
            click.echo(f'{k}\t: {v.op_description}')
        click.echo()

    def is_operator(self, s):
        return s in self.ops()

    def clr(self):
        """Clear stack."""
        stack.clear()

    def clv(self):
        """Clear variables and macros."""
        settings.vars.clear()

    def cla(self):
        """Clear stack, variables and macros."""
        self.clr()
        self.clv()

    def run_op(self, op_name, op_func, num_of_args=2, push=True):
        if stack.size() < num_of_args:
            return None
        try:
            if (num_of_args == 1):
                a = stack.pop()
                x = op_func(a)
            elif (num_of_args == 2):
                b, a = stack.pop(), stack.pop()
                x = op_func(a, b)
            else:
                x = op_func()
            if push:
                stack.push(x)
        except:
            if settings.verbose:
                click.echo(f'{op_name}() filed.')

    def add(self):
        """a + b"""
        self.run_op(op_name='add', op_func=lambda a, b: a+b)

    def sub(self):
        """a - b"""
        self.run_op(op_name='sub', op_func=lambda a, b: a-b)

    def div(self):
        """a / b"""
        self.run_op(op_name='div', op_func=lambda a, b: a/b)

    def mul(self):
        """a * b"""
        self.run_op(op_name='mul', op_func=lambda a, b: a*b)

    def mod(self):
        """a % b"""
        self.run_op(op_name='mod', op_func=lambda a, b: a%b)

    def increment(self):
        """a++"""
        self.run_op(op_name='increment', op_func=lambda a: a+1, num_of_args=1)

    def decrement(self):
        """a--"""
        self.run_op(op_name='decrement', op_func=lambda a: a-1, num_of_args=1)

    def not_equals(self):
        """a != b"""
        self.run_op(op_name='not_equals', op_func=lambda a, b: 1 if a!=b else 0)

    def bit_and(self):
        """a & b"""
        self.run_op(op_name='bit_and', op_func=operator.and_)

    def bit_or(self):
        """a | b"""
        self.run_op(op_name='bit_or', op_func=operator.or_)

    def bit_xor(self):
        """a ^ b"""
        self.run_op(op_name='bit_xor', op_func=operator.xor)

    def bit_not(self):
        """a ~ b"""
        self.run_op(op_name='bit_not', num_of_args=1, op_func=operator.invert)

    def bit_rshift(self):
        """a >> b"""
        self.run_op(op_name='bit_rshift', op_func=operator.rshift)

    def bit_lshift(self):
        """a << b"""
        self.run_op(op_name='bit_lshift', op_func=operator.lshift)

    def bool_and(self):
        """a and b"""
        self.run_op(op_name='bool_and', op_func=lambda a, b: 1 if a and b else 0)

    def bool_or(self):
        """a or b"""
        self.run_op(op_name='bool_or', op_func=lambda a, b: 1 if a or b else 0)

    def bool_not(self):
        """not a"""
        self.run_op(op_name='bool_not', op_func=lambda a: 1 if not a else 0, num_of_args=1)

    def bool_xor(self):
        """bool(a) ^ bool(b)"""
        self.run_op(op_name='bool_xor', op_func=lambda a, b: operator.xor(bool(a), bool(b)))

    def less(self):
        """a < b"""
        self.run_op(op_name='less', op_func=lambda a, b: 1 if a<b else 0)

    def less_equals(self):
        """a <= b"""
        self.run_op(op_name='less_equals', op_func=lambda a, b: 1 if a<=b else 0)

    def equals(self):
        """a == b"""
        self.run_op(op_name='equals', op_func=lambda a, b: 1 if a==b else 0)

    def more(self):
        """a > b"""
        self.run_op(op_name='more', op_func=lambda a, b: 1 if a>b else 0)

    def more_equals(self):
        """a >= b"""
        self.run_op(op_name='more_equals', op_func=lambda a, b: 1 if a>=b else 0)

    def sin(self):
        """sin(a)"""
        self.run_op(op_name='sin', op_func=math.sin, num_of_args=1)

    def asin(self):
        """asin(a)"""
        self.run_op(op_name='asin', op_func=math.asin, num_of_args=1)

    def sinh(self):
        """sinh(a)"""
        self.run_op(op_name='sinh', op_func=math.sinh, num_of_args=1)

    def asinh(self):
        """asinh(a)"""
        self.run_op(op_name='asinh', op_func=math.asinh, num_of_args=1)

    def cos(self):
        """cos(a)"""
        self.run_op(op_name='cos', op_func=math.cos, num_of_args=1)

    def acos(self):
        """acos(a)"""
        self.run_op(op_name='acos', op_func=math.acos, num_of_args=1)

    def cosh(self):
        """cosh(a)"""
        self.run_op(op_name='cosh', op_func=math.cosh, num_of_args=1)

    def acosh(self):
        """acosh(a)"""
        self.run_op(op_name='acosh', op_func=math.acosh, num_of_args=1)

    def tan(self):
        """tan(a)"""
        self.run_op(op_name='tan', op_func=math.tan, num_of_args=1)

    def atan(self):
        """atan(a)"""
        self.run_op(op_name='atan', op_func=math.atan, num_of_args=1)

    def tanh(self):
        """tanh(a)"""
        self.run_op(op_name='tanh', op_func=math.tanh, num_of_args=1)

    def atanh(self):
        """atanh(a)"""
        self.run_op(op_name='atanh', op_func=math.atanh, num_of_args=1)

    def ceil(self):
        """ceil(a)"""
        self.run_op(op_name='ceil', op_func=math.ceil, num_of_args=1)

    def floor(self):
        """floor(a)"""
        self.run_op(op_name='floor', op_func=math.floor, num_of_args=1)

    def round(self):
        """round(a)"""
        self.run_op(op_name='round', op_func=round, num_of_args=1)

    def ip(self):
        """integer part of a"""
        self.run_op(op_name='ip', op_func=lambda a: math.modf(float(a))[1], num_of_args=1)

    def fp(self):
        """fraction part of a"""
        self.run_op(op_name='fp', op_func=lambda a: math.modf(float(a))[0], num_of_args=1)

    def sign(self):
        """copy sign from a to b"""
        self.run_op(op_name='sign', op_func=math.copysign)

    def abs(self):
        """Absolute value of a"""
        self.run_op(op_name='abs', op_func=abs, num_of_args=1)

    def max(self):
        """max(a, b)"""
        self.run_op(op_name='max', op_func=max)

    def min(self):
        """min(a, b)"""
        self.run_op(op_name='min', op_func=min)

    def pi(self):
        """PI constant"""
        self.run_op(op_name='pi', op_func=lambda: math.pi, num_of_args=0)

    def e(self):
        """E constant"""
        self.run_op(op_name='e', op_func=lambda: math.e, num_of_args=0)

    def rand(self):
        """Random number"""
        self.run_op(op_name='rand', op_func=lambda: secrets.SystemRandom().random(), num_of_args=0)

    def exp(self):
        """Exponentiation of a"""
        self.run_op(op_name='exp', op_func=math.exp, num_of_args=1)

    def fact(self):
        """Factorial of a"""
        self.run_op(op_name='fact', op_func=math.factorial, num_of_args=1)

    def sqrt(self):
        """Square root of a"""
        self.run_op(op_name='sqrt', op_func=math.sqrt, num_of_args=1)

    def nlog(self):
        """Natural logarithm of a"""
        self.run_op(op_name='nlog', op_func=lambda a, b: math.log2(a) if b==2 else (math.log10(a) if b==10 else math.log(a, b)))

    def log(self):
        """Logarithm of a"""
        self.run_op(op_name='log', op_func=math.log10, num_of_args=1)

    def pow(self):
        """a to the power of b"""
        self.run_op(op_name='pow', op_func=math.pow)

    def hnl(self):
        """Host to network long"""
        self.run_op(op_name='hnl', op_func=lambda a: socket.htonl(int(a)), num_of_args=1)

    def hns(self):
        """Host to network short"""
        self.run_op(op_name='hns', op_func=lambda a: socket.htons(int(a)), num_of_args=1)

    def nhl(self):
        """Network to host long"""
        self.run_op(op_name='nhl', op_func=lambda a: socket.ntohl(int(a)), num_of_args=1)

    def nhs(self):
        """Network to host short"""
        self.run_op(op_name='nhs', op_func=lambda a: socket.htons(int(a)), num_of_args=1)

    def pick(self):
        """Pick the -ath item from the stack"""
        self.run_op(op_name='pick', op_func=stack.pick, num_of_args=1, push=False)

    def depth(self):
        """Push the current stack depth"""
        try:
            stack.depth()
        except:
            if settings.verbose:
                click.echo(f'depth() filed.')

    def drop(self):
        """Drops the top item from the stack"""
        try:
            stack.drop()
        except:
            if settings.verbose:
                click.echo(f'drop() filed.')

    def dropn(self):
        """Drops n items from the stack"""
        self.run_op(op_name='dropn', op_func=stack.drop, num_of_args=1, push=False)

    def dup(self):
        """Duplicates the top stack item"""
        try:
            stack.dup()
        except:
            if settings.verbose:
                click.echo(f'dup() filed.')

    def dupn(self):
        """Duplicates the top n stack items in order."""
        self.run_op(op_name='dupn', op_func=stack.dup, num_of_args=1, push=False)

    def roll(self):
        """Roll the stack upwards by a."""
        self.run_op(op_name='roll', op_func=stack.roll, num_of_args=1, push=False)

    def rolld(self):
        """Roll the stack downwards by a."""
        self.run_op(op_name='rolld', op_func=stack.rolld, num_of_args=1, push=False)

    def swap(self):
        """Swap the top 2 stack items."""
        try:
            stack.swap()
        except:
            if settings.verbose:
                click.echo(f'swap() filed.')

    def toggle_stack(self):
        """Toggle between horizotal stack view and vertical stack view."""
        if settings.stack_mode == 'h':
            settings.stack_mode = 'v'
        else:
            settings.stack_mode = 'h'

    def toggle_verbose(self):
        """Toggle verbose mode."""
        settings.verbose = not settings.verbose

    def toggle_bin(self):
        """Toggle binary mode."""
        settings.base = 'b'

    def toggle_oct(self):
        """Toggle octal mode."""
        settings.base = 'o'

    def toggle_dec(self):
        """Toggle decimal mode."""
        settings.base = 'd'

    def toggle_hex(self):
        """Toggle hexadecimal mode."""
        settings.base = 'x'

    def repeat(self):
        """Set the repeat var. Following ops will be repeated n times."""
        if stack.size() < 1:
            return None
        try:
            n = stack.pop()
            settings.repeat = n
        except:
            if settings.verbose:
                click.echo(f'repeat() filed.')

    def show_vars(self):
        """Show all saved variables. Alternative to having a debug mode on."""
        click.echo(settings.vars)

    def exit(self):
        """Exit the app."""
        sys.exit()


ops = Operations()
