/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const new_arr = [];

    for (let i = 0; i < arr.length; i += size) {
        new_arr.push(arr.slice(i, i+ size));
    }

    return new_arr;
};
