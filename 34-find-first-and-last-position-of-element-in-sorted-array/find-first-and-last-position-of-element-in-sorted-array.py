class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb=self.lowerBound(nums,target)
        ub=self.UpperBound(nums,target)

        if lb<len(nums) and nums[lb]==target:
            return [lb,ub-1]

        return [-1,-1]




    def lowerBound(self,a,target):
        lo,hi=0,len(a)
        while(lo<hi):
            mid=lo+(hi-lo)//2

            if a[mid]>=target:
                hi=mid
            else:
                lo=mid+1 

        return lo


    def UpperBound(self,a,target):
        lo,hi=0,len(a)
        while(lo<hi):
            mid=lo+(hi-lo)//2

            if a[mid]>target:
                hi=mid
            else:
                lo=mid+1 

        return lo


        