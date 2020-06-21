# REVERSE POLISH NOTATION CALCULATOR

RPN - the Reverse Polish Notation CLI calculator.

## Installation


```bash
pipenv shell
pipenv install .
```

## Usage

```bash
rpn --help                - view help screen
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
```


## Author
[James La Guma](https://www.linkedin.com/in/jlaguma/)