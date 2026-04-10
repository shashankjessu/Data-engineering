from typing import List

students: dict[str,List[int]]= {
    "anirudh":[43,65,21,65,76],
    "vandana": [65,76,12,81,54],
    "nihar":[87,98,78,32,65],
    "sanjay":[76,24,4,45,66,12]
}

#print(dict(sorted(students.items(),key=lambda x : x[1][-1])))

print(dict(sorted(students.items(),key=lambda x : sum(x[1]),reverse=True)))
