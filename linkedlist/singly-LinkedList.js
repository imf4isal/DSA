// constructor for creating a single node
class ListNode {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}

class LinkedList {
  constructor(head = null) {
    this.head = head;
  }

  length() {
    let count = 0;
    let current = this.head;

    while (current) {
      count++;
      current = current.next;
    }
    return count;
  }

  clear() {
    this.head = null;
  }

  lastNode() {
    let lastNode = this.head;

    if (lastNode) {
      while (lastNode.next) {
        lastNode = lastNode.next;
      }
    }
    return lastNode;
  }

  firstNode() {
    return this.head;
  }

  insertAtFirst(data) {
    let newNode = new ListNode(data);
    newNode.next = this.head;
    this.head = newNode;
    return this.head;
  }

  insertAtLast(data) {
    let newNode = new ListNode(data);

    if (!this.head) {
      this.head = newNode;
      return this.head;
    }

    let tail = this.head;
    while (tail.next) {
      tail = tail.next;
    }

    tail.next = newNode;
    return this.head;
  }

  getAt(index) {
    let count = 0;

    let node = this.head;

    while (node) {
      if (count === index) {
        return node;
      }
      count++;
      node = node.next;
    }
    return null;
  }

  insertAt(data, index) {
    let newNode = new ListNode(data);

    if (!this.head) {
      this.head == newNode;
      return this.head;
    }

    if (index === 0) {
      newNode.next = this.head;
      this.head = newNode;
      return this.head;
    }

    let previous = this.getAt(index - 1);

    newNode.next = previous.next;
    previous.next = newNode;

    return this.head;
  }

  deleteFirst() {
    if (!this.head) {
      return;
    }

    this.head = this.head.next;
    return this.head;
  }

  deleteLast() {
    if (!this.head) {
      return;
    }

    if (!this.head.next) {
      this.head = null;
      return;
    }

    prev = this.head;
    tail = this.head.next;

    while (tail.next !== null) {
      prev = tail;
      tail = tail.next;
    }

    prev.next = null;
    return this.head;
  }

  deleteAt(index) {
    if (!this.head) {
      return;
    }

    if (index === 0) {
      this.head = this.head.next;
      return;
    }
    const previous = this.getAt(index - 1);

    if (!previous || !previous.next) {
      return;
    }

    previous.next = previous.next.next;
    return this.head;
  }

  indexOf(data) {
    let ind = -1;
    let node = this.head;
    while (node) {
      ++ind;
      if (node.data === data) return ind;

      node = node.next;
    }
    return -1;
  }

  reverse() {
    let prevNode = null;
    let currentNode = this.head;
    if (currentNode === null) return;

    let nextNode;
    while (currentNode) {
      nextNode = currentNode.next;

      currentNode.next = prevNode;
      prevNode = currentNode;

      currentNode = nextNode;
    }
    this.head = prevNode;
  }

  isEmpty() {
    return this.head == null;
  }

  printList() {
    let node = this.head;
    process.stdout.write("Head ->");
    while (node) {
      process.stdout.write(node.data + " -> ");
      node = node.next;
    }
    console.log("Null");
  }
}

// let node1 = new ListNode(5); // creating only a node
// let node2 = new ListNode(7);

// node1.next = node2; // creating chain between nodes..

// let list = new LinkedList(node1); // creating a linked list.

// let list2 = new LinkedList(); //head set to null if we don't pass argument.
// list2.head = node1; //we can set head of a linked list later.

// console.log(list.lastNode().data);
