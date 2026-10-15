class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tall = -1
        for index in range(len(arr)-1, -1, -1):
            current = arr[index]
            arr[index] = tall
            tall = max(tall, current)
        return arr    

        