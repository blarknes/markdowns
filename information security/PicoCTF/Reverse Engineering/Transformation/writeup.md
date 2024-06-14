# Transformation

## Information

**Point Value**: 20 points  
**Category**: Reverse Engineering  
**Author**: MADSTACKS

## Description

I wonder what this really is... [enc](./files/enc) ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## Hints

1. You may find some decoders online

## Solution

Download the binary file, open it and you will find some chinese characters, it's some kind of problem with the encoding. I tried decoding for UTF-8 but with no success, so I tried encoding the flag common starting characters with the python code the exercise gave us.

```py
flag = "picoCTF{"
print(''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))
result: 灩捯䍔䙻
```

Comparing the result, we got the starting characters of that chinese string as the return, so I built an decoder in python and got the flag.

```py
ascii_table = "!@#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{|}~_"
char_map = []
encrypted_map = []
encrypted_flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"

for char1 in ascii_table:
    for char2 in ascii_table:
        flag = char1 + char2
        char_map.append(flag)
        encrypted_map.append(''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))

flag = ""
for char in encrypted_flag:
    flag += str(char_map[encrypted_map.index(char)])

print(flag)
```

## Flag

picoCTF{16_bits_inst34d_of_8_75d4898b}
