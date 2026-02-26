class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.lowerBound(nums,target)

    def lowerBound(self,a,target):
        lo,hi=0,len(a)
        while(lo<hi):
            mid=lo+(hi-lo)//2

            if a[mid]>=target:
                hi=mid
            else:
                lo=mid+1 

        return lo