function powerDigitSum(exponent) {
  // Calculate 2 raised to the power of the exponent using Math.pow
  // Cast the result to BigInt to handle large numbers
  let powerNumber = BigInt(Math.pow(2, exponent));

  // Convert the resulting BigInt to a string to process its digits
  let stringPowerNumber = powerNumber.toString();

  // Split the string into individual characters (digits),
  // then use reduce to compute the sum of the digits
  let sumOfDigits = stringPowerNumber
    .split('') // Convert the string to an array of characters (digits)
    .reduce(
      (total, elem) => total + Number.parseInt(elem), // Convert each digit to a number and add to the total
      0 // Initialize the sum at 0
    );

  // Return the calculated sum of the digits
  return sumOfDigits;
}

// Example usage: Calculate the sum of the digits of 2^15
powerDigitSum(15);
