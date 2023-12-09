/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    search_index(nums, target, Math.floor(nums.length/2), Math.floor(nums.length/2))
};

function search_index(nums, target, index, zero) {
    if(zero==0){
        return index;
    }
    if(target==nums[index]){
        return index;
    }
    if(target < nums[index]){
        search_index(nums, target, Math.floor(index/2), Math.floor(zero/2));
    } else {
        search_index(nums, target, Math.floor((index+nums.length)/2), Math.floor(zero/2));
    }
};

var nums = [1,2, 3,5];
index = search_index(nums, 5, 2, 1);
console.log(index);