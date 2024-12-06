function divisibleTriangleNumber(n) {
  // Start with the first triangular number, which is 1
  let nbre = 1;
  
  // Start with the first natural number
  let i = 1;

  // Continue finding the next triangular number until it has more than `n` divisors
  while (sumOfDivisors(nbre) < n) {
    i++; // Increment to the next natural number
    nbre += i; // Add it to the current triangular number to get the next one
  }

  // Return the first triangular number with at least `n` divisors
  return nbre;
}

// Function to count the number of proper divisors of a number (excluding the number itself)
function sumOfDivisors(nbre) {
  let sum = 0; // Initialize the sum of divisors

  // Loop through potential divisors from 1 to the square root of `nbre`
  for (let i = 1; i <= Math.sqrt(nbre); i++) {
    if (nbre % i === 0) { // Check if `i` is a divisor
      if (i !== nbre) sum += 1; // Count `i` if it's not the number itself

      // Calculate the complementary divisor
      let complement  = nbre / i;

      // Add the complementary divisor if it's not the same as `i` or `nbre`
      if (complement  !== i && complement  !== nbre) {
        sum += 1;
      }
    }
  }

  // Return the total count of divisors (excluding `nbre` itself)
  return sum;
}

// Test the function to find the first triangular number with at least 500 divisors
divisibleTriangleNumber(500);
