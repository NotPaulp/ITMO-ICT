def division_hash_function(key,M):
    Knum = ''
    for symbol in key:
        Knum += str(ord(symbol))
    Knum = int(Knum)
    hash_value=Knum%M
    return hash_value