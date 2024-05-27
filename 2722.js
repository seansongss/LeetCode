/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    // for (let i of arr2) {
    //     const tmp_idx = arr1.findIndex(item => item.id === i.id);
    //     if (tmp_idx > -1) {
    //         const new_obj = Object.assign(arr1[tmp_idx], i);
    //         arr1.splice(tmp_idx, 1, new_obj);
    //     } else {
    //         arr1.push(i);
    //     }
    // }
    // arr1.sort((a, b) => a.id - b.id);
    // return arr1;
    all_obj = arr1.concat(arr2);
    new_arr = {};
    for (let obj of all_obj) {
        if (!new_arr[obj.id]) {
            new_arr[obj.id] = obj;
            continue;
        }

        new_arr[obj.id] = {...new_arr[obj.id], ...obj};
    }

    return Object.values(new_arr);
};