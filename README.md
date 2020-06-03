# resubs

Tool written for BugBounty Hunter and Penetration Tester in oder to add words from a wordlist
as a subdomain and test it if they are reachable or not via nslookup!


# Installation:

```
git clone https://github.com/ca3s1m/resubs.git
```

```
cd resubs/
```

```
sudo pip3 install -r requirements.txt
```

# Usage:

```
python3 resubs.py -h
```
```
usage: resubs.py [-h] [-f FILE] [-w WORDLIST] [-o OUTPUT] [-s SAVE]

Resubs Tool

optional arguments:
  -h, --help                            show this help message and exit
  -f FILE, --file                       FILE  A file which contain subdomains
  -w WORDLIST, --wordlist WORDLIST      A file which contain certain words
  -o OUTPUT, --output OUTPUT            Where you want to save the resu`lts
  -s SAVE, --save SAVE                  Where you want to save the nslookup results
```

# Python Version:

```
requirement for using this script is python 3.*
```

# Contact:

```
Please feel free to contact me via twitter on https://twitter.com/HackingWhitehat
```
