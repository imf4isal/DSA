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
