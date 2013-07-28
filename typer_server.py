#!/usr/bin/env python
import twitter

def get_consumer_key_secret():
	with open('.APIKEY','r') as f:
		return f.read().split('\n')

def main():
	print get_consumer_key_secret()
	pass

if __name__ == '__main__':
	main()
