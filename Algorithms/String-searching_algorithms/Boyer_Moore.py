def b_m(template,string):
    template_len = len(template)-1
    matches=0
    for j in range(len(string)-template_len):
        match=True
        char1=string[j]
        for k in range(template_len,-1,-1):
            if template[k]!=string[k+j]:
                match=False
                if template[::-1].find(char1)!=-1:
                    j+=template[::-1].find(char1)

                else:
                    j+=template_len
                break
        if match:
            matches+=1
    return matches