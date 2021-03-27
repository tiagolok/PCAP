from math import e

def makeclosure(par):
	loc = par
	def power(p):
		return p ** loc
	return power

fsqr = makeclosure(2)
fcub = makeclosure(3)
fexp = makeclosure(e)
for i in range(5):
	print(i, fsqr(i), fcub(i), fexp(i))
