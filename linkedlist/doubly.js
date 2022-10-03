// node of a doubly linked list

class Node {
  constructor(data) {
    this.data = data;
    this.prev = null;
    this.next = null;
  }
}

class DLL {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(data) {
    const node = new Node(data);
    if (!this.head) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      node.prev = this.tail;
      this.tail = node;
    }
    this.length++;
    return this; // return the whole list.
  }

  //removing last node
  pop() {
    if (this.length === 0) return; // return false;
    const popped = this.tail;
    const newTail = popped.prev;

    if (newTail) {
      newTail.next = null;
      this.prev = null;
    }
    this.tail = newTail; // assigning new Tail, it can be null.
    this.length--;

    return popped;
  }

  //removing first node
  shift() {
    if (!this.head) return; //return false;
    const shiftedNode = this.head;

    const newHead = this.head.next;

    if (newHead) {
      shiftedNode.next = null;
      newHead.prev = null;
    } else {
      this.tail = null;
    }
    this.head = newHead;
    this.length--;
    return shiftedNode;
  }

  //insert Node at first
  unshift(data) {
    const node = new Node(data);
    if (!this.head) {
      this.head = node;
      this.tail = node;
    }

    node.next = this.head;
    this.head.prev = node;
    this.head = node;

    this.length++;
    return this; // returning full list
  }

  //get node of particular index
  getAt(index) {
    if (index >= this.length || index < 0) return -1;

    let countIdx = 0;
    let currentNode = this.head;

    while (countIdx !== index) {
      currentNode = currentNode.next;
      countIdx++;
    }
    return currentNode;
  }

  //inserting node at particular index
  insertAt(data, index) {
    if (index > this.length) return false;

    if (index === 0) {
      this.unshift(data);
    } else if (index === this.length) {
      this.push(data);
    } else {
      const newNode = new Node(data);
      const prevNode = this.getAt(index - 1);
      const nextNode = prev.next;

      prevNode.next = newNode;
      newNode.prev = prevNode;

      newNode.next = nextNode;
      nextNode.pev = newNode;
      this.length++;
    }
    //we are increasing length inside else block instead of here, because unshift and push themselves increase the length
  }

  // deleting node from particular index;
  deleteAt(index) {
    let deletedNode;
    if (index > this.length) {
      return false;
    } else if (index === 0) {
      deletedNode = this.shift();
    } else if (index === this.length - 1) {
      deletedNode = this.pop();
    } else {
      deletedNode = this.getAt(index);
      const prevNode = deletedNode.prev;
      const nextNode = deletedNode.next;
      deletedNode.prev = null;
      deletedNode.next = null;
      prevNode.next = nextNode;
      nextNode.prev = prevNode;
      this.length--;
    }
    return deletedNode;
  }

  // set new value of a particular index's node

  setValue(data, index) {
    const node = this.getAt(index);
    if (node) {
      node.data = data;
      return node;
    }
    return null;
  }
}
