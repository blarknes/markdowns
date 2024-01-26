# Magikarp Ground Mission

## Information

**Point Value**: 30 points  
**Category**: General Skills  
**Author**: SYREAL

## Description

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `ee388b88`

## Hints

1. Finding a cheatsheet for bash would be really helpful!

## Solution

To solve this one you will need to search through the folders of a virtual machine. So first things first, start the virtual machine and access it via the given ssh as **ctf-player** with the password **ee388b88**.

```sh
ssh ctf-player@venus.picoctf.net -p 57054
ctf-player@venus.picoctf.net password: ee388b88
```

Then, as the description stated, start with a **ls** command, this will give us the following result

```sh
$ ls
1of3.flag.txt  instructions-to-2of3.txt
```

In the ctf-player's repository there's two files, the first part of the flag and the instructions to get the second part. Cat into these files to the the following results.

```sh
$ cat 1of3.flag.txt
picoCTF{xxsh_

$ cat instructions-to-2of3.txt
Next, go to the root of all things, more succinctly `/`
```

Following the instructions of the **instructions-to-2of3.txt** file, we need to go to the root folder and see what's inside

```sh
$ cd /
$ ls
2of3.flag.txt  bin  boot  dev  etc  home  instructions-to-3of3.txt  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

Just repeating the process of looking what is inside the text files we get the second part of the flag and the instructions to get to the third part.

```sh
$ cat 2of3.flag.txt
0ut_0f_\/\/4t3r_
$ cat instructions-to-3of3.txt
Lastly, ctf-player, go home... more succinctly `~`
```

Now, following the instructions we just need to go to the home folder and we'll find the last part of the flag.

```sh
$ cd ~
$ ls
3of3.flag.txt  drop-in
$ cat 3of3.flag.txt
3ca613a1}
```

## Flag

picoCTF{xxsh*0ut_0f*\\/\\/4t3r_3ca613a1}
