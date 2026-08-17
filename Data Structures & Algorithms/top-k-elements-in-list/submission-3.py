class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq={}
        for num in nums:
            num_freq[num]=num_freq.get(num, 0)+1
        bucket_freq=[[] for _ in range(len(nums)+1)]
        for num, count in num_freq.items():
            bucket_freq[count].append(num)
        top_freq=[]
        for index in range(len(bucket_freq)-1, -1, -1):
            for num in bucket_freq[index]:
                top_freq.append(num)
                if len(top_freq)==k:
                    return top_freq        


        