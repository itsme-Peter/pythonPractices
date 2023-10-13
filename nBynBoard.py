### The problem of placing n queens on an n x n board


class solution:
    def solve(self,n):
        solutions = []
        state = []
        self.search(state,solutions,n)

        return solutions

    def is_valid_state(self,state,n):
        # check if its a valid solution
        return len(state) == n

    def get_candidates(self,state,n):
        if not state:
            return range(n)

        # find the next positon in the state to populate
        position = len(state)
        candidates = set(range(n))
        
        #prune down candidates that place the queen into attacks
        for row , col in enumerate(state):
            # discard column index if occupied

            candidates.discard(col)
            dist = position - row

            # discard diagonals
            candidates.discard(col + dist)
            candidates.discard(col - dist)

        return candidates
    
    def search(self,state,solutions,n):
        if self.is_valid_state(state,n):
            state_string = self.state_to_string(state)
            solutions.append(state_string)
            return

        for candidate in self.get_candidates(state,n):

            state.append(candidate)
            self.search(state,solutions,n)
            state.pop()
    
    def state_to_string(self,state,n):
        # [1,3,0,1] ==> [".Q..","...Q","Q...",".Q.."]

        ret = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n - i -1)
            ret.append(string)

        return ret
    
sol = solution()

print(sol.solve(3))
            


