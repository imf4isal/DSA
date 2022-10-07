class Node {
  constructor(value) {
    this.val = value;
    this.left = null;
    this.right = null;
  }
}

const depthFirstValues = root => {
  const result = [];
  const stack = [root];

  while (stack.length > 0) {
    const current = stack.pop();
    result.push(current.val);

    // left to right
    if (current.right) stack.push(current.right);
    if (current.left) stack.push(current.left);

    // right to left
    if (current.left) stack.push(current.left);
    if (current.right) stack.push(current.right);
  }

  return result;
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

console.log(depthFirstValues(a));
