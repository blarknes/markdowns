# Mind your Ps and Qs

## Information

**Point Value**: 20 points  
**Category**: Criptography  
**Author**: SARA

## Description

In RSA, a small e value can be problematic, but what about N? Can you decrypt this? [values](./values)

## Hints

1. Bits are expensive, I used only a little bit over 100 to save money

## Solution

[RSA (Rivest–Shamir–Adleman)](<https://en.wikipedia.org/wiki/RSA_(cryptosystem)>) is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. It is highly based on math and can be reversed easily with tools if the numbers are not too large.

Using the numbers provided to us on the [values](./values) file we can decode the flag. First step is to decompose the prime factors based on the **N** value.

There are many tools online, but I used [this one](https://www.dcode.fr/prime-factors-decomposition) because of personal preference, then save the results for further use:

```txt
N = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
N = P × Q
P = 2434792384523484381583634042478415057961
Q = 650809615742055581459820253356987396346063
```

After getting these values, we can get the flag, just need to properly address them to the fields on this [RSA decoder](https://www.dcode.fr/rsa-cipher) and the flag will be decoded.

```txt
VALUE OF THE CIPHER MESSAGE (INTEGER) C=
964354128913912393938480857590969826308054462950561875638492039363373779803642185

PUBLIC KEY E (USUALLY E=65537) E=
65537

PUBLIC KEY VALUE (INTEGER) N=
1584586296183412107468474423529992275940096154074798537916936609523894209759157543

PRIVATE KEY VALUE (INTEGER) D=
Don't need to fill this one

FACTOR 1 (PRIME NUMBER) P=
2434792384523484381583634042478415057961

FACTOR 2 (PRIME NUMBER) Q=
650809615742055581459820253356987396346063

INTERMEDIATE VALUE PHI (INTEGER) Φ=
Don't need to fill this one

DISPLAY=
PLAINTEXT AS CHARACTER STRING
```

## Flag

picoCTF{sma11_N_n0_g0od_73918962}
