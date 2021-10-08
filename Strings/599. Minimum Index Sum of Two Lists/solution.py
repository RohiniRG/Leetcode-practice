class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ind = dict()
        for i in range(len(list1)):
            ind[list1[i]] = i
            
        lowest_ind = float('inf')
        for j in range(len(list2)):
            if list2[j] in ind:
                if lowest_ind > j + ind[list2[j]]:
                    lowest_ind = j + ind[list2[j]]
                    res = [list2[j]]
                elif lowest_ind == j + ind[list2[j]]:
                    res.append(list2[j])
                    
        return res
      
