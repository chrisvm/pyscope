#!/usr/bin/env python3
import ast 


def parse(filename):
	with open(filename) as f:
		return ast.parse(f.read())

if __name__ == '__main__':
	parsed = parse('testcode.py')
	print(parsed)
