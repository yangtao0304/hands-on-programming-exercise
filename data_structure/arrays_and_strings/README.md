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

## 2.1 二维数组

```
#include <iostream>
using namespace std;

template <size_t n, size_t m>
void printArray(int (&a)[n][m])
{
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    cout << "Example I:" << endl;
    int a[2][5];
    printArray(a);
    cout << "Example II:" << endl;
    int b[2][5] = {{1, 2, 3}};
    printArray(b);
    cout << "Example III:" << endl;
    int c[][5] = {1, 2, 3, 4, 5, 6, 7};
    printArray(c);
    cout << "Example IV:" << endl;
    int d[][5] = {{1, 2, 3, 4}, {5, 6}, {7}};
    printArray(d);
}
```

## 3.1 字符串

```
#include <iostream>

int main() {
    string s1 = "Hello World";
    cout << "s1 is \"Hello World\"" << endl;
    string s2 = s1;
    cout << "s2 is initialized by s1" << endl;
    string s3(s1);
    cout << "s3 is initialized by s1" << endl;
    // compare by '=='
    cout << "Compared by '==':" << endl;
    cout << "s1 and \"Hello World\": " << (s1 == "Hello World") << endl;
    cout << "s1 and s2: " << (s1 == s2) << endl;
    cout << "s1 and s3: " << (s1 == s3) << endl;
    // compare by 'compare'
    // if equal, return 0; else return -1
    cout << "Compared by 'compare':" << endl;
    cout << "s1 and \"Hello World\": " << !s1.compare("Hello World") << endl;
    cout << "s1 and s2: " << !s1.compare(s2) << endl;
    cout << "s1 and s3: " << !s1.compare(s3) << endl;
}
```

```
#include <iostream>

int main() {
    string s1 = "Hello World";
    // 1. concatenate
    s1 += "!";
    cout << s1 << endl;
    // 2. find
    cout << "The position of first 'o' is: " << s1.find('o') << endl;
    cout << "The position of last 'o' is: " << s1.rfind('o') << endl;
    // 3. get substr
    cout << s1.substr(6, 5) << endl;
}
```

## 4.1 双指针技巧1
```
void reverse(int *v, int N)
{
    int i = 0;
    int j = N - 1;
    while(i<j)
    {
        swap(v[i],v[j]);
        i++;
        j--;
    }
}
```
值得注意的是，这种技巧经常在排序数组中使用

## 4.2 双指针技巧2
```
给定一个数组和一个值，原地删除该值的所有实例并返回新的长度
int removeElement(vector<int>& nums, int val)
{
    int k = 0;
    for(int i = 0; i < nums.size(); ++i)
    {
        if(nums[i]!=val){
            nums[k++]=nums[i];
        }
    }
    return k;
}
```
同时有一个慢指针和一个快指针：解决这类问题的关键是***确定两个指针的移动策略***

## 5.1 数组相关的技术
1. 这里有一些其他类似于数组的数据结构，但具有一些不同的属性：

- 字符串
- 哈希表
- 链表
- 队列
- 栈
2. 正如我们所提到的，我们可以调用内置函数来对数组进行排序。但是，理解一些广泛使用的排序算法的原理及其复杂度是很有用的。

3. 二分查找也是一种重要的技术，用于在排序数组中搜索特定的元素。

4. 我们在这一章中引入了双指针技巧。想要灵活运用该技技巧是不容易的。这一技巧也可以用来解决：

- 链表中的慢指针和快指针问题
- 滑动窗口问题
5. 双指针技巧有时与贪心算法有关，它可以帮助我们设计指针的移动策略。 在不久的将来，我们会提供更多的卡片来介绍上面提到的这些技术，并更新链接。