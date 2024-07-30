class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1

        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True )

        top_k = [item[0] for item in sorted_count[:k]]

        return top_k