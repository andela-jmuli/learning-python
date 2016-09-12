

def cases(me):
	for i in me:
		if i == i.upper():
			i = i.lower()
		elif i == i.lower():
			i = i.upper()
		print i


cases(['jana', 'TULIENDA', 'kujibamba'])