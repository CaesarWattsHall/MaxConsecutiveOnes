class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        auto r = 0, m1 = 0;
        for (auto n: nums) {
            if (n==1){
            r ++;
            m1 = max(m1, r);
        } else {
            r = 0;
            
        }
        }
    return m1;
    }
};
