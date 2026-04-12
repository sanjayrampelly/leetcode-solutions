var minDepth = function (root) {
    function dfs(node) {
        if (!node) return Infinity;

        if (!node.left && !node.right) {
            return 1; // leaf node
        }

        let lRes = dfs(node.left);
        let rRes = dfs(node.right);
        return 1 + Math.min(lRes, rRes);
    }

    let res = dfs(root);
    return res === Infinity ? 0 : res;
};
