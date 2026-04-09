var isCousins = function (root, x, y) {
    let xp, yp
    let xd, yd

    function dfs(node, p, depth) {
        if (!node) return;

        if (node.val === x) {
            xp = p
            xd = depth
        }
        if (node.val === y) {
            yp = p
            yd = depth
        }

        dfs(node.left, node, depth+1);
        dfs(node.right, node, depth+1);
    }

    dfs(root, null, null)

    return (xp !== yp) && (xd === yd)
};

// var isCousins3333 = function (root, x, y) {
//     let op = {};
//     var rec = function (r, d) {
//         if (r.left) {
//             op[r.left.val] = { p: r.val, d };
//             rec(r.left, d + 1);
//         }
//         if (r.right) {
//             op[r.right.val] = { p: r.val, d };
//             rec(r.right, d + 1);
//         }
//     };

//     rec(root, 0);
//     return ((op[x]?.p !== op[y]?.p) && (op[x]?.d === op[y]?.d))
// };
