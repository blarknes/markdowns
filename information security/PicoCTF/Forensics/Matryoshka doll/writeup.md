# Matryoshka doll

## Information

**Point Value**: 30 points  
**Category**: Forensics  
**Author**: SUSIE/PANDU

## Description

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](./dolls.jpg)

## Hints

1. Wait, you can hide files inside files? But how do you find them?
2. Make sure to submit the flag as picoCTF{XXXXX}

## Solution

The name of the challenge is the biggest hint, Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. So the catch is that there are files hidden inside files, and to achieve that, the most known way is to hide a .zip file in another extension. In this case the .jpg files are masked .zip files, so we can change the extension and get inside the folder. Doing so, we get another doll.jpg file, again and again.  
Because of that I wrote a python script to get the .jpg file, convert it to .zip and extract the folder.

```py
import os
from pathlib import Path
import zipfile

directory = "/path/to/your/folder/"
base_images = "base_images/"

while True:
    files = os.listdir(directory)
    print(files)

    if not any(".jpg" in x for x in files):
        break
    files = os.listdir(directory)

    for f in files:
        if (".jpg" in f):
            p = Path(directory + f)
            p.rename(p.with_suffix('.zip'))
            with zipfile.ZipFile(directory + f.replace(".jpg", ".zip"), 'r') as zip_ref:
                zip_ref.extractall(directory)

    directory += base_images
```

Doing so, you get 4 iterations of folders, and at the end of it there will be a flag.txt file with the flag inside of it.

## Flag

picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}
