def dfs(self):
    res = []

    def traverse(cn):
        if cn is None:
            return
        traverse(cn.left)
        res.append(cn.value)
        traverse(cn.right)

    traverse(self.root)
    return res

def kth_smallest(self, k):
    if self.root is None:
        return None

    res = self.dfs()

    if k < 1 or k > len(res):
        return None

    return res[k - 1]