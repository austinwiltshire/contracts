#include<cassert>

std::string validate_input(std::string const& unsafe){
	//Validates unsafe input, ensuring it has no sql embedded in it
	auto safe_input = magic_and_stuff(unsafe);

	//postconditions
	assert(contains_no_sql(safe_input)); //output has been verified as being sql free
