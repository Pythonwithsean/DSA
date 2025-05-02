#include <iostream>

using namespace std;

template <typename T>
class ArrayList
{
private:
	int size;
	int capacity;
	T[] arr;

public:
	ArrayList() : size(0), capacity(10), arr(T[capacity]) {};
};

int main()
{

	return 0;
}