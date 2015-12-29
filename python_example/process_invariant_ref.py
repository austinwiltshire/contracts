def foo(x, y):

	x_1 = adjustment_1(x)
	x_2 = adjustment_2(x, y)
	return x_2

def adjustment_1(x):
	x = x + 3
	#process invariant
	assert x >= 3, "X must be greater than 3"
	return x


def adjustment_2(x, y):
	x = x + y
	#process invariant
	assert x >= y, "X must be greater than y"
	return x	x = x + y
