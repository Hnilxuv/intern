class ManageInt:
    def subsetSumToK(self, arr, n, output, k):
        if n == 0:
            if k == 0:
                output[0][0] = 0
                return 1
            else:
                return 0
        output1 = [[0 for j in range(50)] for i in range(1000)]
        output2 = [[0 for j in range(50)] for i in range(1000)]
        size1 = self.subsetSumToK(arr[1:], n - 1, output1, k - arr[0])
        size2 = self.subsetSumToK(arr[1:], n - 1, output2, k)
        for i in range(size1):
            output[i][0] = output1[i][0] + 1
            output[i][1] = arr[0]
        for i in range(size1):
            for j in range(1, output1[i][0] + 1):
                output[i][j + 1] = output1[i][j]
        for i in range(size2):
            for j in range(output2[i][0] + 1):
                output[i + size1][j] = output2[i][j]
        return size1 + size2

    def countSubsequences(self, arr, n, output, k):
        size = self.subsetSumToK(arr, n, output, k)
        for i in range(size):
            for j in range(1, output[i][0] + 1):
                print(output[i][j], end=' ')
            print()


mi = ManageInt()
arr = [5, 12, 3, 17, 1, 18, 15, 3, 17]
length = 9
output = [[0 for j in range(50)] for i in range(1000)]
k = 6
mi.countSubsequences(arr, length, output, k)