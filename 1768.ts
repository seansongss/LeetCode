function mergeAlternately(word1: string, word2: string): string {
    let result: string = "";
    let word1_len: number = word1.length;
    let word2_len: number = word2.length;
    let max: number = Math.max(word1_len, word2_len)
    for (let i: number = 0; i < max; i++) {
        if (i < word1_len) {
            result = result.concat("", word1[i])
        }
        if (i < word2_len) {
            result = result.concat("", word2[i])
        }
    }
    return result
};

console.log(mergeAlternately("abc", "pqr")) // "apbqcr"
console.log(mergeAlternately("ab", "pqrs")) // "apbqrs"
console.log(mergeAlternately("abcd", "pq")) // "apbqcd"