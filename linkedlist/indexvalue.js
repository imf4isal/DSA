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
//problem: return the give index node value of a linkedlist
//////////////////////////////

const indexValue = (head, ind) => {
  let count = 0;
  let current = head;
  while (current !== null) {
    if (count === ind) return current.val;
    current = current.next;
    count++;
  }
  return null;
};

console.log(indexValue(a, 8));

const indexValueRecur = (head, ind) => {
  if (head === null) return null;
  if (ind === 0) return head.val;
  return indexValueRecur(head.next, ind - 1);
};

console.log(indexValueRecur(a, 2));
