# [数组和字符串](https://leetcode-cn.com/explore/learn/card/array-and-string/)

## 1.1 数组中的操作

```
#include <iostream>
using namespace std;

int main()
{
    // 1. Initialize
    int a0[5];
    int a1[5] = {1, 2, 3}; // other element will be set as the default value
    // 2. Get Length
    int size = sizeof(a1) / sizeof(*a1);
    cout << "The size of a1 is: " << size << endl;
    // 3. Access Element
    cout << "The first element is: " << a1[0] << endl;
    // 4. Iterate all Elements
    cout << "[Version 1] The contents of a1 are:";
    for (int i = 0; i < size; ++i)
    {
        cout << " " << a1[i];
    }
    cout << endl;
    cout << "[Version 2] The contents of a1 are:";
    for (int& item : a1)
    {
        cout << " " << item;
    }
    cout << endl;
    // 5. Modify Element
    a1[0] = 4;
    // 6. Sort
    sort(a1, a1+size);
}
```

## 1.2 动态数组

```
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    // 1. Initialize
    vector<int> v0;
    vector<int> v1(5, 0);
    // 2. Make a copy
    vector<int> v2(v1.begin(), v1.end());
    vector<int> v3(v2);
    // 2. Cast an array to a vector
    int a[5] = {0, 1, 2, 3, 4};
    vector<int> v4(a, *(&a + 1));
    // 3. Get length
    cout << "the size of v4 is: " << v4.size() << endl;
    // 4. Access element
    cout << "the first element in v4 is: " << v4[0] << endl;
    // 5. Iterate the vector
    cout << "[Version 1] The contents of v4 are:";
    for (int i = 0; i < v4.size(); ++i)
    {
        cout << " " << v4[i];
    }
    cout << endl;
    cout << "[Version 2] The contents of v4 are:";
    for (int &item : v4)
    {
        cout << " " << item;
    }
    cout << endl;
    cout << "[Version 3] The contents of v4 are:";
    for (auto item = v4.begin(); item != v4.end(); ++item)
    {
        cout << " " << *item;
    }
    cout << endl;
    // 6. Modify element
    v4[0] = 5;
    // 7. Sort
    sort(v4.begin(), v4.end());
    // 8. Add new element at the end of the vector
    v4.push_back(-1);
    // 9. Delete the last element
    v4.pop_back();
}
```