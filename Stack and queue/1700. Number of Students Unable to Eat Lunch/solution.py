class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0
        while len(students):
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                counter = 0
            else:
                counter += 1
                students.append(students.pop(0))
                
                if counter >= len(students):
                    break
                
        return len(students)
    
