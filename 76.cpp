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
            if (target.find(c) == target.end()) {
                target.insert(make_pair(c, 1));
            } else {
                target[c] += 1;
            }
            cout << c << ": ";
            cout << target[c] << endl;
        }
        cout << t << endl;
        unordered_map<char, int> subset;
        for (char c : s) {
            if (subset.find(c) == subset.end()) {
                subset.insert(make_pair(c, 1));
            } else {
                subset[c]++;
            }
            cout << c << ": ";
            cout << subset[c] << endl;
        }

        int l = 0;
        int r = s.size() - 1;
        string substring = "";
        while (l < r) {
            char left = s[l];
            char right = s[r];
            if (subset[left] - 1 < target[left] && subset[right] - 1 < target[right]) {
                for (int i = l; i <= r; i++) {
                    substring += s[i];
                }
                return substring;
            } else if (subset[left] - 1 < target[left]) {
                subset[right] -= 1;
                r -= 1;
            } else if (subset[right] - 1 < target[right]) {
                subset[left] -= 1;
                l += 1;
            } else {
                subset[left] -= 1;
                subset[right] -= 1;
                l += 1;
                r -= 1;
            }
        }

        return "";
    }
};

int main() {
    cout << Solution().minWindow("ADOBECODEBANC", "ABC") << endl;
}