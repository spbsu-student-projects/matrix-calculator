import re, fractions
import operation, expression, matrix

TOKEN_OP = r'\(|\)|' + '|'.join(re.escape(op.name) for op in operation.opDict.values())
TOKEN = re.compile(r'[\w\.]+|'+ TOKEN_OP)
TOKEN_OP = re.compile(TOKEN_OP)
TOKEN_NUM = re.compile(r'[\d\.]+')

print("Input expression:")

s = [m.group() for m in TOKEN.finditer(input())]

print()

d = dict()

for t in s:
	if TOKEN_OP.fullmatch(t) is None and t not in d:
		if not TOKEN_NUM.fullmatch(t) is None:
			d[t] = matrix.Matrix(t)
		else:
			width = None
			
			elemList = []
			
			while width is None:
				print("Input " + t + ":")
				
				while True:
					elemLine = list(map(fractions.Fraction, input().split()))
					if len(elemLine) == 0: break
					
					if len(elemLine) != width and not width is None:
						print("Wrong number of elements, input this line again:")
					else:
						width = len(elemLine)
						elemList.extend(elemLine)
			
			m = matrix.Matrix(0, len(elemList) // width, width)
			for i in range(len(m)): m[i] = elemList[i]
			
			d[t] = m

print("Result:")
print(expression.process(s, d))