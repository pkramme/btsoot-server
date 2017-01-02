#!/usr/bin/env python3.6


import os
import sys


try:
	from datatransfer import datalib
except ImportError:
	print("BTSOOT Server can try to load missing dependency. This requires an internet connection.")
	if input("Should i try? (y/N) ") == "y":
		os.system("git clone https://git.paukra.com/open-source/datatransfer.git")
	else:
		print("Abort. Install manually or restart the program.")
		exit()


def split(string, splitters): #MAY RESOLVE ALL PROBLEMS WITH CSV
	final = [string]
	for x in splitters:
		for i,s in enumerate(final):
			if x in s and x != s:
				left, right = s.split(x, 1)
				final[i] = left
				final.insert(i+1, x)
				final.insert(i+2, right)
	return final


def main():
	print("BTSOOT SERVER")
	while 1: #ENTERING MAIN LOOP FOR CONTINUOS USAGE
		print(":: Waiting for incoming connection...")
		datalib.receive("scanfile")
		print(":: Received scanfile.")
		with open("scanfile", "r") as scan:
			lines = scan.readlines()
			for line in lines:
				splitted_line = split(line, ",")
				if splitted_line[2] == None:
					os.mkdir(splitted_line[0]) #RECREATE DIRECTORY STRUCTURE
				elif splitted_line[2] == "error":
					pass
				elif splitted_line[2] == "permission_denied":
					pass
				else:
					filepath = split(splitted_line, "/")
					filepathlengh = len(filename)
					filename = filepath[filepathlengh]
					print(f"Creating file with name: {filename}")
					datalib.receive("/home/paul/btsoot/backup" + filepath)
		os.system("rm scanfile")



if __name__ == "__main__":
	main()
