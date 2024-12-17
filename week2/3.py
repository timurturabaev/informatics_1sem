word=input()
mirr=['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
z1=['E', 'J', 'S', 'Z']
z2=['3', 'L', '2', '5']
spell=[]
eq=[]
for i in word:
    spell.append(i)
for i in word:
    if mirr.count(i)!=0:
        eq.append(2)
    elif z1.count(i)!=0:
        eq.append(1)
    elif z2.count(i)!=0:
        eq.append(-1)
    else:
        eq.append(0)
mirror=False
pal=False
for i in range(len(word)):
    if spell[i]==spell[-i-1]:
        pal=True
    else:
        pal=False
for i in range(len(word)):
    if eq[i]==eq[-i-1]==2:
        mirror=True
    elif eq[i]==1 and eq[-i-1]==-1:
        mirror=True
    elif eq[i]==-1 and eq[-i-1]==1:
        mirror=True
    else:
        mirror=False
if pal==True and mirror==True:
    print(word, 'is a mirrored palindrome.')
elif pal==True and mirror!=True:
    print(word, 'is a regular palindrome.')
elif pal!=True and mirror==True:
    print(word, 'is a mirrored string.')
else:
    print(word, 'is not a palindrome.')