class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_gas = 0
        total_gas = 0
        start_idx = 0
        for i, g in enumerate(gas):
            curr_gas += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]
            print(total_gas)
            if curr_gas < 0:
                curr_gas = 0
                start_idx = i + 1
        return start_idx if total_gas >= 0 else -1
