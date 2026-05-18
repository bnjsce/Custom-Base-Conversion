import sys, os
import math
import time

def clear() -> None:
	'''
	Clears the screen using OS.
	'''
	os.system('cls' if os.name=='nt' else 'clear')

def main() -> None:
	'''
	Main menu
	'''
	clear()
	print('MAIN MENU \n ------------------------')
	print('1) Base-x to denary')
	print('2) Denary to base-x')
	print('3) Base-x to base-x')
	print('4) Exit')
	print('------------------------')
	user = input('>>> ').replace(' ', '').lower()

	if user == '1':
		clear()
		n = input('Number to be converted: ').upper()
		try:
			b = int(input('Base from which to be converted: '))
		except ValueError:
			print('Base-x must be an whole integer. Please try again...')
			time.sleep(0.8)
			main()

		if b < 2 or b > 26:
			print('Base-x must be between 2 and 26 (inclusive). Please try again...')
			time.sleep(0.8)
			main()

		clear()
		result = custom_base_to_denary(n, b)
		if result == -99:
			print('Invalid conversion. Please try again...')
			time.sleep(0.8)
			main()
		print(f'{n} (base-{b}): {result} (base-10)')
		input('\nPress enter to continue...')
		main()

	elif user == '2':
		clear()
		try:
			n = int(input('Number to be converted: '))
			b = int(input('Base to be converted to: '))
		except ValueError:
			print('Base-x and conversion number must be whole integers. Please try again...')
			time.sleep(0.8)
			main()

		if b < 2 or b > 26:
			print('Base-x must be between 2 and 26 (inclusive). Please try again...')
			time.sleep(0.8)
			main()

		clear()
		result = denary_to_custom_base(n, b)
		try:
			result = int(result)
		except ValueError:
			print(result)
			time.sleep(0.8)
			main()
		print(f'{n} (base-10): {result} (base-{b})')
		input('\nPress enter to continue...')
		main()
	elif user == '3':
		clear()
		n1 = input('Number to be converted: ').upper()
		try:
			b1 = int(input('Original base: '))
			b2 = int(input('New base: '))
		except ValueError:
			print('Base-x must be an whole integer. Please try again...')
			time.sleep(0.8)
			main()

		if b1 < 2 or b1 > 26 or b2 < 2 or b2 > 26:
			print('Base-x must be between 2 and 26 (inclusive). Please try again...')
			time.sleep(0.8)
			main()

		clear()
		n2 = denary_to_custom_base(custom_base_to_denary(n1, b1), b2)
		try:
			n2 = int(n2)
		except ValueError:
			print(n2)
			time.sleep(0.8)
			main()
		print(f'{n1} (base-{b1}): {n2} (base-{b2})')
		input('\nPress enter to continue...')
		main()
	elif user == '4':
		exit()
	else:
		print('Invalid option. Please try again...')
		time.sleep(0.8)
		main()

def custom_base_to_denary(n, b) -> int:
	'''
	Convert a custom base (2 - 26 incl.) to denary (base-10).

	Parameters:
	n (str): Number to be converted.
	b (int): Base from which to be converted.

	Returns:
	total (int): Denary conversion of inputted number. If it returns -99, there is an error.
	'''
	total = 0
	max_unit = b - 1
	for i in range(len(n)):
		idx = len(n) - i - 1
		val = n[idx]
		try:
			val = int(n[idx])
			if val > max_unit:
				return -99
		except:
			val = ord(n[idx]) - 55
			if val > 35 or val < 10 or val > max_unit:
				return -99
		total += val * (b ** i)
	return int(total)

def denary_to_custom_base(n, b) -> str:
	'''
	Convert denary (base-10) to a custom base (2 - 26 incl.)

	Parameters:
	n (int): Denary number to be converted.
	b (int): Custom base to be converted to.

	Returns:
	rtn (str): Custom base conversion from inputted denary number.
	'''
	max_idx = 0
	try:
		max_idx = math.floor(math.log(n, b))
	except ValueError:
		return f'Invalid value for base-{b}. Please try again...'
	max_unit = b - 1
	total = n
	rtn = ''

	if n < b:
		return 'The conversion number cannot be lower than the base. Please try again...'
	
	for i in range(max_idx, -1, -1):
		mult = b ** i
		val = max_unit
		while val * mult > total:
			val -= 1
		total -= val * mult
		if val > 9:
			val = chr(val + 55)
		rtn += str(val)

	return rtn

main()