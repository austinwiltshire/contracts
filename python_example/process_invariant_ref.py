def foo(x_1, y):
	x_1 = x_1 + 3

	#process invariant
	assert x >= 3, "X must be greater than 3"

	x_2 = x_1 + y

	...

	#process invariant
	assert x_2 >= y, "X must be greater than y"

	return x_2
