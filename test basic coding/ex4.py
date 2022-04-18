import numpy as np
from collections import defaultdict


class ArrIntManage:
    arr_int = np.random.randint(10, size=10)

    def arr(self):
        print(self.arr_int)

    def sum(self):
        return sum(self.arr_int)

    def sum_prime(self):
        prime = []
        for i in self.arr_int:
            c = 0
            for j in range(1, i):
                if i % j == 0:
                    c += 1
            if c == 1:
                prime.append(i)
        print(prime)
        print(sum(prime))

    def find_three_conse_num(self):
        arr = self.arr_int
        for i in range(len(arr) - 2):
            if (arr[i] == arr[i + 1] == arr[i + 2]):
                a = arr[i]
        print([a, a + 1, a + 2])

    # def subs_longest_equal_s(self,s):
    #     for i in self.arr_int:
    #         sum

    def find_subarray_sum(self, Sum):

        prevSum = defaultdict(lambda: 0)
        res = 0
        arr = self.arr_int
        # Sum of elements so far.
        currsum = 0
        for i in range(0, len(arr)):
            currsum += arr[i]
            if currsum == Sum:
                res += 1
            if (currsum - Sum) in prevSum:
                res += prevSum[currsum - Sum]
            prevSum[currsum] += 1
        return res


arr = ArrIntManage()
# arr.arr()
# print(arr.sum())
# arr.sum_prime()
# arr.find_three_conse_num()
print(arr.find_subarray_sum(10))
