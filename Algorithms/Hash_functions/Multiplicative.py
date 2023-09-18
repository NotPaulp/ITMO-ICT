def multiplicative_hash_function(key,M):
    Knum=''
    for symbol in key:
        Knum+=str(ord(symbol))
    Knum=int(Knum)
    C = (5 ** (0.5) - 1) / 2
    hash_value=int(M*((Knum*C)%1))
    return hash_value