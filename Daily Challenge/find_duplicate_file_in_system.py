# Day 7

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content = dict()
        for file_str in paths:
            f = file_str.split(" ")
            dir = f[0]
            for i in range(1, len(f)):
                file_name, file_content = f[i].split("(")
                file_content = file_content[:-1]
                if file_content not in content:
                    content[file_content] = [dir+"/"+file_name]
                else:
                    content[file_content].append(dir+"/"+file_name)
        
        result = [i for i in content.values() if len(i) > 1]
        return result

# RESULTS:
# Runtime: 155 ms, faster than 49.83% of Python3 online submissions for Find Duplicate File in System.
# Memory Usage: 23.7 MB, less than 76.61% of Python3 online submissions for Find Duplicate File in System.

