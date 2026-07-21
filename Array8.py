"""
Greedy Algorithm
Gas Station 
The Gas Station problem is a famous Greedy Algorithm interview question. 
It tests your ability to make the best local decision to achieve the global solution.


Q.1 Problem Statement

There are n gas stations arranged in a circular route.

At each gas station:

gas[i] = amount of fuel available.
cost[i] = fuel needed to travel to the next station.

Your task is to find the starting gas station index from which you can complete the entire circle exactly once.

If it's impossible, return -1.

Example
Input:
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output:
3
"""
def can_complete_circuit(gas, cost):
    # If total gas is less than total cost, journey is impossible
    if sum(gas) < sum(cost):
        return -1

    start = 0
    fuel = 0

    for i in range(len(gas)):
        fuel += gas[i] - cost[i]

        # Can't continue from current start
        if fuel < 0:
            start = i + 1
            fuel = 0

    return start


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

print("Starting Station:", can_complete_circuit(gas, cost))

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
Jump Game I 

This is one of the most popular Greedy Algorithm interview questions. It tests whether you can determine if the last index of an array is reachable.



Q.2 You are given an array nums.

Each element represents the maximum number of steps you can jump forward from that position.

Your task is to determine whether you can reach the last index starting from the first index.

Return True if you can reach the end.
Return False otherwise.
Example
Input:
nums = [2,3,1,1,4]

Output:
True


"""
def can_jump(nums):
    max_reach = 0

    for i in range(len(nums)):
        # Current position cannot be reached
        if i > max_reach:
            return False

        # Update the farthest reachable position
        max_reach = max(max_reach, i + nums[i])

    return True


nums = [2, 3, 1, 1, 4]
print("Can Reach End:", can_jump(nums))

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Candy 

The Candy problem is a classic Greedy Algorithm interview question. It is considered one of the harder array problems because you need to satisfy two conditions at the same time.



Q. 3 There are N children standing in a line.

Each child has a rating.

You have to distribute candies according to these rules:

Every child must get at least one candy.
If a child has a higher rating than an adjacent child, they must receive more candies than that neighbor.

Your task is to find the minimum number of candies needed.

"""


print("------------------------------Vivek Learning DSA Python----------------------------------------")

