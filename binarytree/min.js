class Node {
  constructor(value) {
    this.val = value;
    this.left = null;
    this.right = null;
  }
}

const treemin = root => {
  if (root === null) return Infinity;
  const left = treemin(root.left);
  const right = treemin(root.right);
  return Math.min(root.val, left, right);
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

console.log(treemin(a));
