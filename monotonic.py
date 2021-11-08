def is_monotonic(nums):
    a=sorted(nums)
    b=sorted(nums,reverse=True)
    if nums !=a and nums !=b:
        return False
    else:
        return True
