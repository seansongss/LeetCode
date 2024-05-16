function mergeAlternately(word1, word2) {
    var result = "";
    var word1_len = word1.length;
    var word2_len = word2.length;
    var max = Math.max(word1_len, word2_len);
    for (var i = 0; i < max; i++) {
        if (i < word1_len) {
            result = result.concat("", word1[i]);
        }
        if (i < word2_len) {
            result = result.concat("", word2[i]);
        }
    }
    return result;
}
;
console.log(mergeAlternately("abc", "pqr")); // "apbqcr"
console.log(mergeAlternately("ab", "pqrs")); // "apbqrs"
console.log(mergeAlternately("abcd", "pq")); // "apbqcd"
