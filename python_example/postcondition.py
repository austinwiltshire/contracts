
def validate_input(unsafe_input):
	"""Validates unsafe input, ensuring it has no SQL embedded in it"""
	safe_input = magic_and_stuff(unsafe_input)

	#postconditions
	assert contains_no_sql(safe_input), "Output has been verified as being sql free"
