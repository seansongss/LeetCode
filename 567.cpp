#include <string>
#include <iostream>
using namespace std;
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;
        int alphabet_set[26] = {0};
        for (char c : s1) {
            alphabet_set[c - 'a'] += 1;
        }
        
        int subset[26] = {0};
        for (int i = 0; i < s1.size() ; i++ ) {
            subset[s2[i] - 'a'] += 1;
        }

        int toDelete = 0;
        for (int i = s1.size() - 1; i < s2.size(); i++) {
            int count = 0;
            for (int j = 0; j < 26; j++) {
                if (alphabet_set[j] != subset[j]) {
                    break;
                }
                count++;
            }
            if (count == 26) return true;

            if (i != s2.size() - 1) {
                subset[s2[toDelete] - 'a'] -= 1;
                subset[s2[toDelete + s1.size()] - 'a'] += 1;
                toDelete++;
            }
        }
        return false;
    }
};

int main() {
    cout << Solution().checkInclusion("ab", "eidboaoo") << endl;
    cout << "I am learning C++";
}