class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        hS = []
        iS = []
        total = 0
        for index, h in enumerate(height):
            if h == 0: continue
            if len(hS) == 0: 
                hS.append(h)
                iS.append(index)
            elif hS[-1] > h:
                total += (index - iS[-1] - 1) * h
                hS.append(h)
                iS.append(index)
            elif hS[-1] == h:
                total += (index - iS[-1] - 1) * h
                iS[-1] = index
            else:
                preHeight = 0
                while len(hS) > 0 and hS[-1] <= h:
                    total += (index - iS[-1] - 1) * (hS[-1] - preHeight)
                    preHeight = hS[-1]
                    del iS[-1]
                    del hS[-1]
                if len(hS) > 0:
                    total += (index - iS[-1] - 1) * (h - preHeight)
                iS.append(index)
                hS.append(h)
        return total
                    
                
                
        