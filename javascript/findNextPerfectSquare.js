function findNextSquare(sq) {
  // Return the next square if sq is a perfect square, -1 otherwise
  sqNumber= Math.sqrt(sq);
  return Number.isInteger(sqNumber) ?Math.pow(sqNumber+1,2):-1;
}