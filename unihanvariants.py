# _*_ coding=utf-8 *_*
lines = open("Unihan/Unihan_Variants.txt", "r", encoding="UTF-8").readlines()

db = {}

for l in lines:
    if l[0]=='#': continue
    s = l.split('\t')
    if s[1]=='kSimplifiedVariant':
        o = chr(int(s[0][2:], base=16))
        d = chr(int(s[2].split(' ')[0][2:], base=16))
        if o in db: 
            db[o].append(d)
        else:
            db[o] = [d]

lines = open('cangjie5raw.txt', 'r', encoding='UTF-8').readlines()
f = open('cangjie5out.txt', 'w', encoding='UTF-8')

for l in lines:
    f.write(l)
    s = l.split('\t')
    if s[1] in db:
        for d in db[s[1]]:
            f.write("%s\t%s\t%s\n" % (s[0], d, '999'))

f.close()


