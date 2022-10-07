class Node {
  constructor(value) {
    this.val = value;
    this.left = null;
    this.right = null;
  }
}

// const treemax = root => {
//   if (root === null) return 0;
//   const left = treemax(root.left);
//   const right = treemax(root.right);
//   const m = left > right ? left : right;

//   return root.val + m;
// };

const treemax = root => {
  if (root === null) return -Infinity;
  if (!root.left && !root.right) return root.val;
  return root.val + Math.max(treemax(root.left), treemax(root.right));
};

const a = new Node(3);
const b = new Node(11);
const c = new Node(4);
const d = new Node(4);
const e = new Node(2);
const f = new Node(1);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

console.log(treemax(a));
