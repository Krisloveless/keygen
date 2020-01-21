import pdb

def guess(a, b):
	#pdb.set_trace()
	t1 = ord(a)
	t2 = ord(b)
	eax = t1^t2
	#0xF
	# here actually asm dhq, for simplicity edx = 0
	if eax < 0:
		edx = 0xFFFFFFFF
	else:
		edx = 0
	edx &= 15
	eax += edx
	eax &= 15
	eax -= edx
	#0x41
	r8 = 65
	#0x30
	r15 = 48
	#0xA
	if eax < 10:
		r8 = 48
	r8 += eax
	return chr(r8)

def mash(name):
	res = ""
	while len(res) < 16:
		res += name
	res = res[:16]
	return res

if __name__ == '__main__':
	out = ""
	NAME = "TEST_PURPOSE"
	a = "1234567890123456"
	b = mash(NAME)
	for i in range(len(a)):
		out += guess(a[i], b[i])
	print(out)
