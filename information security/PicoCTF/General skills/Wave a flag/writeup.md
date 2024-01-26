# Wave a flag

## Information

**Point Value**: 10 points  
**Category**: General Skills  
**Author**: SYREAL

## Description

Can you invoke help flags for a tool or binary? [This program](./warm) has extraordinarily helpful information..

## Hints

1. This program will only work in the webshell or another Linux computer.
2. To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget [https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm](https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm)
3. Run this program by entering the following in the Terminal prompt: \$ ./warm, but you'll first have to make it executable with \$ chmod +x warm
4. -h and --help are the most common arguments to give to programs to get more information from them!
5. Not every program implements help features like -h and --help.

## Solution

Download the [warm](./warm) file, then open a terminal and browse to the file location, run the following commands and you will get to the flag.

```sh
$ chmod +x warm
$ ./warm
$ ./warm -h
```

## Flag

picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
