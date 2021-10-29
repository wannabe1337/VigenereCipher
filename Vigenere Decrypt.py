import time
from tqdm.auto import tqdm

ciphertext=input("Enter the text to Decrypt : ")
key=input("Enter the KEY : ")

key=key.upper()
ciphertext=ciphertext.upper()

letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plaintext=''

bar=tqdm(total=len(ciphertext),position=0,leave=False)
i=0
for c in ciphertext:
	
	bar.set_description('Decrypting {}'.format(c))
	bar.update()
	time.sleep(0.05)

	if(c==' '):
		plaintext+=' '
	
	else :

		if(i==len(key)):
			i=0

		rot=letters.find(key[i])+1
		i+=1
		shift=letters.find(c)
		if(shift<rot):
			shift=shift+25-rot+1
		else:
			shift=shift-rot
		plaintext+=letters[shift]

#bar.close()
print('\nVigenere Decrypted PlainText : ',plaintext)
