#include <vector>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> nums_cpy = {nums.begin(), nums.end()};
        int prev;
        int count = 0;
        for (int num : nums_cpy) {
            if (prev != num) {
                prev = num;
                nums[count] = num;
                count++;
            }
        }
        return count;
    }
};