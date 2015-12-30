#define PRECONDITION(predicate, message) \
if(!(predicate)){ \
	std::cerr << "Precondition failed! " << (message) << std::endl; \
	assert(predicate); \
}

#define POSTCONDITION(predicate, message) \
if(!(predicate)){ \
	std::cerr << "Postcondition failed! " << (message) << std::endl; \
	assert(predicate); \
}

#define PROCESS_INVARIANT(predicate, message) \
if(!(predicate)){ \
	std::cerr << "Process Invariant Failed! " << (message) << std::endl; \
	assert(predicate); \
}

#define OBJECT_INVARIANT(predicate, message) \
if(!(predicate)){ \
	std::cerr << "Object Invariant Failed! " << (message) << std::endl; \
	assert(predicate); \
}
