class Node:
  #constructor
  def __init__(self,weight,name):
    self.weight=weight
    self.name=name

#adjacency list
a=Node(0,'a')
b=Node(3,'b')
c=Node(1,'c')
d=Node(0,'d')

graph2={a:([b,c]),
        b:([c]),
        c:([d]),
        d:([a])}
print(graph2)
starting_point= d

def get_sum(graph):
  sum=0
  for items in graph:
    sum+=items.weight
  return sum

operation='clean'
operand='dirt'
def operate(operation,operand,node):
  if node.weight>0:
    node.weight-=1
    print(f'{operation}ing {operand} at {node.name}\n{node.weight}')

    print(f'Starting at {starting_point.name}')


def max_attr(graph):
  return max(graph,key=lambda x:x.weight)
target=max_attr(graph2)

#find path
visited = set()
def dfs(visited, graph2,node,target):
  sum=get_sum(graph2)
  while sum>0:
    if node.name == target.name:#find target
      while node.weight>0:
        operate('clean','dirt',node)#operate on target until it has no weight
      target=max_attr(graph2)#find new target
      # for neighbor in graph2[node]:#repeat
      #   dfs(visited,graph2,neighbor,target)
    else:
      for neighbor in graph2[node]:#repeat
          dfs(visited,graph2,neighbor,target)
    sum=get_sum(graph2)
      

dfs(visited,graph2,starting_point,target)
