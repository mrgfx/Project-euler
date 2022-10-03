#include <iostream>
#include <cmath>
using namespace std;
bool is_prime(int n)
{
    if (n <= 1)
    {
        return false;
    }

    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }

    return true;
}

bool is_permutation_int(int n1, int n2)
{
    int digits[10];
    for (int i = 0; i < 10; i++)
    {
        digits[i] = 0;
    }

    while (n1 > 0)
    {
        digits[n1 % 10]++;
        n1 /= 10;
    }
    while (n2 > 0)
    {
        digits[n2 % 10]--;
        n2 /= 10;
    }

    for (int i = 0; i < 10; i++)
    {
        if (digits[i] != 0)
        {
            return false;
        }
    }

    return true;
}

string find_prime_permutation(const int n)
{
    int start_num = pow(10, n + 1);
    int end_num = pow(10, n);

    string res_prime_permutation = "";
    while (start_num >= end_num)
    {
        if (is_prime(start_num))
        {
            int first_permutation = start_num + 3330;
            int second_permutation = first_permutation + 3330;

            if (is_permutation_int(start_num, first_permutation) && is_permutation_int(start_num, second_permutation) && is_prime(first_permutation) && is_prime(second_permutation))
            {
                res_prime_permutation = to_string(start_num) + to_string(first_permutation) + to_string(second_permutation);
                break;
            }
        }
        --start_num;
    }
    return res_prime_permutation;
}

int main()
{
    const int DIGIT_LENGTH = 3;
    string result = find_prime_permutation(DIGIT_LENGTH);
    cout << result << "\n";
    return 0;
}