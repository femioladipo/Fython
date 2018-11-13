# Fython

Femi's Compiler written in Python2

## Usage

```bash
python2 interpeter.py yourfile
```

## Examples

### Example 1:

Prints out 9, by storing 4 then 5, then adding them, and printing the result.

```
// Single Line Comment
INT 4
INT 5
ADD // 9 is stored in memory
PRINT // 9 is popped and printed to screen
```

### Example 2:

Prints numbers 100 to 0.

```
INT 100
CALL 4
JGE 1
EXIT
INT 1
SWAP
SUB
PRINT
SWAP
RET
```

### Example 3:

Prints fibanacci number for 45.

```
INT 45
CALL 11
PRINT
EXIT
SWAP // F(0)
RET
POP // F(1)
POP
INT 1
SWAP
RET
SWAP // F(x)
JEQ 4 // do F(0)
DUP
INT 1
SUB
JEQ 6 // do F(1)
CALL 11 // call F(x - 1)
SWAP
INT 1
SUB
INT 1
SUB
CALL 11 // call F(x - 2)
ADD
SWAP
RET
```
