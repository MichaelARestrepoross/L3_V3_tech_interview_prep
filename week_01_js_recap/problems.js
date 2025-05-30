// Reverse a string
function reverseString(str) {
  return str.split('').reverse().join('');
}
  
// Find max in array
function findMax(arr) {
  if (arr.length === 0) return undefined;
  return Math.max(...arr);
}

// Check if palindrome
function isPalindrome(word) {
  return word === word.split('').reverse().join('');
}

module.exports = { reverseString, findMax, isPalindrome };