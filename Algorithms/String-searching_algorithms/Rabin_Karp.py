def r_k(template,string):
    template_len=len(template)-1
    alphabet_size=0
    alphabet=[]
    hash_code={}
    matches=0
    for i in range(len(string)):
        if not(string[i] in alphabet):
            alphabet.append(string[i])
            hash_code[string[i]]=alphabet_size
            alphabet_size+=1
    template_hash=0
    for n in range(template_len+1):
        template_hash+=hash_code[template[n]]*alphabet_size**(template_len-n)
    for j in range(len(string) - template_len):
        match = True
        substr_hash=0
        for n in range(template_len+1):
                substr_hash+=hash_code[string[n+j]]*alphabet_size**(template_len-n)
        if template_hash==substr_hash:
            for k in range(template_len+1):
                if template[k] != string[j+k]:
                    match = False
            if match:
                matches += 1
    return matches