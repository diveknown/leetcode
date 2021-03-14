        #下面是手写大根堆,ps:本题没有插入
        def upadjust(nums):                                                   #插入元素时，向上调整
            childindex = len(nums)-1                                          #插入的叶子节点值为最后一个，childindex
            parentindex = (childindex-1)//2
            temp = nums[childindex]                                          
            while childindex>0 and temp>nums[parentindex]:                    #子节点大于父节点，上调子节点，下调父节点
                nums[childindex] = nums[parentindex]
                childindex = parentindex
                parentindex = (parentindex-1)//2
            nums[childindex] = temp

        def downadjust(nums,parentindex):                                     #向下调整，建堆和出堆调整时
            temp = nums[parentindex]
            childindex = 2*parentindex + 1
            while childindex < len(nums):
                #右孩子值大于左孩子，父节点和大的交换
                if childindex +1 <len(nums) and nums[childindex+1] > nums[childindex]:
                    childindex += 1
                if temp > nums[childindex]:                                       #父节点大于子节点，不用调整
                    break
                nums[parentindex] = nums[childindex]
                parentindex = childindex
                childindex = childindex*2+1
            nums[parentindex] = temp

        def buildMinHeap(nums):
            for i in range((len(nums)-1)//2,-1,-1):
                downadjust(nums,i)
