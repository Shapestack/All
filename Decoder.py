import random
import time

a=[(input('Введите число: '))]
b=[]

start=time.perf_counter()

wh=True
while wh:	
#	wh-=1
	decod=str(random.randrange(0, 10))
	for i in decod:
		if decod in a[0]:	
			b.append(decod)	
		else:
			pass
			
	joi=[''.join(b)]
	if joi==a:	
		break
	elif len(b)>=len(a[0]):
		print(f'{joi}', end='\r')
		b.clear()
	else:
		pass
		
if joi==a:
	print(a, 'coded')
	print('Success')
	print(joi, 'decoded')
else:
	print('Not decoded')

end=time.perf_counter()
print(end-start)



