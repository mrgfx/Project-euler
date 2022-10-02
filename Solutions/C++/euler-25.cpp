#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string add_strs(string s1, string s2)
{
    if (s1.length() > s2.length())
    {
        swap(s1, s2);
    }

    string res_s = "";

    int n1 = s1.length(), n2 = s2.length();
    int len_diff = n2 - n1, carry = 0;

    for (int cur_idx = n1 - 1; cur_idx >= 0; cur_idx--)
    {
        int digit_sum = (s1[cur_idx] - '0') + (s2[cur_idx + len_diff] - '0') + carry;
        res_s += (digit_sum % 10 + '0');
        carry = digit_sum / 10;
    }

    for (int cur_idx = n2 - n1 - 1; cur_idx >= 0; cur_idx--)
    {
        int digit_sum = (s2[cur_idx] - '0') + carry;
        res_s += (digit_sum % 10 + '0');
        carry = digit_sum / 10;
    }

    if (carry)
    {
        res_s.push_back(carry + '0');
    }

    reverse(res_s.begin(), res_s.end());
    return res_s;
}

int main()
{
    string prev_num = "1", cur_num = "1", res_num = "";
    int cur_fib_idx = 2;
    const int DIGIT_COUNT = 1000;
    while (res_num.length() < DIGIT_COUNT)
    {
        res_num = add_strs(prev_num, cur_num);
        prev_num = cur_num;
        cur_num = res_num;

        cur_fib_idx++;
    }

    cout << cur_fib_idx << "\n";
    return 0;
}