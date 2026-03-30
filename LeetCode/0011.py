def maxArea(height):
    left=0
    right=len(height)-1
    water=0
    while left < right:
        mid=right-left
        c_h=min(height[left],height[right])
        water=max(water,(c_h*mid))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return water

