def foo(x, y):
	x = x + 3

	#process invariant?
	assert x >= 3, "X must be greater than 3"

	x = x + y

	...

	#process invariant?
	assert x >= y, "X must be greater than y"

	return x
