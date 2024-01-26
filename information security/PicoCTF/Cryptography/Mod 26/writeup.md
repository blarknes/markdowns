# Mod 26

## Information

**Point Value**: 10 points  
**Category**: Criptography  
**Author**: PANDU

## Description

Cryptography can be easy, do you know what ROT13 is?  
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}

## Hints

1. This can be solved online if you don't want to do it by hand!

## Solution

The flag is encrypted with ROT13, to decrypt you may use one of many websites online, like [rot13.com](https://rot13.com/) for example. Or you may make your own decrypter, like the one below.

```py
import codecs
flag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"
print(codecs.encode(flag, 'rot_13'))
```

## Flag

picoCTF{next_time_I'll_try_2_rounds_of_rot13_wqWOSBKW}
