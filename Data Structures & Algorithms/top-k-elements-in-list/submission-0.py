class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_count={}
        for num in nums:
            dict_count[num]=dict_count.get(num, 0)+1
        frequencies=[[] for _ in range(len(nums)+1)]
        for num, count in dict_count.items():
            frequencies[count].append(num)
        answer=[]
        for index in range(len(frequencies)-1, 0, -1):
            for num in frequencies[index]:
                answer.append(num)
                if len(answer)==k:
                    return answer   
        