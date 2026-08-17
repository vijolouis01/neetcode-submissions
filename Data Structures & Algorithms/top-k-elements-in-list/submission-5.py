class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=count.get(num, 0)+1
        bucket=[[] for _ in range(len(nums)+1)]
        for num, value in count.items():
            bucket[value].append(num)
        top_k=[]    
        for index in range(len(bucket)-1, -1, -1):
            for num in bucket[index]:
                top_k.append(num)
                if len(top_k)==k:
                    return top_k                    




        