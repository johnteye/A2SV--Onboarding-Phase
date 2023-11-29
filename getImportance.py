"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # def to_list(employee):
        #     return [employee.id, employee.importance, employee.subordinates]

        graph = defaultdict(list)
        for employee in employees:
            graph[employee.id] = employees.index(employee)
        
        def dfs(employee, res):
            if not employee:
                return 0

            for sub in employee.subordinates:

                res = dfs(employees[graph[sub]], res + employees[graph[sub]].importance)

            return res 


        return dfs(employees[graph[id]], employees[graph[id]].importance)
