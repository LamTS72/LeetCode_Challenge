class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = list(filter(lambda x: x >= target, hours))
        print(res)
        return len(res)