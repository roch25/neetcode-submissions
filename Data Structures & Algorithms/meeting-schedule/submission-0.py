"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        end = 0
        for i in sorted(intervals, key=lambda x: x.start):
            print(i.start, end, i.start > end)
            if i.start < end:
                return False
            end = i.end
            
        return True
