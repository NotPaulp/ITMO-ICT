def k_m_p(template,string):
    k=0
    pref = {0: 0}
    matches=0
    for i in range(1, len(template)):
        j = pref[i - 1]
        while j > 0 and template[j] != template[i]:
            j = pref[j - 1]
        if template[j] == template[i]:
            j += 1
        pref[i] = j
    for j in range(len(string)):
        while k != 0 and string[j]!=template[k]:
            k = pref[k - 1]

        if string[j]==template[k]:
            k+=1
            if k == len(template):
                matches += 1
                k = 0
    return matches