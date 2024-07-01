class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, n):
                self.representative = list(range(n + 1))
                self.size = [1] * (n + 1)
                self.components = n

            def find(self, x):
                if self.representative[x] == x:
                    return x
                self.representative[x] = self.find(self.representative[x])
                return self.representative[x]

            def union(self, x, y):
                x = self.find(x)
                y = self.find(y)

                if x == y:
                    return 0
                if self.size[x] > self.size[y]:
                    self.size[x] += self.size[y]
                    self.representative[y] = x
                else:
                    self.size[y] += self.size[x]
                    self.representative[x] = y

                self.components -= 1
                return 1

            def is_fully_connected(self):
                return self.components == 1

        alice_graph = UnionFind(n)
        bob_graph = UnionFind(n)
        edges_req = 0

        for edge in edges:
            if edge[0] == 3:
                edges_req += alice_graph.union(edge[1], edge[2]) | bob_graph.union(
                    edge[1], edge[2]
                )
        for edge in edges:
            if edge[0] == 1:
                edges_req += alice_graph.union(edge[1], edge[2])
            else:
                edges_req += bob_graph.union(edge[1], edge[2])

        if bob_graph.is_fully_connected() and alice_graph.is_fully_connected():
            return len(edges) - edges_req
        return -1
