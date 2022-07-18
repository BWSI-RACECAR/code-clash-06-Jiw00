"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #6 - Longest Distance Between Checkpoints (checkpoints.py)


Author: Chris Lai

Difficulty Level: 3/10

Prompt: The Grand Prix is an obstacle course for the RACECAR. Each of the RACECARs must traverse the course 
and navigate through checkpoints. At the beginning of each obstacle, there will be a checkpoint, at which the 
RACECAR can stop to refuel. Before the course starts, each competitor is given an array of values that indicate 
the distance of these checkpoints (in meters) relative to the starting line. In order to prepare your RACECAR 
for the final race, you want to calculate the longest distance between two checkpoints such that your car has 
enough fuel to last the entire leg.

Given an array of checkpoint distance values, return an integer to represent the longest distance between two checkpoints.

Constraints: All numbers in the array “n” will be integers 10^9 >= n >= 0. Assume the number of items in the 
array “k” will be 10^9 >= k > 0. You may not use the Python sort() method.

Test Cases:
Input: [0, 3, 4, 9] ; Output: 5
Input: [10, 8, 4, 1] ; Output: 4
Input: [5, 0, 3, 6] ; Output: 3
"""

from pyparsing import java_style_comment


class Solution:
    def longestdistance(self, checkpoints):
        # type checkpoints: list
        # return type: int
        distance = 0
        # TODO: Write code below to return an int with the solution to the prompt
        for i in range(0, len(checkpoints)):
            pos = i
            for j in range(i, len(checkpoints)):
                if checkpoints[j] < checkpoints[i]:
                    pos = j
        
            temp = checkpoints[pos]
            checkpoints[pos] = checkpoints[i]
            checkpoints[i] = temp
        print(checkpoints)
        for i in range(0, len(checkpoints)-1):
            temp = checkpoints[i+1] - checkpoints[i] 
            if temp > distance:
                distance = temp
        
        return distance


def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.longestdistance(array)
    print(ans)

if __name__ and "__main__":
    main()