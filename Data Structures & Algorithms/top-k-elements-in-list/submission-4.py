class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=dict()
        for num in nums:
            counts[num]=counts.get(num, 0)+1
        buckets=[[] for _ in range(len(nums)+1)]    
        for num, count in counts.items():
            buckets[count].append(num)
        top_k_freq=[]    
        for index in range(len(buckets)-1, -1, -1):
            for num in buckets[index]:
                top_k_freq.append(num)
                if len(top_k_freq) == k:
                    return top_k_freq   




        