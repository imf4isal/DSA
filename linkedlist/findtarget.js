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
//problem: return True if target element has been found, otherwise return false
//////////////////////////////

//using iterator

const findTarget = (head, target) => {
  let current = head;
  while (current !== null) {
    if (current.val === target) return true;
    current = current.next;
  }
  return false;
};

console.log(findTarget(a, 11));

// using recursion

const findTargetRecur = (head, target) => {
  if (head === null) return false;
  if (head.val === target) return true;
  return findTargetRecur(head.next, target);
};

console.log(findTargetRecur(a, 11), "recursion");
