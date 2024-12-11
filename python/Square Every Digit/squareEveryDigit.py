def square_digits(num):
    # Your code here
    square = ""
    for x in str(num):
        square+=str(int(x)**2)
    
    return int(square)