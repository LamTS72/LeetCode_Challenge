class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats = sorted(seats)
        students = sorted(students)
        sum_res = 0
        for i in range(len(seats)):
            sum_res += abs(seats[i] - students[i])

        return sum_res