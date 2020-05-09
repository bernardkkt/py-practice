#!/usr/bin/env python3
import logging

class Hashes:
	def __init__(self):
		self.logger = logging.getLogger('decorator-log')
		return
    
	def print_ln(self, func):
		print("Hello")
		return
    
	@print_ln
	def base64(self):
		return

def main():
	return

if __name__ == "__main__":
	main()
