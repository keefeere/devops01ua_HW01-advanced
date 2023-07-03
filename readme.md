# Passgen by KeeFeeRe(c)2023

Passgen is a Python script that generates a complex random passwords of a given length.

## Usage

To run the script, you need to have Python 3 installed on your system. You can download it from https://www.python.org/downloads/.

To execute the script, open a terminal or command prompt and navigate to the directory where the script is located. Then type:

```bash
python passgen.py
```

The script will prompt you to enter the desired length and amount of generated passwords. The amount must be an integer between 1 and 100. The complexity is predefined and match the following criteria:

- At least one Lowercase, one uppercase letter, one digits and one special character

The script will then generate and print a random passwords that meets the criteria. For example:

```bash
python passgen.py
Welcome to the Linux User Password Generator by KeeFeeRe!
Please enter the desired password length (between 6 and 255, default is 8): 12
Do you want to see the colored output? (Y/N(default)): n
How many passwords do you want to get?  (default is 1):3
Generating 3 password(s):

maQaqVu,5_Zd
eM1M9V8sfHW.
OwE1c7XM$1YI
```
