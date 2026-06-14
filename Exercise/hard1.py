import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

def solve():
    n = int(input())
    
    parent = [int(input()) for _ in range(n)]
    color = [int(input()) for _ in range(n)]
    
    q = int(input())
    queries = [int(input()) for _ in range(q)]
    
    # Build tree
    tree = [[] for _ in range(n+1)]
    root = 1
    
    for i in range(2, n+1):
        tree[parent[i-1]].append(i)

    # DFS to get max unique path starting from node
    def dfs(node, used):
        if color[node-1] in used:
            return 0
        
        used.add(color[node-1])
        
        best = 0
        for child in tree[node]:
            best = max(best, dfs(child, used))
        
        used.remove(color[node-1])
        
        return 1 + best

    # Process queries
    ans = 0
    for s in queries:
        ans += dfs(s, set())
    
    print(ans % MOD)


solve()