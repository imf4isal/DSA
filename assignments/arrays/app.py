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

#5 shuffle the array
# def shuffle(self, nums: List[int], n: int) -> List[int]:
#     output = []
#     for i in range(0, len(nums) - n):
#         output.append(nums[i])
#         output.append(nums[i+n])

#     return output

#6 kids with greatest number of candies
# def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#     maximum = max(candies)
#     output = []
#     for i in candies:
#         if(i+extraCandies >= maximum):
#             output.append(True)
#         else:
#             output.append(False)
#     return output

# 8. How Many Numbers Are Smaller Than the Current Number(10minutes)
# def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#     output = []

#     for numcurrent in nums:

#         c = 0
#         for num in nums:
#             if num < numcurrent:
#                 c = c + 1
#         output.append(c)

#     return output

# 9. Create Target Array in the Given Order (15 minutes)
# def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
#     targetArray = []
#     for i, element in enumerate(index):
#         targetArray.insert(element, nums[i])

#     return targetArray

# 10. [Check if the Sentence Is Pangram](10m)
# def checkIfPangram(self, sentence: str) -> bool:
#     alpha = [
#         "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
#         "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
#     ]

#     sen = sentence.lower()

#     output = False
#     for alp in alpha:
#         for ltr in sen:
#             if (alp == ltr):
#                 output = True
#     return output

# 11. [Count Items Matching a Rule]

# def countMatches(self, items: List[List[str]], ruleKey: str,
#                  ruleValue: str) -> int:
#     itm = ["type", "color", "name"]

#     typ = itm.index(ruleKey)

#     count = 0
#     for item in items:
#         if (item[typ] == ruleValue):
#             count = count + 1

#     return count

# 12. [Find the Highest Altitude]
# def largestAltitude(self, gain: List[int]) -> int:

#     altitudes = [0]

#     for g in gain:

#         lastalt = len(altitudes) - 1
#         altitudes.append(altitudes[lastalt] + g)

#     return max(altitudes)

# 13. [Flipping an Image]
# def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

#     output = []
#     for img in image:
#         flip = img[::-1]
#         invert = []
#         for n in flip:
#             if (n == 0):
#                 invert.append(1)
#             else:
#                 invert.append(0)

#         output.append(invert)

#     return output

# def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

#     output = []
#     for img in image:
#         output.append(img[::-1])
#     for i in output:
#         for j in range(len(i)):
#             if (i[j] == 1):
#                 i[j] = 0
#             else:
#                 i[j] = 1
#     return output

# 18. [Add to Array-Form of Integer]
# def addToArrayForm(self, num: List[int], k: int) -> List[int]:

#     numStr = [str(int) for int in num]

#     total = str(int("".join(numStr)) + k)

#     output = []

#     for i in total:
#         output.append(i)

#     return output

# 21. [Two Sum]
# def twoSum(self, nums: List[int], target: int) -> List[int]:

#     output = []
#     for i in range(0, len(nums)):

#         for j in range(i + 1, len(nums)):
#             if (nums[i] + nums[j] == target):
#                 output.append(i)
#                 output.append(j)
#     return output

# 22. [Find N Unique Integers Sum up to Zero]
# def sumZero(self, n: int) -> List[int]:

#     output = []

#     if (n % 2 != 0):
#         output.append(0)

#     for i in range(1, int(n / 2) + 1):
#         output.append(i)
#         output.append(-1 * i)
#     return output
