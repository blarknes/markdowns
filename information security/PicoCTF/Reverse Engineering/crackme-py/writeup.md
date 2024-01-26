# crackme-py

## Information

**Point Value**: 30 points  
**Category**: Reverse Engineering  
**Author**: SYREAL

## Description

[crackme.py](./crackme.py)

## Hints

- (None)

## Solution

This one is pretty straightforward, download and open the [crackme.py](./crackme.py) file, and run the following snippet at the end of the code.

```py
decode_secret(bezos_cc_secret)
```

This will access the ROT47 decoding function and will give us the flag.

## Flag

picoCTF{1|\/|\_4_p34|\|ut_502b984b}
