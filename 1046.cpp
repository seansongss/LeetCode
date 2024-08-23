#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> heap;
        for (int stone : stones) {
            heap.push(stone);
        }
        while (heap.size() > 1) {
            int max = heap.top();
            heap.pop();
            int second_max = heap.top();
            heap.pop();
            if (max - second_max > 0) {
                heap.push(max - second_max);
            }
        }
        
        if (heap.empty()) return 0;

        return heap.top();
    }
};