#1
# def buildArray(self, nums: List[int]) -> List[int]:
#     ans = []

#     for i in nums:
#         ans.append(nums[i])

#     return ans
#2
# def getConcatenation(self, nums: List[int]) -> List[int]:
#     nums2 = nums

#     nums3 = nums + nums2

#     return nums3

# running sum of 1d array
# def runningSum(self, nums: List[int]) -> List[int]:
#     output = []

#     for i in range(0, len(nums)):
#         sum = 0
#         for j in range(0, i + 1):
#             sum += nums[j]
#         output.append(sum)
#     return output

#richest customer wealth
# def maximumWealth(self, accounts: List[List[int]]) -> int:
#     wealthList = []
#     for i in range(0, len(accounts)):
#         sum = 0

#         for j in range(0, len(accounts[i])):
#             sum += accounts[i][j]

#         wealthList.append(sum)

#     return max(wealthList)
