class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0] * 101

        for birth, death in logs:
            population[birth - 1950] += 1
            population[death - 1950] -= 1

        year=1950
        curr_pop=0
        max_pop=0
        
        for i in range(101):
            curr_pop += population[i]
            if curr_pop>max_pop:
                max_pop = curr_pop
                year = 1950 + i        
        return year

