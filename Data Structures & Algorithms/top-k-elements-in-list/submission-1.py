class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_frequency={}
        for num in nums:
            number_frequency[num]=number_frequency.get(num, 0)+1
        bucket_frequency=[[] for _ in range(len(nums)+1)]    
        for number, frequency in number_frequency.items():
            bucket_frequency[frequency].append(number)
        top_frequent_numbers=[]
        for frequency in range(len(bucket_frequency)-1, -1, -1):
            for number in bucket_frequency[frequency]:
                top_frequent_numbers.append(number)
                if len(top_frequent_numbers) == k:
                    return top_frequent_numbers

        