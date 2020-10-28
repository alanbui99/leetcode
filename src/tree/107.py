class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.dict = collections.defaultdict(list)
        self.dfs(root, 0)
        return self.dict.values()[::-1]

    def dfs(self, root, level):
        if root is None:
            return
        self.dict[level].append(root.val)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
