import struct


def float_to_hex(float_value):
    # Float değeri 32 bit floating point olarak paketler
    packed_float = struct.pack('f', float_value)

    # Paketlenmiş float değerini hexadecimal olarak dönüştürür
    hex_value = hex(int.from_bytes(packed_float, byteorder='big'))[2:]

    # Hexadecimal değeri 4 haneli olacak şekilde 0'larla tamamlar
    hex_value = hex_value.zfill(8)  # 32 bit = 8 haneli hexadecimal değer

    return hex_value

#
# # Örnek kullanım
# float_value = 12.88 # Örnek olarak 3.14 float değeri
# hex_result = float_to_hex(float_value)
# print("32 bit Floating Point Hexadecimal Değer:", hex_result)
