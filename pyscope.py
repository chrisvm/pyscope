#!/usr/bin/env python3
import ast
import argparse
import json
import common
import imp


class CommandNotFound(Exception):
	def __init__(self):
		pass

def run_command():
	# create the argument parser
	parser = argparse.ArgumentParser()

	# add command option
	parser.add_argument("command", help="the command to run")

	# get the command
	command = parser.parse_args().command

	# get the config 
	conf = common.config()

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
	run_command()

if __name__ == '__main__':
	main()
