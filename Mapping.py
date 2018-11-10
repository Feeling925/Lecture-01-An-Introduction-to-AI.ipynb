# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 21:26:07 2018

@author: Administrator
"""

BJ = 'Beijing'
SZ = 'Shenzhen'
GZ = 'Guangzhou'
WH = 'Wuhan'
HLJ = 'Heilongjiang'
NY = 'Newyork'
CM = 'Chianmai'
SG = 'Singapore'

air_route = {
             BJ: {SZ, GZ, WH, HLJ, NY},
             GZ: {WH, BJ, CM, SG},
             SZ:{BJ, SG},
             WH:{BJ, GZ},
             HLJ:{BJ},
             CM:{GZ},
             NY:{BJ}
             }
air_route = networkx.Graph(air_route)
networkx.draw(air_route, with_labels=True)


def search_destination(graph, start, destination):
    pathes = [[start]]
    seen = set()
    chosen_pathes = []
    while pathes:
        path = pathes.pop(0)
        frontier = path[-1]
        if frontier in seen: continue
        # get new lines
        
        for city in graph[frontier]:
            new_path = path + [city]
            pathes.append(new_path)
            if city == destination: return new_path
        
        seen.add(frontier)
    return chosen_pathes

def draw_route(cities):
    return ' ✈️ -> '.join(cities)
print(draw_route(search_destination(air_route, SZ, CM)))







