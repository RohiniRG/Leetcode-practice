lass Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def util(root):
            if root is None:
                q.append("None")
            else:
                q.append(str(root.val))
                util(root.left)
                util(root.right)
        
        q = []
        util(root)
        return ' '.join(q)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def util():
            curr = next(data)
            if curr == "None":
                return None
            else:
                newnode = TreeNode(int(curr))
                newnode.left = util()
                newnode.right = util()
                return newnode
            
        data = iter(data.split(' '))
        return util()

