function latticePaths(gridSize) {
  // `gridSize` represents the size of the grid, e.g., 4 means a 4x4 grid.
  
  let n = gridSize; // Assign `gridSize` to a variable `n` for clarity.
  let totalNumberOfMoves = 2 * n; // Calculate the total number of moves required (n right + n down).
  
  // Calculate the number of routes using the formula:
  // C(2n, n) = (2n)! / (n! * n!)
  let numberOfRoutes = fact(totalNumberOfMoves) / (fact(n) * fact(n));
  
  return numberOfRoutes; // Return the computed number of lattice paths.
}

// Helper function to calculate the factorial of a number `n`.
function fact(n) {
  if (n === 0) { // Base case: factorial of 0 is 1.
    return 1;
  } else {
    // Recursive case: factorial of `n` is `n * factorial of (n - 1)`.
    return n * fact(n - 1);
  }
}

// Example usage:
// Find the number of lattice paths for a 4x4 grid.
latticePaths(4);
