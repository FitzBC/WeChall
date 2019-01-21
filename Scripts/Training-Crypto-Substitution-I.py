# s='CT AFZ RNIPQFAT QJL TJM WRU DZRL AFPG IT EDPZUL P RI PISDZGGZL OZDT VZNN LJUZ TJMD GJNMAPJU KZT PG WUGIPWIDNDEC AFPG NPAANZ WFRNNZUQZ VRG UJA AJJ FRDL VRG PA'
# by-the-almighty-god-you-can-read-this-my-friend-i-am-impressed-very-well-done-your-solution-key-is-cnsmicmrlrfb-this-little-challenge-was-not-too-hard-was-it
s='OH VJB KITWAJVH AXR HXM YKZ SBKR VJWL TH USWBZR W KT WTESBLLBR PBSH FBII RXZB HXMS LXIMVWXZ CBH WL YSOZXXXIZZBI VJWL IWVVIB YJKIIBZAB FKL ZXV VXX JKSR FKL WV'

total=''
# dict={'A':'t','B':'.','C':'b','D':'r','E':'f','F':'h','G':'s','H':'.','I':'m','J':'o','K':'k',
#       'L':'d','M':'u','N':'l','O':'v','P':'i','Q':'g','R':'a','S':'p','T':'y','U':'n','V':'w',
#       'W':'c','X':'.','Y':'.','Z':'e',' ':'-'}

dict={'A':'g','B':'e','C':'k','D':'.','E':'p','F':'w','G':'.','H':'y','I':'l','J':'h','K':'a',
      'L':'s','M':'u','N':'.','O':'b','P':'v','Q':'.','R':'d','S':'r','T':'m','U':'f','V':'t',
      'W':'i','X':'o','Y':'c','Z':'n',' ':'-'}

# a c d e f g h i l m n o r s t u v w
# p y
# a c d e f g h i l m n o r s t u v w p y
# b j q x z
count=0
countdict={}
for i in s:
    if i in countdict:
        countdict[i]=countdict[i]+1
    else:
        countdict[i]=0
print(countdict)
tt1=s.split(' ')
dict3={}
for i in tt1:
    if i in dict3:
        dict3[i]=dict3[i]+1
    else:
        dict3[i]=0
print(dict3)
for i in s:
    ss=s[:count]
    sss=s[count+1:]
    count=count+1
    s=ss+dict[i]+sss
print(s)