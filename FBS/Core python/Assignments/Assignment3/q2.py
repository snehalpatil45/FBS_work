# wap to input any alphabet and check whether it is vowel or consonant.

alphabet = input('Enter alphabet:')
if(alphabet .lower() in ['a','e','i','o' ,'u']):
	print(f'{alphabet} is a vowel')
else:
	print(f'{alphabet} is a consonant')