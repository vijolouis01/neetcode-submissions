class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for index in range(len(arr)):
            if index == len(arr) - 1:
                result.append(-1)
            else:
                right = arr[index+1:]
                greatest = max(right)
                result.append(greatest) 
        return result              

        