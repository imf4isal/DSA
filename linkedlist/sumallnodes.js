// implementing a linked list
class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const a = new Node(4);
const b = new Node(3);
const c = new Node(5);
const d = new Node(8);

a.next = b;
b.next = c;
c.next = d;

/////////////////////////////
//problem: return the sum of all nodes.
//////////////////////////////

// using iterator

const sumNodes = head => {
  let sum = 0;
  let current = head;

  while (current !== null) {
    sum += current.val;
    current = current.next;
  }
  return sum;
};
console.log(sumNodes(a));

// using recursion

const sumNodesRecur = head => {
  if (head === null) return 0;
  return head.val + sumNodesRecur(head.next);
};

console.log(sumNodesRecur(a));
