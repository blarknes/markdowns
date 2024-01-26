# information

## Information

**Point Value**: 10 points  
**Category**: Forensics  
**Author**: SUSIE

## Description

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](./cat.jpg)

## Hints

1. Look at the details of the file
2. Make sure to submit the flag as picoCTF{XXXXX}

## Solution

Simply download the [cat.jpg](cat.jpg) file and run it through any metadata viewer (eg: [metadata2go](https://www.metadata2go.com/)). Copy the license which is encoded in base64, [decode](https://www.base64decode.org/) it and there you go.

## Flag

picoCTF{the_m3tadata_1s_modified}
