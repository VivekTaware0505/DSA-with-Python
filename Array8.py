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


