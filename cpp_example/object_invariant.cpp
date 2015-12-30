#include<cassert>

class ValueStock
{
public:
	ValueStock(float price, float book_value) : 
		mprice(price),
		mbook_value(book_value)
	{}

	void buy(){
		this->invariant();
		...
		this->invariant();
	}

	void sell(){
		this->invariant();
		...
		this->invariant();
	}

private:
	void invariant(){
		assert(this->mprice < this->mbook_value); //Value stocks must have prices below book values
	}
};

	
