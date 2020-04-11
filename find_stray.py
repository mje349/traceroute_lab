'''
Author: Montana Esguerra
Filename: find_stray.py
Description: used for finding stray bits in my code
'''

with open("icmp_traceroute_v2.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)