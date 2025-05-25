"""
Problem 2: Merge Intervals
Question: Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals.
"""
intervals = [[1, 3], [2, 6], [15, 18], [8, 10]]

def test_merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    merged = intervals[0] #Get the last merged interval , start witht the first interval


    for current in intervals[1:]:
        #Current gets us the next array to be compared with the merged intervals lets say next current is [2, 6]
        last  = merged[-1]#  merged[-1] gets is -3 last element
        if current <= last:


test_merge_intervals(intervals)