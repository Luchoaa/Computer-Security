from pwn import *

# Define the key length
KEY_LEN = 50000

# Connect to the server
conn = remote('mercury.picoctf.net', 36981)

# Receive the encrypted flag
conn.recvuntil('This is the encrypted flag!\n')
encrypted_flag_hex = conn.recvline().strip()
encrypted_flag = bytes.fromhex(encrypted_flag_hex.decode())

# Calculate the length of input needed to wrap around key_location to 0
input_length = KEY_LEN - len(encrypted_flag)

# Send the input to wrap around the key_location
conn.sendline('A' * input_length)

# Send another input to get it encrypted with the same key slice
conn.sendline('B' * len(encrypted_flag))
conn.recvuntil('Here ya go!\n')
encrypted_input_hex = conn.recvline().strip()
encrypted_input = bytes.fromhex(encrypted_input_hex.decode())

# Recover the key slice
key_slice = bytes([a ^ b for a, b in zip(encrypted_input, b'B' * len(encrypted_flag))])

# Decrypt the flag
flag = bytes([a ^ b for a, b in zip(encrypted_flag, key_slice)])

print('Flag:', flag.decode())
