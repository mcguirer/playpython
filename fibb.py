numbers = [1]

while len(numbers) < 256:
	if len(numbers) == 1:
		numbers.append(1)
	else:
		numbers.append(numbers[-1] + numbers[-2])

for i in numbers:
	print i