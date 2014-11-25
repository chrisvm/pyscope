#!/usr/bin/env python3
import ast
import argparse
import json 
import constants
import imp 


#TODO: add the implemented commands to the argumentparser

def parse(filename):
	with open(filename) as f:
		return ast.parse(f.read())

class CommandNotFound(Exception):
	def __init__(self):
		pass 

def parse_arguments():
	# create the argument parser
	parser = argparse.ArgumentParser()

	# add command option
	parser.add_argument("command", help="the command to run")

	# get the command
	command = parser.parse_args().command

	# parse the config
	with open(constants.config) as f: 	
		conf = json.loads(f.read())

	# get the command 
	command_obj = None
	for comm in conf['commands']:
		if comm == command:
			command_obj = conf['commands'][comm]
			break 

	# if command not found, show error 
	if not command_obj:
		raise CommandNotFound()
	else:
		# run the command
		filename = command_obj['filename']
		mod = imp.load_module(filename=filename, name=comm,
							  file=open(filename), details=('', 'r', imp.PY_SOURCE))
		mod.main()

def main():
	print(parse_arguments())

if __name__ == '__main__':
	main()