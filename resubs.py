#!/usr/local/bin/python3
# coding=utf-8

# IMPORTS
# --------------
import argparse
import os
import socket
# --------------

# GLOBAL FUNCTIONS
# --------------

parser = argparse.ArgumentParser(description='Resubs Tool')

parser.add_argument("-f", "--file", help="Please give the url which you want to scan")
parser.add_argument("-w", "--wordlist", help="Please give the url which you want to scan")
parser.add_argument("-o", "--output", help="Please give the url which you want to scan")
parser.add_argument("-s", "--save", help="Please give the url which you want to scan")

args = parser.parse_args()

# -------------

# GLOBAL VARIABLE

os.system('clear')
file = args.file
wordlist = args.wordlist
output = args.output
save = args.save

# -------------

# COLORS
# --------------
red = '\33[31m'
cyan = '\33[36m'
green = '\33[32m'
white = '\33[0m'
yellow = '\33[33m'
blue = '\33[34m'


# --------------

# FUNCTIONS
# --------------


def logo():
    print(blue + """


 ██████  █████  ███████ ███████ ██ ███    ███     ██████  ███████ ███████ ██    ██ ██████  ███████ 
██      ██   ██ ██      ██      ██ ████  ████     ██   ██ ██      ██      ██    ██ ██   ██ ██      
██      ███████ █████   ███████ ██ ██ ████ ██     ██████  █████   ███████ ██    ██ ██████  ███████ 
██      ██   ██ ██           ██ ██ ██  ██  ██     ██   ██ ██           ██ ██    ██ ██   ██      ██ 
 ██████ ██   ██ ███████ ███████ ██ ██      ██     ██   ██ ███████ ███████  ██████  ██████  ███████ 
                                                                                                   
                                                                                                                                                                                               
===================================================================================================

    """ + white)


def resubs():
    with open(file, "r") as r, open(wordlist, "r") as a, open(output, "w") as ff:
        domains = r.read().splitlines()
        prefixes = a.read().splitlines()
        for p in prefixes:
            for d in domains:
                ff.write(f"{p}.{d}\n")
                print(f"{p}.{d}")


def nslookup():
    f = open(file, "w")
    with open(save, "r") as fp:
        line = fp.readline()

        while line:
            try:
                clean_line = line.strip()
                addr1 = socket.gethostbyname(clean_line)
                print("valid url : " + addr1 + " from " + clean_line)
                f.write(clean_line + "\n")

            except:
                clean_line = line.strip()
                print(clean_line + " is not valid")

            line = fp.readline()

    f.close()

    print("")
    print(green + """"### All Done! You will find your report in your chosen directory ###""" + white)


def main():
    if file is not None and wordlist is not None and output is not None:
        resubs()
    elif file is not None and save is not None:
        nslookup()
    elif file is not None and wordlist is not None and output is not None and save is not None:
        resubs()
        nslookup()
    else:
        logo()
        print(red + "[!] Type python3 resubs.py -h for help.")


# FUNCTIONS CALL
# --------------
if __name__ == '__main__':
    main()
# --------------
