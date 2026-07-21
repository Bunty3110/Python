# valid bst
def is_valid_bst(self):
    results=self.dfs_in_order()
    if results==sorted(results):
        return True
    return False