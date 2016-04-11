import sys
from contextlib import contextmanager

def reader():
	with sys.stdin as input:
		while True:
			yield input.readline()


@contextmanager
def writer():
	with sys.stdout as output:
		yield output
