def appearance(intervals):
    events = []
    for item in intervals:
        event = intervals[item]
        for i in range(len(event)):
            events.append((event[i], 1 - 2*(i%2)))
    events.sort()
    count = 0
    start = 0
    total_time = 0
    for event in events:
        count += event[1]
        if count == 3:
            start = event[0]
        if count == 2 and start > 0:
            total_time += event[0] - start
            start = 0
    return total_time      

tests = [
     {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
   {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], \
            f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    

