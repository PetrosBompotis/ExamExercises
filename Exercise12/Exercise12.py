with open('myfile.txt','r') as file:
    s = file.read()
'''*****************************************************************************
 Μετατροπή κάθε χαρακτήρα του κειμένου του αρχείου στον αντίστοιχο αριθμό ASCII
*****************************************************************************'''
a=[ord(c) for c in s]
'''**********************************************************************************************
Συνάρτηση που μετατρέπει τους αριθμούς ASCII των χαρακτήρων στον αντίστοιχο του κατοπτρικού τους
**********************************************************************************************'''
def met(b):
    b=128-b
    return b
c=[met(b) for b in a]
'''************************************************************
Μετατροπή των αριθμών ASCII σε χαρακτήρες ASCII και ένωσή τους
************************************************************'''
d=""
for i in range(len(c)):
    d=d +chr(c[i])
'''************************
Αναποδογύριση του κείμενου
************************'''
reversedstring=''.join(reversed(d))
print(reversedstring)