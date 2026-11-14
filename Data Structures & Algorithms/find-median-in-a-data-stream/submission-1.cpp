class MedianFinder {
private:
    priority_queue<int> lower;
    priority_queue<int, vector<int>, greater<int>> upper;
public:
    MedianFinder() {
    }
    
    void addNum(int num) {
        if (lower.size() == upper.size()) {
            if (lower.empty()) {
                lower.push(num);
            } else if (num > upper.top()) {
                upper.push(num);
            } else {
                lower.push(num);
            }
        } else if (lower.size() > upper.size()){
            if (num < lower.top()) {
                upper.push(lower.top());
                lower.pop();
                lower.push(num);
            } else {
                upper.push(num);
            }
        } else {
            if (num > upper.top()) {
                lower.push(upper.top());
                upper.pop();
                upper.push(num);
            } else {
                lower.push(num);
            }
        }
    }
    
    double findMedian() {
        if (lower.size() == upper.size()) {
            return (double)(lower.top() + upper.top())/2;
        } else if (lower.size() > upper.size()) {
            return (double)lower.top();
        } else {
            return (double)upper.top();
        }
    }
};
