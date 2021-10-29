import time
from tqdm.auto import tqdm

text=input("Enter the text to encrypt : ")
key=input("Enter the KEY : ")

key=key.upper()
text=text.upper()

letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertext=''

bar=tqdm(total=len(text),position=0,leave=False)
i=0
for c in text:
	
	bar.set_description('Encrypting {}'.format(c))
	bar.update()
	time.sleep(0.05)

	if(c==' '):
		ciphertext+=' '
	else:
		if(i==len(key)):
			i=0
		rot=letters.find(key[i])+1
		i+=1
		shift=letters.find(c)+rot
		if(shift>25):
			shift=(shift%25) - 1
		ciphertext+=letters[shift]

#bar.close()
print('\nVigenere CipherText : ',ciphertext)
