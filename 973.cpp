#include <vector>
#include <queue>
#include <cmath>
using namespace std;
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int, vector<int>>> pq;
        
        for (vector<int> point : points) {
            pq.push({point[0]*point[0] + point[1]*point[1], {point[0], point[1]}});
            if (pq.size() > k) pq.pop();
        }

        vector<vector<int>> res;
        while (k > 0) {
            pair<int, vector<int>> p = pq.top();
            res.push_back(p.second);
            pq.pop();
            k--;
        }
        
        return res;
    }
};
