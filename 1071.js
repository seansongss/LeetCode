function gcdOfStrings(str1, str2) {
    if (str1 + str2 !== str2 + str1) {
        return "";
    }
    var gcd = function (a, b) {
        return b === 0 ? a : gcd(b, a % b);
    };
    return str1.substring(0, gcd(str1.length, str2.length));
}
;
// str1 = "ABCABC", str2 = "ABC"
// "ABC"
console.log(gcdOfStrings("ABCABC", "ABC"));
