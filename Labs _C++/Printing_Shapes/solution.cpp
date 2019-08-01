#include <iostream>
#include <string>
using namespace std;

// Problem 1: The Staircase

void theStaircase(int num)
{
    for (unsigned int i = 1; i < num + 1; i++)
    {
        for (unsigned int j = 1; j < i + 1; j++)
        {
            cout << j << " ";
        }
        cout << endl;
    }
}

// Problem 2: Flip-It

void flipIt(int num)
{
	for (unsigned int i = 0; i < num; i++)
	{
		for (unsigned int j = 1; j < num + 1 - i; j++)
		{
			cout << j << " ";
		}
		cout << endl;
	}
}

// Problem 3: Backwards Now

void backwardsNow(int num) 
{
	for (unsigned int i = 1; i < num + 1; i++) 
	{
		for (unsigned int j = 0; j < i; j++) 
		{
			cout << (num - j) << " ";
		}
		cout << endl;
	}
}

// Problem 4: Flip-It Backwards

void flipItBackwards(int num) 
{
	for (unsigned int i = 1; i < num + 1; i++) 
	{
		for (unsigned int j = 0; j < (num - i + 1); j++) 
		{
			cout << (num - j) << " ";
		}
		cout << endl;
	}
}

// Problem 5: Sharp Bump

void sharpBump(int num) 
{
	for (unsigned int i = 1; i < (num + 1); i++) 
	{
		for (unsigned int j = 1; j < (i + 1); j++) 
		{
			cout << j << " ";
		}
		cout << endl;
	}
	for (unsigned int i = 0; i < num - 1; i++)
	{
		for (unsigned int j = 1; j < (num - i); j++)
		{
			cout << j << " ";
		}
		cout << endl;
	}
}

// Problem 6: Pointy Corner

void pointyCorner(int num) 
{
	for (unsigned int i = 0; i < num; i++)
	{
		for (unsigned int j = 1; j < (num - i + 1); j++)
		{
			cout << j << " ";
		}
		cout << endl;
	}
	for (unsigned int i = 2; i < (num + 1); i++)
	{
		for (unsigned int j = 1; j < (i + 1); j++)
		{
			cout << j << " ";
		}
		cout << endl;
	}
}

// Problem 7: If and Then

void ifAndThen(int num) 
{
	for (unsigned int i = 0; i < num; i++) 
	{
		for (unsigned int j = 0; j < num; j++) {
			if (i == j) 
			{
				cout << j;
			}
			else
			{
				cout << "0";
			}
		}
		cout << endl;
	}
}

// Problem 8: Binary Staircase

void binaryStaircase(int num)
{
	for (unsigned int i = 1; i < num + 1; i++) 
	{
		bool toggle = true;
		for (unsigned int j = 0; j < i; j++) {
			if (toggle) 
			{
				cout << "1";
			}
			else
			{
				cout << "0";
			}
			toggle = !toggle;
		}
		cout << endl;
	}
}
            

// Problem 9: Binary Block

void binaryBlock(int num)
{
	bool toggle = true;
	for (unsigned int i = 1; i < num + 1; i++) 
	{
		for (unsigned int j = 0; j < num; j++) {
			if (toggle) 
			{
				cout << "1";
			}
			else
			{
				cout << "0";
			}
			toggle = !toggle;
		}
		cout << endl;
	}
}

// Problem 10: Strange Layers

void strangeLayers(int num)
{
	for (int i = 1; i < num + 1; i++)
	{
		for (int j = 0; j < num; j++)
		{
			if (num - j <= i)
			{
				cout << (i);
			}
			else
			{
				cout << "1";
			}
		}
		cout << endl;
	}
}


// Problem 11: Palindromes

void palindromes(int num)
{
	for (int i = 2; i < num + 2; i++)
	{
		for (int j = 1; j < i; j++)
		{
			cout << j << " ";
		}
		for (int j = (i - 2); j > 0; j--)
		{
			cout << j << " ";
		}
		cout << endl;
	}
}

// Problem 12: Hanging by a Thread

void hangingByAThread(int num)
{
	for (int i = 0; i < num; i++)
	{
		for (int j = 1; j < num + 1; j++) 
		{
			if (j > i)
			{
				cout << j;
			}
			else
			{
				cout << " ";
			}
		}
		cout << endl;
	}
	for (int i = 2; i < num + 1; i++)
	{
		for (int j = 1; j < num + 1; j++)
		{
			if (j > num - i)
			{
				cout << j;
			}
			else
			{
				cout << " ";
			}
		}
		cout << endl;
	}
}


// Problem 13: Vertical Counting

void verticalCounting(int num)
{
	for (int i = 1; i < num + 1; i++) 
	{
		for (int j = 0; j < i; j++)
		{
			int addnum = 0;
			int colnum = num;
			for (int k = 0; k < j; k++)
			{
				addnum += colnum;
				colnum -= 1;
			}
			cout << ((i - j) + addnum) << " ";
		}
		cout << endl;
	}
}


// Problem 14: Even Diamond

#include <cmath>

void evenDiamond(int num)
{
	if (num % 2 == 0)
	{
		return;
	}
	int numbers = 1;
	int rate = 2;
	int mid = ceil(static_cast<double>(num) / 2.0);
	for (int i = 0; i < num; i++)
	{
		for (int j = 0; j < (num - numbers); j++)
		{
			cout << " ";
		}
		for (int j = 0; j < numbers; j++)
		{
			cout << (j + 1) << " ";
		}
		cout << endl;
		if (i == (mid - 1))
		{
			rate = -rate;
		}
		numbers += rate;
	}
}

// Problem 15: Even Hourglass

#include <cmath>

void evenHourglass(int num)
{
	if (num % 2 == 0)
	{
		return;
	}
	int numbers = num;
	int rate = -2;
	int mid = ceil(static_cast<double>(num) / 2.0);
	for (int i = 0; i < num; i++)
	{
		for (int j = 0; j < (num - numbers); j++)
		{
			cout << " ";
		}
		for (int j = 0; j < numbers; j++)
		{
			cout << (j + 1) << " ";
		}
		cout << endl;
		if (i == (mid - 1))
		{
			rate = -rate;
		}
		numbers += rate;
	}
}

// Problem 16: Offset Diamond

#include <cmath>

void offsetDiamond(int num)
{
	int numbers = 1;
	int rate = 1;
	int mid = num - 1;
	for (int i = 0; i < num * 2 - 1; i++)
	{
		for (int j = 0; j < (num - numbers); j++)
		{
			cout << " ";
		}
		for (int j = 0; j < numbers; j++)
		{
			cout << (j + 1) << " ";
		}
		cout << endl;
		if (i == (mid - 1))
		{
			rate = -rate;
		}
		numbers += rate;
	}
}

// Problem 17: Offset Hourglass
#include <cmath>

void offsetDiamond(int num)
{
	int numbers = num;
	int rate = -1;
	int mid = num - 1;
	for (int i = 0; i < num * 2 - 1; i++)
	{
		for (int j = 0; j < (num - numbers); j++)
		{
			cout << " ";
		}
		for (int j = 0; j < numbers; j++)
		{
			cout << (j + 1) << " ";
		}
		cout << endl;
		if (i == mid)
		{
			rate = -rate;
		}
		numbers += rate;
	}
}


