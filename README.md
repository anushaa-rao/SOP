# SOP
Study Oriented Project code bases 
ECDSA

This is an implementation of ECDSA (Elliptic Curve Digital Signature Algorithm) in Python. It uses the ed25519 elliptic curve, which is defined by the equation "y^2 = x^3 + ax^2 + x" over the field F_p, where p = 2^255 - 19, and a = -1.

The program begins by defining the base point, which is a point on the curve with coordinates (15112221349535400772501151409588531511454012693041857206046113283949847762202, 46316835694926478169428394003475163141307993866256225615783033603165251855960). It then defines several helper functions, including functions for finding the positive modulus of a number, typecasting a string to an integer, calculating the greatest common divisor of two numbers, and finding the modular inverse of a number modulo another number.

The program then defines a function for applying the double-and-add method, which is used to compute scalar multiplication of a point on the elliptic curve. It also defines a function for adding two points on the elliptic curve, which is used by the double-and-add function.

Next, the program generates a random 32-byte private key and uses the double-and-add function to compute the corresponding public key. It then hashes a message using SHA-512 and signs the hash using ECDSA. The signing process involves generating a random value "r", computing the point R = r * base using scalar multiplication, hashing the x-coordinate of R, the x-coordinate of the public key, and the message using SHA-512 to obtain a value "h", and computing the signature "s" as s = r + h * private key. The program then outputs the signature as a pair (R, s).

Finally, the program verifies the signature by computing two points: P1 = s * base - h * public key and P2 = R + h * public key. If P1 == P2, the signature is valid. The program outputs the result of the verification check

