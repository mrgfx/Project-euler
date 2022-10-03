#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int expression_value(vector<int> indexes)
{
    int max_len = indexes[indexes.size() - 1];
    string nums = "";
    int nums_len = 0;
    int cur_num = 1;
    while (nums_len < max_len)
    {
        nums.append(to_string(cur_num));
        nums_len += (floor(log10(cur_num)) + 1);
        ++cur_num;
    }

    int res_val = 1;
    for (auto idx : indexes)
    {
        res_val *= (nums[idx - 1] - '0');
    }

    return res_val;
}

int main()
{
    vector<int> indexes{1, 10, 100, 1000, 10000, 100000, 1000000};
    cout << expression_value(indexes) << "\n";
    return 0;
}