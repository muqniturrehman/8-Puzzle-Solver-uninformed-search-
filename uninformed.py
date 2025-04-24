class Node:
    def __init__(self, state, parent=None):

        self.state = state
        self.parent = parent 
    
    def __str__(self):
        output = ""
        for i in range(3):
            output += f"{self.state[i]}\n"
        return output

class PuzzleSolver:
    def __init__(self, start, goal):

        self.start = start
        self.goal = goal

    def is_solvable(self, state):

        inversions = 0
        ans = [num for row in state for num in row if num != ' ']
        for i in range(len(ans)):
            for j in range(i + 1, len(ans)):
                if ans[i] > ans[j]:
                    inversions += 1
        return inversions % 2 == 0
            
    def find_space(self, state):

        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    return (i,j)
        
    def find_moves(self, pos):

        x, y = pos
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    
    def is_valid(self, move):

        x, y = move
        return 0 <= x < 3 and 0 <= y < 3
    
    def play_move(self, state, move, space):

        n_state = [row[:] for row in state.state]  
        n_node = Node(n_state, state)
        x, y = move
        sx, sy = space
        n_node.state[x][y], n_node.state[sx][sy] = n_node.state[sx][sy], n_node.state[x][y]
        return n_node
    
    def generate_children(self, state):

        children = []
        space = self.find_space(state.state)
        moves = self.find_moves(space)

        for move in moves:
            if self.is_valid(move):
                child = self.play_move(state, move, space)
                children.append(child)
        return children

    def solve_puzzle_backtracking(self):

        def backtrack(node, visited):
            if node.state == self.goal.state:
                self.disp_solution(node)
                return True
            
            visited.add(str(node.state))
            children = self.generate_children(node)
            
            for child in children:
                if str(child.state) not in visited:
                    if backtrack(child, visited):
                        return True
            return False

        visited = set()
        if not backtrack(self.start, visited):
            print("No solution found.")

    def solve_puzzle_dfs(self):
        
        open_list = [self.start]      
        visited = set()

        while open_list:
            node = open_list.pop()
            if node.state == self.goal.state:
                self.disp_solution(node)
                return
            visited.add(str(node.state))
            children = self.generate_children(node)
            for child in children:
                if str(child.state) not in visited:
                    open_list.append(child)
        print("No solution found.")
    
    def solve_puzzle_bfs(self):

        open_list = [self.start]     
        visited = set()

        while open_list:
            node = open_list.pop(0)
            if node.state == self.goal.state:
                self.disp_solution(node)
                return
            visited.add(str(node.state))
            children = self.generate_children(node)
            for child in children:
                if str(child.state) not in visited:
                    visited.add(str(child.state))
                    open_list.append(child)
        print("No solution found.")
    
    def solve_puzzle_dfid(self):

        def dls(node, depth, visited):
            if node.state == self.goal.state:
                self.disp_solution(node)
                return True
            if depth == 0:
                return False
            
            visited.add(str(node.state))
            children = self.generate_children(node)
            for child in children:
                if str(child.state) not in visited:
                    if dls(child, depth - 1, visited):
                        return True
            return False
        
        depth_limit = 0
        while True:
            print(f"Searching with depth limit: {depth_limit}")
            visited = set()
            if dls(self.start, depth_limit, visited):
                return
            depth_limit += 1

    def disp_solution(self, final_state):
        
        solution_path = []
        current_node = final_state
        while current_node:
            solution_path.append(current_node)
            current_node = current_node.parent

        solution_path.reverse()     
        step = 0
        for node in solution_path:
            print(f"\nStep {step}:")
            print(node)
            step += 1


def main():
    start = Node([[4, 7, 8], [3, 6, 5], [1, 2, ' ']])
    goal = Node([[1, 2, 3], [4, 5, 6], [7, 8, ' ']])

    solver = PuzzleSolver(start=start, goal=goal)
    #solver.solve_puzzle_backtracking()
    #solver.solve_puzzle_dfs()
    #solver.solve_puzzle_bfs()
    solver.solve_puzzle_dfid()

main()