# keygenme-py

## Information

**Point Value**: 30 points  
**Category**: Reverse Engineering  
**Author**: SYREAL

## Description

[keygenme-trial.py](./files/keygenme-trial.py)

## Hints

- (None)

## Solution

After downloading the [keygenme-trial.py](./files/keygenme-trial.py) file, doing a basic overview, we're able to identify that the application has almost the full key hardcoded, so let's take note of it. Also, there's a graphical interface, in which we have an option to unlock the **full version code**.  
Following the path of this option in the code, we get to a function called **enter_license**, where a validation is made to check the inputed key inside the **check_key** function.

The first validation made is the size compare between the user inputed key and the placeholder key in the code, knowing this, we just need to input a key of the same size (32). After this, there's a validation to compare if the 23 first characters are the same in both strings.  
Lastly, there's a comparation of the last 8 characters based on the trial username. To decode the remaining part of the key we just need to know what the compared characters are, a way to do so is with the following snippet of code that displays the flag for us.

```py
import hashlib

username_trial = b"SCHOFIELD"

key = (
hashlib.sha256(username_trial).hexdigest()[4],
hashlib.sha256(username_trial).hexdigest()[5],
hashlib.sha256(username_trial).hexdigest()[3],
hashlib.sha256(username_trial).hexdigest()[6],
hashlib.sha256(username_trial).hexdigest()[2],
hashlib.sha256(username_trial).hexdigest()[7],
hashlib.sha256(username_trial).hexdigest()[1],
hashlib.sha256(username_trial).hexdigest()[8])

key = ''.join(key)

print("picoCTF{1n_7h3_|<3y_of_" + key + "}")
```

Inserting this flag in the main application generates a new file called [keygenme.py](./files/keygenme.py) that has a cool reference to the Tron franchise when you run it.

## Flag

picoCTF{1n*7h3*|<3y_of_e584b363}
