#include <vector>
#include <queue>
#include <cmath>
using namespace std;
class Compare {
public:
    bool operator() (vector<int> a, vector<int> b) {
        double dist_a = sqrt(pow(a[0], 2) + pow(a[1], 2));
        double dist_b = sqrt(pow(b[0], 2) + pow(b[1], 2));
        
        return dist_a > dist_b;
    }
};
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>, vector<vector<int>>, Compare> heap;
        
        for (vector<int> point : points) {
            heap.push(point);
        }

        vector<vector<int>> res;
        while (k > 0) {
            res.push_back(heap.top());
            heap.pop();
            k--;
        }
        
        return res;
    }
};
