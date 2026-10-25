import sys

goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def move_left( state ):
    new_state = state[:]
    index = new_state.index( 0 )
    if index not in [0, 3, 6]:
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None

def move_right( state ):
    new_state = state[:]
    index = new_state.index( 0 )
    if index not in [2, 5, 8]:
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None

def move_up( state ):
    new_state = state[:]
    index = new_state.index( 0 )
    if index not in [0, 1, 2]:
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None

def move_down( state ):
    new_state = state[:]
    index = new_state.index( 0 )
    if index not in [6, 7, 8]:
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None

def create_node( state, parent, operator, depth, cost ):
    return Node( state, parent, operator, depth, cost )

def expand_node( node, nodes ):
    expanded_nodes = []
    expanded_nodes.append( create_node( move_up( node.state ), node, "Up", node.depth + 1, node.cost + 1 ) )
    expanded_nodes.append( create_node( move_down( node.state ), node, "Down", node.depth + 1, node.cost + 1 ) )
    expanded_nodes.append( create_node( move_left( node.state ), node, "Left", node.depth + 1, node.cost + 1 ) )
    expanded_nodes.append( create_node( move_right( node.state), node, "Right", node.depth + 1, node.cost + 1 ) )
    expanded_nodes = [n for n in expanded_nodes if n.state != None]
    return expanded_nodes
    

def bfs( start, goal ):
    nodes = []
    nodes_expanded = 0
    visited_nodes = []
    nodes.append( create_node( start, None, None, 0, 0 ) )
    while True:
        if len( nodes ) == 0: return None
        nodes_expanded += 1
        node = nodes.pop(0)
        visited_nodes.append(node.state)
        
        if node.state == goal:
            moves = []
            temp = node
            while True:
                if temp.operator is not None:
                    moves.insert(0, temp.operator)
                if temp.depth <= 1: break
                temp = temp.parent
            return moves, nodes_expanded                
            
        exp_ans = expand_node( node, nodes )
        exp_ans = [n for n in exp_ans if n.state not in visited_nodes]
        nodes.extend( exp_ans )

def dfs( start, goal ):
    depth_limit = 10
    nodes = []
    nodes_expanded = 0
    visited_nodes = []
    nodes.append( create_node( start, None, None, 0, 0 ) )
    while True:
        if len( nodes ) == 0: return None
    
        node = nodes.pop(0)
        visited_nodes.append(node.state)

        if node.state == goal:
            moves = []
            temp = node
            while True:
                if temp.operator is not None:
                    moves.insert(0, temp.operator)
                if temp.depth <= 1: break
                temp = temp.parent
            return moves, nodes_expanded            
            
        if node.depth < depth_limit:
            expanded_nodes = expand_node( node, nodes )
            expanded_nodes = [n for n in expanded_nodes if n.state not in visited_nodes]
            nodes_expanded = len(expanded_nodes) + nodes_expanded
                
            expanded_nodes.extend( nodes )
            nodes = expanded_nodes

def a_star( start, goal ):
    nodes = []
    nodes_expanded = 0
    visited_nodes = []
    nodes.append( create_node( start, None, None, 0, 0 ) )
    while True:
        if len( nodes ) == 0: return None
        nodes.sort(key=lambda x: x.depth + h(x.state, goal_state))
        nodes_expanded += 1
        node = nodes.pop(0)
        visited_nodes.append(node.state)
        
        if node.state == goal:
            moves = []
            temp = node
            while True:
                if temp.operator is not None:
                    moves.insert( 0, temp.operator )
                if temp.depth <= 1: break
                temp = temp.parent
            return moves, nodes_expanded 
            
        exp_ans = expand_node( node, nodes )
        exp_ans = [n for n in exp_ans if n.state not in visited_nodes]
        nodes.extend( exp_ans )

def h( state, goal ):
    score = 0
    for i in range( len( state ) ):
        if state[i] != goal[i]:
            score = score + 1
    return score

class Node:
    def __init__( self, state, parent, operator, depth, cost ):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost

def temp_func( start, goal, method ):
    result = None
    if method == 'bfs':
        result = bfs(start, goal)
    elif method == 'dfs':
        result = dfs( start, goal )
    elif method == 'ast':
        result = a_star( start, goal )
    else:
        print("Invalid method")
        exit()
    return result

def main():
    # Menggunakan nilai default jika argumen kurang agar tidak error index out of range
    method = sys.argv[1] if len(sys.argv) > 1 else 'bfs'
    board = sys.argv[2] if len(sys.argv) > 2 else '1,2,5,3,4,0,6,7,8'
    
    board_split = board.split(',')
    starting_state = [int(i) for i in board_split]
    
    if len(starting_state) == 9: 
        if starting_state == goal_state:
            print("Start node was the goal!")
            return

        result = temp_func( starting_state, goal_state, method )
        if result == None:
            print("No solution found")
        else:
            file = open("output.txt","w")
            file.write("path_to_goal:" + str(result[0]) + "\n")
            file.write("cost_of_path:" + str(len(result[0])) + "\n")
            file.write("search_depth:" + str(len(result[0])) + "\n")
            file.close()

            print("Result is", result[0])
            print(len(result[0]), "moves")
            print("Nodes expanded", result[1])
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()