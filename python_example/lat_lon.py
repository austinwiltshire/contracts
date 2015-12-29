
class Latitude(object):
	def __init__(self, value):
		self._value = value
		self._invariant_()

	def _invariant_(self):
		assert 90 >= self._value >= -90, "Must be between 90 and -90 degrees"

	def __add__(self, other):
		self._invariant_()
		return Latitude(self._value + other._value)

class Longitude(object):
	def __init__(self, value):
		self._value = value
		self._invariant_()

	def _invariant_(self):
		assert 180 >= self._value >= -180, "Must be between 180 and -180 degrees"

	def __add__(self, other):
		self._invariant_()
		return Longitude(self._value + other._value)


def new_location(old_latitude, old_longitude, latitude_delta, longitude_delta):
	#type checking not required, just here to illustrate the object invariant.
	# In statically typed languages this wouldn't be required at all
	assert isinstance(old_latitude, Latitude) and isinstance(latitude_delta, Latitude)
	assert isinstance(old_longitude, Longitude) and isinstance(longitude_delta, Longitude)

	new_latitude = old_latitude + latitude_delta
	new_longitude = old_longitude + longitude_delta

	return new_latitude, new_longitude
