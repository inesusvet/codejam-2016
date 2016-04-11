
from google import reader, writer


def number_to_jamcoin(number):
	return '{:b}'.format(number)


def make_jamcoin(length):
	return (1 << length - 1) + 1


def jamcoins(length):
	limit = 1 << length
	number = make_jamcoin(length)
	while number < limit:
		yield number
		number += 1 << 1


def find_divisor(number):
	i = 3
	while i < number:
		if number % i == 0:
			return i

		i += 1

	return False


def divisors(jamcoin):
	return map(
		lambda i: find_divisor(int(jamcoin, i)),
		xrange(2, 11),
	)


def main(length, number):
	collected = list()
	generator = jamcoins(length)
	while len(collected) < number:
		jamcoin = next(generator)
		result = divisors(number_to_jamcoin(jamcoin))
		if all(result):
			result = [number_to_jamcoin(jamcoin)] + result[:]
			collected.append(result)

	return collected


if __name__ == '__main__':
	input = reader()
	header = next(input)
	test_number = int(header.strip())
	case = 0
	with writer() as output:
		while case < test_number:
			case += 1
			length, number = map(int, next(input).strip().split())
			output.write('Case #%d:\n' % case)
			results = main(length, number)
			for result in results:
				output.write('%s\n' % ' '.join(map(str, result)))
