function longestCollatzSequence(limit) {
  // Initialize variables
  let i = 1;                  // Start from 1
  let count = 0;              // To track the maximum length of the Collatz sequence found so far
  let startingNumber = 1;     // To store the number that produces the longest sequence

  // Loop through all numbers less than the given limit
  while (i < limit) {
    // Calculate the number of terms in the Collatz sequence for the current number
    let number = numberOfTerms(i);

    // Update the max count and starting number if the current sequence is longer
    if (count < number) {
      count = number;         // Update the maximum sequence length
      startingNumber = i;     // Update the starting number with the longest sequence
    }

    // Move to the next number
    i++;
  }

  // Return the starting number that produces the longest Collatz sequence
  return startingNumber;
}

// Helper function to calculate the number of terms in the Collatz sequence for a given number
function numberOfTerms(i) {
  let count = 1;              // Initialize count, starting with the input number itself

  // Keep generating the next number in the sequence until reaching 1
  while (i != 1) {
    if (i % 2 == 0) {
      // If the number is even, divide it by 2
      i = i / 2;
    } else {
      // If the number is odd, multiply by 3 and add 1
      i = 3 * i + 1;
    }
    count++;                  // Increment the count for each step
  }

  // Return the total number of terms in the sequence
  return count;
}

// Example usage
longestCollatzSequence(14);
