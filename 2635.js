/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const returnedArr = [];
    for (let i = 0; i < arr.length; i++) {
        returnedArr[i] = fn(arr[i], i);
    }
    return returnedArr;
};
