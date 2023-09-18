def crc32(*args):
    key=bytes(args[0],"utf-8")
    crc = 0xFFFFFFFF
    polynomial = 0xEDB88320
    for byte in key:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1
    hash_value=crc ^ 0xFFFFFFFF
    return hash_value