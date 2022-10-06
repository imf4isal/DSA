// variant one

const nextGreater = ar => {
  let n = ar.length;
  let stack = [];
  let nge = new Array(n);
  let arr = ar.concat(ar);
  for (i = n * 2 - 1; i >= 0; i--) {
    while (stack.length && stack[stack.length - 1] <= arr[i]) {
      stack.pop();
    }

    if (!stack.length) {
      stack.push(arr[i]);
      nge[i % n] = -1;
    } else {
      nge[i % n] = stack[stack.length - 1];
      stack.push(arr[i]);
    }
  }

  console.log(nge);
};

const nums = [5, 7, 1];

nextGreater(nums);

// const nextGreater = arr => {
//   let stack = [];
//   let nge = new Array(arr.length);

//   for (i = arr.length - 1; i >= 0; i--) {
//     while (stack.length && stack[stack.length - 1] <= arr[i]) {
//       stack.pop();
//     }

//     if (!stack.length) {
//       stack.push(arr[i]);
//       nge[i] = -1;
//     } else {
//       nge[i] = stack[stack.length - 1];
//       stack.push(arr[i]);
//     }
//   }

//   console.log(nge);
// };
