/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
 
 /**
  * suppose newInterval(sn,en), intervals[i](si,ei);
  */
class Solution {
public:
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        vector<Interval> result;
        int size = intervals.size();
        if(size == 0){
            result.push_back(newInterval);
            return result;
        }
        int start = 0;
        bool merging = false;
        for(int i = 0; i < size; i++){
            if(intervals[i].start > newInterval.end){
                //sn < en < si < ei
                if(!merging){
                    //there is no need to merge, just insert the newInterval 
                    //into the proper position
                    result.push_back(newInterval);
                    
                }else{
                    Interval in(start,newInterval.end);
                    result.push_back(in);
                }
                for(int j = i; j < size; j++){
                    result.push_back(intervals[j]);
                }
                return result;
            }else if(intervals[i].end < newInterval.start){
                //si < ei < sn < en
                result.push_back(intervals[i]);
            }else if(intervals[i].end >= newInterval.end && intervals[i].start <= newInterval.start){
                //si <= sn < en <= ei
                for(int j = i; j < size; j++){
                    result.push_back(intervals[j]);
                }
                return result;
            }else if(intervals[i].end <= newInterval.end){
                if(merging){
                    continue;
                }
                if(intervals[i].start < newInterval.start){
                    //si < sn < ei <= en
                    start = intervals[i].start;
                }else{
                    //sn <= si < ei <= en
                    start = newInterval.start;
                }
                merging = true;
            }else{
                if(merging){
                    Interval in(start,intervals[i].end);
                    result.push_back(in);
                }else{
                    Interval in(newInterval.start,intervals[i].end);
                    result.push_back(in);
                }
                for(int j = i+1; j < size; j++){
                    result.push_back(intervals[j]);
                }
                return result;
            }
        }
        if(merging){
            Interval in(start,newInterval.end);
            result.push_back(in);
        }else{
            result.push_back(newInterval);
        }
        return result;
    }
};