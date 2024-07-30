#include <string>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        int count[26] = {0};
        for (char c : s) {
            count[c - 'a']++; 
        }

        for (char c : t) {
            count[c - 'a']--; 
        }

        for (int i : count) {
            if (i != 0) {
                return false;
            }
        }
        return true;
    }
};