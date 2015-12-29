def new_location(old_latitude, old_longitude, latitude_delta, longitude_delta):
	#preconditions
	assert 90 >= old_latitude >= -90, "Must be between 90 and -90 degrees"
	assert 180 >= old_longitude >= -180, "Must be between 90 and -90 degrees"

	new_latitude = old_latitude + latitude_delta
	new_longitude = old_longitude + longitude_delta

	#postconditions
	assert 90 >= new_latitude >= -90, "Must be between 90 and -90 degrees"
	assert 180 >= new_longitude >= -180, "Must be between 180 and -180 degrees"
	return new_latitude, new_longitude
	
