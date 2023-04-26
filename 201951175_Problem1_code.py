#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Yash Beniwal

import random

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class Random:
    def __init__(self):
        self.randoms = []
        for i in range(10000000):
            self.randoms.append(random.random())

    def get_randoms(self):
        return self.randoms

class State:
    def __init__(self):
        self.s1 = Node(100)
        self.s2 = Node(500)
        self.s3 = Node(1000)
        self.s4 = Node(5000)
        self.s5 = Node(10000)
        self.s6 = Node(50000)
        self.s7 = Node(100000)
        self.s8 = Node(500000)
        self.s9 = Node(1000000)
        self.s10 = Node(5000000)
        self.s1.next = self.s2
        self.s2.next = self.s3
        self.s3.next = self.s4
        self.s4.next = self.s5
        self.s5.next = self.s6
        self.s6.next = self.s7
        self.s7.next = self.s8
        self.s8.next = self.s9
        self.s9.next = self.s10

class Iterate:
    def __init__(self):
        obj = State()
        self.head = obj.s1
        obj1 = Random()
        self.randoms = obj1.get_randoms()
        self.stopper = False
        self.times_visited = {}
        self.value_function = {}
        self.gamma = 1
        self.theta = 0.00005
        self.prob = [1, 0.99, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
        self.itr = 0
        self.cnt = 0

    def print_state_transition(self):
        for k, v in self.times_visited.items():
            print(k, end=' ')
        print()
        for k, v in self.times_visited.items():
            print((v * 100) / self.cnt, end=' ')
        print()

    def get_stopper_state(self):
        return self.stopper

    

    def dfs(self, temp, currState):
        global itr, prob, gamma, TimesVisited, ValueFunction, theta, stopper
        TimesVisited[currState] += 1
        if not temp:
            return (currState, 0)
        maxStateReached = currState
        answerReward = 0
        mx = 0
        oldValue = ValueFunction[currState]
        quitReward = ValueFunction[currState - 1]
        if self.randoms[itr % 10000000] <= prob[currState]:
            self.itr += 1
            nextStateReward = self.dfs(temp.next, currState + 1)
            answerReward = selfprob[currState] * (self.gamma * nextStateReward[1] + temp.val)
            maxStateReached = max(maxStateReached, nextStateReward[0])
            ValueFunction[currState] = (self.ValueFunction[currState] * (self.TimesVisited[currState] - 1) + answerReward) / (self.TimesVisited[currState])
            if abs(oldValue - self.ValueFunction[currState]) < theta:
                self.stopper = True
        return (maxStateReached, max(quitReward, answerReward))


    def cycle():
        global cnt
        cnt += 1
        return dfs(head, 1)

class Solution:
    def solve(self):
        itr = 0
        mp = defaultdict(int)
        mp1 = defaultdict(float)
        obj = iterate()
        while not obj.getStopperState():
            it = obj.cycle()
            mp[it[0]] += 1
            itr += 1
            mp1[it[0]] = (mp1[it[0]] * (obj.cnt - 1) + it[1]) / obj.cnt
        print(itr)
        obj.PrintStateTransition()


    def print_results():
        pr = [(k, v) for k, v in mp.items()]
        pr1 = [(k, v) for k, v in mp1.items()]
        pr.sort()
        pr1.sort()
        for it in pr:
            print(it[0], end=" ")
        print("\n")
        for it in pr:
            print("{:.2f}".format(it[1] * 100 / itr), end=" ")
        print("\n")
        for it in pr1:
            print(it[0], end=" ")
        print("\n")
        for it in pr1:
            print("{:.6f}".format(it[1]), end=" ")
        print("\n")

    
if __name__ == '__main__':
    obj = Solution()
    obj.solve()
    obj.print()
    



