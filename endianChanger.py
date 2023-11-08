def big_endian_to_little_endian(big_endian_hex):
    # Convert big endian hex to bytes and reverse the byte order
    little_endian_bytes = bytes.fromhex(big_endian_hex)[::-1]

    # Convert bytes back to hex
    little_endian_hex = little_endian_bytes.hex()

    return little_endian_hex


# Example usage
big_endian_hex = "123456789ABCDEF0"
little_endian_hex = big_endian_to_little_endian(big_endian_hex)
print("Little Endian Representation:", little_endian_hex)
