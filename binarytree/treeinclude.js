class Node {
  constructor(value) {
    this.val = value;
    this.left = null;
    this.right = null;
  }
}

const treeinclude = (root, target) => {
  if (root === null) return false;
  if (root.val === target) return true;
  return treeinclude(root.left, target) || treeinclude(root.right, target);

  // bread first
  // if (!root) return [];
  // const queue = [root];
  // while (queue.length > 0) {
  //   const current = queue.shift();

  //   if (current.val === target) {
  //     return true;
  //   }

  //   if (current.left) queue.push(current.left);
  //   if (current.right) queue.push(current.right);
  // }

  // return false;
};

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

console.log(treeinclude(a, "f"));
console.log(treeinclude(a, "a"));
console.log(treeinclude(a, "e"));
console.log(treeinclude(a, "g"));
