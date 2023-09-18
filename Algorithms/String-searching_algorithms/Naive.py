def naive(template,string):
    template_len=len(template)-1
    matches=0
    for j in range(len(string) - template_len):
        match = True
        for k in range(template_len+1):
            if template[k] != string[j+k]:
                match=False
        if match:
            matches += 1
    return matches