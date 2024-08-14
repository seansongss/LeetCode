#include <string>
using namespace std;

class Solution {
public:
    int myAtoi(string s) {
        int i = 0;
        int sign = 1;
        long res = 0;
        while (i < s.size() && s[i]==' ') {
            i++;
        }

        if (s[i] == '-') {
            sign = -1;
            i++;
        } else if (s[i] =='+') {
            i++;
        }

        while (i < s.size()) {
            if ('0' <= s[i] && s[i] <= '9') {
                res = res * 10 + (s[i] - '0');
                if (res > INT_MAX && sign == 1) {
                    return INT_MAX;
                } else if (res > INT_MAX && sign == -1) {
                    return INT_MIN;
                }
                
                i++;

            } else {
                return res * sign;
            }
        }

        return res * sign;
    }
};