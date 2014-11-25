#!/usr/bin/env python3
import ast
import argparse


def parse(filename):
	with open(filename) as f:
		return ast.parse(f.read())

def parse_arguments():
	# create the argument parser
	parser = argparse.ArgumentParser()

	# add command option
	parser.add_argument("command", help="the command to run", )

if __name__ == '__main__':
	parsed = parse('testcode.py')
	print(parsed)
