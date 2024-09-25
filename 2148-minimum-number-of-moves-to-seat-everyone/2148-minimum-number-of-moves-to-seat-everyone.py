class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = [abs(i - j) for i,j in zip(seats, students)]
        return sum(res)