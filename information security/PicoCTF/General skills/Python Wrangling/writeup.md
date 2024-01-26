# Python Wrangling

## Information

**Point Value**: 10 points  
**Category**: General Skills  
**Author**: SYREAL

## Description

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](./ende.py) using [this password](./pw.txt) to get [the flag](./flag.txt.en)?

## Hints

1. Get the Python script accessible in your shell by entering the following command in the Terminal prompt: $ wget [https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/ende.py](https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/ende.py)
2. $ man python

## Solution

Download all the files, then open up a terminal and go to the selected folder, then use the following command:

```sh
$ ende.py -d flag.txt.en
```

Then the program will ask your for a password, you can find it inside the [pw.txt](./pw.txt) file, insert it and you're good to go.

## Flag

picoCTF{4p0110_1n_7h3_h0us3_192ee2db}
