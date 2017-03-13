
"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm 
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "dfs"
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    explored = set()
    frontier = []
    start_state = problem.getStartState()
    frontier.append(start_state)
    parent_hash = {}
    parent_hash[start_state] = (None, None)

    def get_path(state):
        path_stack = util.Stack()
        actions = []
        current = state
        while parent_hash[current][0] is not None:
            path_stack.push(parent_hash[current][0])
            current = parent_hash[current][1]
        while not path_stack.isEmpty():
            actions.append(path_stack.pop())

        return actions

    while len(frontier):
        node = frontier.pop()
        if problem.isGoalState(node):
            return get_path(node)
        explored.add(node)
        for state, action, _ in problem.getSuccessors(node):
            if state not in explored and state not in frontier:
                parent_hash[state] = (action, node)
                frontier.append(state)


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    explored = set()
    frontier = util.Queue()
    start_state = problem.getStartState()
    frontier.push(start_state)
    parent_hash = {}
    parent_hash[start_state] = (None, None)

    def get_path(state):
        path_stack = util.Stack()
        actions = []
        current = state
        while parent_hash[current][0] is not None:
            path_stack.push(parent_hash[current][0])
            current = parent_hash[current][1]
        while not path_stack.isEmpty():
            actions.append(path_stack.pop())

        return actions

    while not frontier.isEmpty():
        node = frontier.pop()
        if problem.isGoalState(node):
            return get_path(node)
        explored.add(node)
        for state, action, _ in problem.getSuccessors(node):
            if state not in explored and state not in frontier.list:
                parent_hash[state] = (action, node)
                frontier.push(state)

  
      
def uniformCostSearch(problem):
    "Search the node of least total cost first. "

    start_state = problem.getStartState()
    parent_hash = {}
    parent_hash[start_state] = (None, None, 0)

    def get_priority(state):
        return parent_hash[state][2]

    def get_path(state):
        path_stack = util.Stack()
        actions = []
        current = state
        while parent_hash[current][0] is not None:
            path_stack.push(parent_hash[current][0])
            current = parent_hash[current][1]
        while not path_stack.isEmpty():
            actions.append(path_stack.pop())

        return actions

    explored = set()
    frontier = util.PriorityQueueWithFunction(get_priority)
    frontier.push(start_state)

    while not frontier.isEmpty():
        node = frontier.pop()
        if problem.isGoalState(node):
            return get_path(node)
        explored.add(node)
        for state, action, cost in problem.getSuccessors(node):
            if state not in explored and state not in frontier.heap:
                parent_hash[state] = (action, node, parent_hash[node][2] + cost)
                frontier.push(state)

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    parent_hash = {}
    parent_hash[start_state] = (None, None, 0)
    #goal = problem.goal
    def get_priority(state):
        return parent_hash[state][2] + heuristic(state, problem)

    def get_path(state):
        path_stack = util.Stack()
        actions = []
        current = state
        while parent_hash[current][0] is not None:
            path_stack.push(parent_hash[current][0])
            current = parent_hash[current][1]
        while not path_stack.isEmpty():
            actions.append(path_stack.pop())

        return actions

    explored = set()
    frontier = util.PriorityQueueWithFunction(get_priority)
    frontier.push(start_state)

    while not frontier.isEmpty():
        node = frontier.pop()
        if problem.isGoalState(node):
            return get_path(node)
        explored.add(node)
        for state, action, cost in problem.getSuccessors(node):
            if state not in explored and state not in frontier.heap:
                parent_hash[state] = (action, node, parent_hash[node][2] + cost)
                frontier.push(state)
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
