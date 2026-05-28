class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        starts = set()
        visited = set()
        
        for num in nums:
            if num not in visited:
                if num - 1 not in nums:
                    starts.add(num)
                    visited.add(num)
                else:
                    n = num
                    while n not in visited:
                        if n - 1 not in nums:
                            starts.add(n)
                            visited.add(n)
                            break
                        else:
                            visited.add(n)
                            n = n - 1
        print(starts)
        print(visited)

        max_ = 1
        for start in starts:
            print(f"Start: {start}")
            s = start
            while s in nums:
                print(s)
                s += 1
            max_ = max(max_, s - start)
        return max_