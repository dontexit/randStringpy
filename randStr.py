# import os
# import sys

# def write_random_lowercase(n):
#     min_lc = ord(b'a')
#     len_lc = 26
#     ba = bytearray(os.urandom(n))
#     for i, b in enumerate(ba):
#         ba[i] = min_lc + b % len_lc # convert 0..255 to 97..122
#     sys.stdout.buffer.write(ba)

# write_random_lowercase(1000000)
import string
import secrets
def create_ud():
    alphabet = string.ascii_letters + string.digits + '_'
    return ''.join(secrets.choice(alphabet) for i in range(12))
    # return 
    
print(create_ud())

