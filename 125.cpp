#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        string new_str = "";
        for (int i = 0; i < s.size() ; i++) {
            if (('a' <= s[i] && 'z' >= s[i] ) || ('0' <= s[i] && s[i] <= '9')) {
                new_str += s[i];
            } else if ('A' <= s[i] && s[i] <= 'Z') {
                new_str += tolower(s[i]);
            }
        }

        int start = 0;
        int end = new_str.size() - 1;
        while (end >= 0) {
            if (new_str[start] != new_str[end]) {
                return false;
            }
            start += 1;
            end -= 1;
        }

        return true;
    }
};