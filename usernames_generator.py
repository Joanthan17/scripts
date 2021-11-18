#!/bin/python3



""" 
 takes list of full names and create enteries of user names in "windows" style


 ex:
 john smith --> 
 				john smith
 				johnsmith
 				john.smith
 				jsmith
 				j.smith
 				smith john
 				smithjohn
 				smith.john
 				sjohn
 				s.john

"""
import sys

if len(sys.argv) != 2:
	print("Usage: 'python3 usernames_generator.py users.txt'") 

f = sys.argv[1]
with open(f, "r") as fi:
	lines = fi.readlines()

print("[-] creating multiple names from '" + f + "'...")
allnames = []
for line in lines:
	l = []
	first, last = line.strip("\n").split()
	l.append(first + " " +last)
	l.append(first + last)
	l.append(first + "." + last)
	l.append(first[0] + last)
	l.append(first[0] + "." + last)
	l.append(last + " " + first)
	l.append(last + first)
	l.append(last + "." + first)
	l.append(last[0] + first)
	l.append(last[0] + "." + first)
	allnames.extend(l)
	

new_f = f.strip(".txt") + "_extended.txt"	
with open(new_f, "w") as fi:
	for name in allnames:
		fi.write("%s\n" % name)

print("[+] action completed - '" + new_f + "' has been created")