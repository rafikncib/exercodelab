function largestGridProduct(arr) {
  // Initialize the greatest product to -1 (assuming all values in the grid are non-negative).

  let prod = -1;

  // The grid is square, so rows and columns have the same length.
  // Use a single variable to represent the grid's size.

  let len =  arr.length;

  // Iterate through every cell in the grid.
  for(let i=0;i<len;i++){
    for(let j=0;j<len;j++){
            // Check horizontally (to the right) if there are enough cells.

      if(j+3<len){
        if(prod < arr[i][j]*arr[i][j+1]*arr[i][j+2]*arr[i][j+3]){
          // Update the greatest product.
          prod = arr[i][j]*arr[i][j+1]*arr[i][j+2]*arr[i][j+3];
          
        }
      }
      // Check vertically (downwards) if there are enough cells.

      if(i+3<len){
        if(prod < arr[i][j]*arr[i+1][j]*arr[i+2][j]*arr[i+3][j]){
          // Update the greatest product.
          prod = arr[i][j]*arr[i+1][j]*arr[i+2][j]*arr[i+3][j];
          
        }
      }
      // Check diagonally down-right if there are enough cells.

      if(i+3<len && j+3<len){
        if(prod < arr[i][j]*arr[i+1][j+1]*arr[i+2][j+2]*arr[i+3][j+3]){
          // Update the greatest product.
          prod = arr[i][j]*arr[i+1][j+1]*arr[i+2][j+2]*arr[i+3][j+3];
     
        }
      }
      // Check diagonally up-right if there are enough cells.

     if(i+3<len && j-3>=0){
        if(prod < arr[i][j]*arr[i+1][j-1]*arr[i+2][j-2]*arr[i+3][j-3]){
          // Update the greatest product.
          prod = arr[i][j]*arr[i+1][j-1]*arr[i+2][j-2]*arr[i+3][j-3];

        }
      }
      
    
    }
  }

    // Return the greatest product found in the grid.

  return prod;
}
