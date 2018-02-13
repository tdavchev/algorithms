def dfs_visit(adj, s):
    for v in adj[s]:
        if v not in parent:
            parent[v] = s
            dfs_visit(adj, v)

def dfs(V, adj):
    parent = {}
    for s in V:
        if s not in parent:
            parent[s] = None
            dfs_visit(adj, s)
