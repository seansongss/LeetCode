#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, bool> m;
        for (int num : nums) {
            if (m[num]) {
                return true;
            }
            m[num] = true;
        }
        return false;
    }
};