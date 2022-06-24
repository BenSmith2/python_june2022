/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/

const strA1 = "ABCD";
const strB1 = "CDAB";
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated
const expected1 = true;

const strA2 = "ABCD";
const strB2 = "CDBA";
// Explanation: all same letters in 2nd string, but out of order
const expected2 = false;

const strA3 = "ABCD";
const strB3 = "BCDAB";
// Explanation: same letters in correct order but there is an extra letter.
const expected3 = false;

/**
 * Determines whether the second string is a rotated version of the first.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether the second string is a rotated version of the 1st.
 */
function isRotation(s1, s2) {
    if (s1.length!= s2.length){
        return false
    }
    for (var i = 0; s2.length>i; i++){
        s1 = s1.slice(s1.length-1)+s1.slice(0, s1.length-1)
        console.log(s1) 
    }
    

}

function isRotation(s1, s2) { 
    if (s1.length == s2.length){ 
        for (var i = 0; s2.length>i; i++){ 
            s1 = s1.slice(s1.length-1)+s1.slice(0, s1.length-1) 
            console.log('Rotate', s1) if (s1 === s2){ 
                return true 
            } 
        } 
    } 
    else{ return false } 
}

console.log(isRotation(strA1,strB1)) //should be true
console.log(isRotation(strA2,strB2)) //should be false
console.log(isRotation(strA3,strB3)) //should be false