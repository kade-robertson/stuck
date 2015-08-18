# Standard I/O

There are a few ways of taking input in Stuck:

## String Input - `s`

This utilizes Python's `raw_input()` method to take input in the form of a string, and place it on the stop of the stack.

## Integer/Float/List/Etc Input - `i`

This utilizes Python's `input()` method to take input in any form that you would like, however strings taken in this format must be surrounded by quotes.

## Multiple Inputs - `t`

This takes input via `raw_input()` as a string, splits it by the delimeter `|`, and then evaluates each bit and places it on the stack in the order it was inputted.