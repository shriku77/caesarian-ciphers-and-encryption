'''
Created on Oct 21, 2021

@author: Praagna Shrikrishna Sriram
'''
def encrypt(w):
#encrypts a given string into piglatin
    a = 'aeiouAEIOU'
    b = ""
    u =""
    for v in w:
            if v in a:
                b += v
    c = list(b)
    d = w[2:]
    e = ""
    if w[:2] == 'qu':
        for q in w[2:]:
                if q in a:
                    e += q
    f = list(e)
    g = "aeiouAEIOUyY"
    h =""
    if len(set(a)&set(w)) == 0:
        for t in w:
            if t in g:
                h += t
    j = list(h)




    if w[0] in 'aeiouAEIOU':
        return w + "-way"
    elif (w[0:2] == "qu"):
        return w[w.index(f[0]):] + "-" + w[:w.index(f[0])] + "ay"
    else:
        for i in range(len(w)):
            if len(c) == 0:
                if len(set('yY') & set(w)) > 0:
                    return w[w.index(j[0]):] + "-" + w[:w.index(j[0])] + "ay"
                else:
                    return w + '-way'
            else:
                return w[w.index(c[0]):] + "-" + w[:w.index(c[0])] + "ay"


def decrypt(w):
 #decrypts a string from piglatin
    a = 'aeiouAEIOU'
    b = set(w) & set(a)
    c = list(b)
    if w[-2:] == "ay":
        if len(set(w[:-4]) & set(a)) == 0:
            k = w[w.index("-") + 2:-2] + w[:w.index("-")]
            return k
        elif w[0] in a:
            if w[-3] in 'w':
                i = w[w.index("-") + 2:-2] + w[:w.index("-")]
                return i
            else:
                o = w[w.index("-") + 1:-2] + w[:w.index("-")]
                return o
        else:
            o = w[w.index("-") + 1:-2] + w[:w.index("-")]
            return o


encrypt('rhythm')
encrypt('zzz')
encrypt('STRENGTH')
encrypt('my')

decrypt('one-way')
decrypt('our-fay')
decrypt('antity-quay')
decrypt('easel-way')
decrypt('y-may')