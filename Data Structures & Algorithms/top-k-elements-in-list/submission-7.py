class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count=dict()
        for num in nums:
            num_count[num]=num_count.get(num, 0)+1
        bucket=[[] for _ in range(len(nums)+1)]
        for num, count in num_count.items():
            bucket[count].append(num)
        top_k=[]
        for count in range(len(bucket)-1, -1, -1):
            for num in bucket[count]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k       
        