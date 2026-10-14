class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        count  = 0
        for index in range(len(arr)-1, -1, -1):
            current = arr[index]
            arr[index] = largest
            largest = max(current, largest)
        return arr    

        