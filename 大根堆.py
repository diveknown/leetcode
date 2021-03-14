        def upadjust(nums):
            childindex = len(nums)-1
            parentindex = (childindex-1)//2
            temp = nums[childindex] #插入的叶子节点值
            while childindex>0 and temp>nums[parentindex]:#子节点大于父节点，上调子节点
                nums[childindex] = nums[parentindex]
                childindex = parentindex
                parentindex = (parentindex-1)//2
            nums[childindex] = temp

        def downadjust(nums,parentindex):
            temp = nums[parentindex]
            childindex = 2*parentindex + 1
            while childindex < len(nums):
                #右孩子值大于左孩子，父节点和大的交换
                if childindex +1 <len(nums) and nums[childindex+1] > nums[childindex]:
                    childindex += 1
                if temp > nums[childindex]:    #父节点小于子节点，不用调整
                    break
                nums[parentindex] = nums[childindex]
                parentindex = childindex
                childindex = childindex*2+1
            nums[parentindex] = temp

        def buildMinHeap(nums):
            for i in range((len(nums)-1)//2,-1,-1):
                downadjust(nums,i)
        
        buildMinHeap(nums)
