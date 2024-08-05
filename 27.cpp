#include <vector>
using namespace std;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size = nums.size() - 1;
        int i = 0;
        while (i <= size) {
            if (nums[i] == val) {
                swap(nums[i], nums[size]);
                size--;
            } else {
                i++;
            }
        }
        return size + 1;
    }
};