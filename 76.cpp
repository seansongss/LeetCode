#include <string>
#include <unordered_map>
#include <iostream>
using namespace std;
class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty() || s.size() < t.size()) return "";

        unordered_map<char, int> target;
        for (char c : t) {
            target[c]++;
        }
        int count = t.size();

        int l = 0, r = 0, start = 0;
        int minLen = INT_MAX;
        while (r < s.size()) {
            if (target[s[r]] > 0) {
                count--;
            }
            target[s[r]]--;
            r++;

            while (count == 0) {
                if (r - l < minLen) {
                    start = l;
                    minLen = r - l;
                }

                if (target[s[l]] == 0) {
                    count++;
                }
                target[s[l]]++;
                l++;
            }
        }

        if (minLen == INT_MAX) {
            return "";
        } else {
            return s.substr(start, minLen);
        }
    }
};

int main() {
    cout << Solution().minWindow("ADOBECODEBANC", "ABC") << endl;
}