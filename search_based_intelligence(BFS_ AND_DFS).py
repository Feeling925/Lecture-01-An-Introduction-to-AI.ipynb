# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:39:54 2018

@author: Administrator
"""
import networkx
graph={
       'A':'B B B C',
       'B':'A C',
       'C':'A B D E',
       'D':'C',
       'E':'C F',
       'F':'E'
       }
       
       
for k in graph:
    graph[k] = set(graph[k].split())
#非空数值均可作为Bool类型True
print('元素' in set('1 2 3 4 5 6 元素'.split()))
#集合通过split后不维持之前的顺序，但也不是随机的
for element in set('1 2 3 4 5 6 7 8 9 10 100000 元素'.split()):
    print(element)
print(graph)
Graph = networkx.Graph(graph)
networkx.draw(Graph, with_labels=True)

#Breadth First Search
seen = set()
need_visited = ['A']
while need_visited:
    node = need_visited.pop(0)
    if node in seen:
        print('{} has been seen'.format(node))
        continue
    print(' I am looking at : {}'.format(node))
    need_visited += graph[node]
    seen.add(node)
#Depth First Search
#定义无向图
graph_long = {
              '1':'2 7',
              '2':'3 1',
              '3':'2 4',
              '4':'3 5',
              '5':'4 6 10',
              '6':'5',
              '7':'1 8',
              '8':'7 9',
              '9':'8 10',
              '10':'5 9 11',
              '11':'10 12',
              '12':'11'
              }
              
for n in graph_long:
    graph_long[n] = graph_long[n].split()
    networkx.draw(Graph_long, with_labels=True) 
#合并广度优先和深度优先解法
def search(graph, concat_func):
    seen = set()
    need_visited = ['1']   
    
    while need_visited:
        node = need_visited.pop(0)
        if node in seen: 
            print('{} has been seen'.format(node))
            continue
        print('   I am looking at : {}'.format(node))
        seen.add(node)
        new_discoveried = graph[node]        
        need_visited = concat_func(new_discoveried, need_visited)
def treat_new_discover_more_important(new_discoveried, need_visited):
    return new_discoveried + need_visited

def treat_already_discoveried_more_important(new_discoveried, need_visited):
    return need_visited + new_discoveried            
              
           
              
              
              
              
              
              
              
              
              