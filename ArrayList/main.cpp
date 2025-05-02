#include <iostream>
#include <string>

using namespace std;

template <typename T>
class ArrayList
{
private:
	int size;
	int capacity;
	T *arr;

public:
	ArrayList() : size(0), capacity(10)
	{
		arr = new T[capacity];
	};
	int Size()
	{
		return this->size;
	}
	int Get(int index) const
	{
		if (index >= size)
		{
			cerr << "Out of bounds" << endl;
			return -1;
		}
		return arr[index];
	}
	void Add(T item)
	{
		if (size == capacity)
		{
			cerr << "out of space Resizing" << endl;
			capacity *= 2;
			int *temp = new int[capacity];
			for (int i = 0; i < size; i++)
			{
				temp[i] = arr[i];
			}
			delete[] arr;
			arr = temp;
		}
		arr[size++] = item;
	}
	void showArray() const
	{
		cout << "[";
		for (int i = 0; i < size; i++)
		{
			cout << arr[i];
			if (i != size - 1)
				cout << ",";
		}
		cout << "]" << "\n";
	}
};

int main()
{
	ArrayList<int> arr;
	cout << arr.Size() << endl;
	arr.Add(1);
	arr.Add(2);
	arr.Add(3);
	arr.Add(4);
	arr.Add(5);
	arr.Add(6);
	arr.Add(7);
	arr.Add(7);
	arr.Add(7);
	arr.Add(7);
	arr.Add(7);
	cout << arr.Size() << "\n";
	arr.showArray();
	return 0;
}