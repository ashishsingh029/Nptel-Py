def solution(marks):
    ### Enter your solution below this line
    ### Indent your entire code by one unit (4 spaces) to the right
    n = len(marks)
    for i in range(n-1):
        for j in range(n-i-1):
            if marks[j] > marks[j+1]:
                marks[j], marks[j+1] = marks[j+1], marks[j]
    if n%2 != 0:
        median = marks[n//2]
    else:
        median = (marks[n//2] + marks[n//2 - 1]) / 2
### Enter your solution above this line
    return median
marks_input = input()
# Extracting numeric values from the input string
marks = [float(mark.strip()) for mark in marks_input.split(',') if mark.strip().isdigit()]
result = solution(marks)
print(result)