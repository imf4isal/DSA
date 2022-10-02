// implementing a linked list
class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const a = new Node("A");
const b = new Node("B");
const c = new Node("C");
const d = new Node("D");

a.next = b;
b.next = c;
c.next = d;

/////////////////////////////
//problem: add all nodes from an linked list into an arary, and return that array.
//////////////////////////////

// using iterator

const linkedListtoArray = head => {
  let current = head;
  resArr = [];
  while (current !== null) {
    resArr.push(current.val);
    current = current.next;
  }
  return resArr;
};

console.log(linkedListtoArray(a));

//using recursion
const linkedListtoArrayRecur1 = (head, arr) => {
  if (head === null) return arr;
  arr.push(head.val);
  return linkedListtoArrayRecur1(head.next, arr);
};

console.log(linkedListtoArrayRecur1(a, []), 1);

const linkedListtoArrayRecur2 = head => {
  let values = [];

  fillup(head, values);

  return values;
};

const fillup = (head, values) => {
  if (head === null) return;
  values.push(head.val);
  fillup(head.next, values);
};

console.log(linkedListtoArrayRecur2(a), 2);
