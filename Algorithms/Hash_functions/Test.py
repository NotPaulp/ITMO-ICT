from Additive import additive_hash_function
from Multiplicative import multiplicative_hash_function
from Division import division_hash_function
from CRC32 import crc32
hash_table={}
Keys=input("Enter the keys separated by spaces: ").split(' ')
load_factor=0.7
M=int(len(Keys)/load_factor)
hash_functions={0:additive_hash_function,1:multiplicative_hash_function,2:division_hash_function,3:crc32}
while True:
    print("Enter hash function type:\n0 - Additive\n1 - Multiplicative\n2 - Division\n3 - CRC32")
    type=input()
    if type.isdigit():
        type=int(type)
        if type >=0 and type <= 3:
            hash_function=hash_functions[type]
            break
    print("Incorrect input format: enter the number 0-3")
for Key in Keys:
    hash_value=hash_function(Key,M)
    hash_table[Key]=hash_value
    print(f"{Key}: {hash_table[Key]}")
