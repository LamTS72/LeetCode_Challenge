class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        stack_m = []
        stack_s = []
        flag = False
        for i in range(len(arr2)):
            compare_e = arr2[i]
            for item in arr1:
                if compare_e == item:
                    stack_m.append(item)
                elif compare_e != item and item not in arr2 and flag == False:
                    stack_s.append(item)
            flag = True

        print("M: ",stack_m)
        print("S: ",stack_s)
        arr1 = stack_m + sorted(stack_s)
        return arr1

        