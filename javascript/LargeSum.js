function largeSum(arr) {
  // Step 1: Concatenate all 50-digit numbers in the array into one long string.
  // This makes it easier to process all numbers as a single continuous sequence.
  let str = arr.join(''); 

  // Step 2: Initialize a variable to store the cumulative sum of the numbers.
  // We will add partial values extracted from the string in the loop below.
  let sum = 0;

  // Step 3: Process the string while it contains digits.
  while (str !== "") {
    // Step 3.1: Take the first 12 digits of the string.
    // We only need the most significant digits because:
    // - Adding smaller digits won’t affect the leading 10 digits of the result.
    // - Using fewer digits reduces computational complexity.
    sum += Number.parseInt(str.slice(0, 12)); 
    
    // Step 3.2: Remove the first 50 characters from the string.
    // Each number in the original array is exactly 50 digits long.
    str = str.slice(50); 

  }

  // Step 4: After summing up all the numbers, we convert the total sum to a string.
  // Extract the first 10 characters (the most significant digits).
  // Convert those 10 characters back to an integer.
  return Number.parseInt(sum.toString().slice(0, 10));
}

// Only change code above this line

const testNums = [
  '37107287533902102798797998220837590246510135740250',
  '46376937677490009712648124896970078050417018260538'
];

largeSum(testNums);