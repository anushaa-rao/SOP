
import Crypto.Util.number
from Crypto.Util.number import bytes_to_long 
from Crypto.Util.number import long_to_bytes


def lcm(num1: int, num2: int) -> int:
	return (num1 * num2) // gcd(num1, num2)

def gcd(num1: int, num2: int) -> int:
	if num1 == 0:
		return num2
	else:
		return gcd(num2 % num1, num1)


def extended_gcd(num1: int, num2: int):
	old_r, r = num1, num2
	old_s, s = 1, 0
	old_t, t = 0, 1

	while (r != 0):
		quotient = old_r // r
		old_r, r = r, old_r - quotient * r
		old_s, s = s, old_s - quotient * s 
		old_t, t = t, old_t - quotient * t

	return old_s, old_t

def mul_inverse(num1: int, num2: int) -> int:
	s, t = extended_gcd(num1, num2)
	return s % num2


def encrpytRSA(m: int, bits: int):

	# # Randomly generated 256 bit prime numbers
	# p = 139047819728230194775529933261539665563
	# q = 614411440986309041176911847787988986873

	p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
	q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
	
	n = p * q


	# Find carmichael totient of n, which is lcm(p - 1, q - 1)
	carmichael_totient = lcm(p - 1, q - 1)
	
	# Choose an exponent such that gcd(e, carmichael totient) is 1

	e = 65537
	# assert(gcd(e, carmichael_totient) == 1)

	d = mul_inverse(e, carmichael_totient)
	c = pow(m, e, n)
	return n, e, c, d

def decryptRSA(c: int, d: int, n: int):
	return pow(c, d, n)


def main():

	print("Please provide plaintext")
	plaintext = bytes(input(), 'utf-8')
	m = bytes_to_long(plaintext)

	print(f"m = {m}")

	n, e, c, d = encrpytRSA(m, 64)
	print(f"Public key:\n(n, e) = ({n}, {e})")
	print(f"Ciphertext = {c}")

	plaintext_decrypted = str(long_to_bytes(decryptRSA(c, d, n)), 'utf-8')
	print(f"Plaintext = {plaintext_decrypted}")



if __name__ == '__main__':
	main()
