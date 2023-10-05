"""
Code to run and test all search algorithms.
"""

from a_star import a_star_search
from bfs import breadth_first_search
from dfs import depth_first_search
from tests import dis_map2, dis_mapM, time_map1, time_map2, time_mapM, time_mapT

if __name__ == "__main__":
    path = breadth_first_search(time_map1, "John_Stevens", "Mariana_Cardoso")
    print(path)
    assert path == ["John_Stevens", "John_Doe", "Raj_Gupta", "Mariana_Cardoso"]
    path = depth_first_search(time_mapT, "Alex_Robbinson", "Aaron_Stone")
    print(path)
    assert path == ["Alex_Robbinson", "Walter_Walker", "Sarah_Parker", "Aaron_Stone"]
    path = a_star_search(dis_map2, time_map2, "John_Doe", "Alex_Robbinson")
    print(path)
    assert path == ["John_Doe", "John_Stevens", "Walter_Walker", "Alex_Robbinson"]
    path = a_star_search(dis_mapM, time_mapM, "Hannah_Mullard", "Alex_Robbinson")
    print(path)
    assert path == [
        "Hannah_Mullard",
        "David_Stone",
        "Catherine_Stevens",
        "Benjamin_Walker",
        "Alex_Robbinson",
    ]
