def additive_hash_function(key,M):
    hash_value=-1
    for symbol in key:
        hash_value+=ord(symbol)
    hash_value%=M
    return hash_value
