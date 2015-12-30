
#include<cassert>

...
std::vector<int> the_list;
...
auto found = std::find_if(
	the_list.begin(),
	the_list.end(),
	[](int x){ return x > 20; }
);

assert(found != the_list.end()); //At least one element more than 20 exists
...
