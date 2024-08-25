#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        if (tasks.empty()) return 0;

        priority_queue<int> pq;
        vector<int> map(26);
        for(char i : tasks) {
            map[i - 'A']++;
        }
        for (int i = 0; i < 26; i++) {
            if (map[i]) pq.push(map[i]);
        }

        int t = 0;
        while(!pq.empty()) {
            vector<int> remain;
            int cycle = n + 1;

            while (cycle && !pq.empty()) {
                int max_freq = pq.top();
                pq.pop();
                if (max_freq > 1) {
                    remain.push_back(max_freq - 1);
                }
                t++;
                cycle--;
            }

            for(int count : remain) {
                pq.push(count);
            }
            
            if (pq.empty()) break;

            t += cycle;
        }

        return t;
    }
};