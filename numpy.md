# numpy 
    NumPy is a fundamental library for numerical computing in Python. It provides support for arrays, matrices, and many mathematical functions that operate on these data structures. Here is a detailed overview of numerical computing with NumPy:

# installation
    import numpy as np
    
       1-d array represent as a vector 

      all elements of array of numpy  contains the same data  type .

      # vector multi.
      mport numpy as np

      a = np.array([1, 2, 3])
      b = np.array([4, 5, 6])

      result = np.dot(a, b)
      print(result)  # Output: 32      


# data types of numpy 
     
     NumPy supports a wide range of data types, which are essential for 
       numerical computations. These data types are defined in a 
        platform-independent way, providing consistency across different 
         systems.

    1. integer (int8 , int64)     
    2. float(flaot 16 , float)

    note :
      
   Integer Types: The array a is created with 8-bit signed integers.

   Floating-Point Types: The array b is created with 32-bit single- 
     precision floating-point numbers.

   Complex Types: The array c is created with 64-bit complex numbers.


# csv file data reading with numpy 
 
    To read CSV file data using NumPy, you can use the numpy.genfromtxt 
    function, which is designed to handle CSV (and other text) files. 
     This function provides flexibility in handling different data types 
      and missing values.

    1. import urllib.request
    2. urllib.request.urlretrive(link)  
    3. file_data  = np.genfromtxt('file.txt' , delimiter=',' 
      skip_header=1)

      delimiter is the operator which seprate the data .

    # np.concatante function is used for add a new column in the given 
      matrix .


      #np.savetxt

          np.savetxt is a function in NumPy used to save an array to a 
          text file. This function provides a simple way to export data 
           from a NumPy array into a format that can be easily read and 
            shared.

          np.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', 
            header='', footer='', comments='# ', encoding=None)
            X: The array to be saved.

 # Broadcasting in numpy 
          Broadcasting is a powerful feature in NumPy that allows arithmetic operations to be performed on arrays of different shapes. When the shapes of two arrays are different, NumPy tries to "broadcast" the smaller array across the larger array so that the operation can be performed.

          import numpy as np

arr1 = np.array([[1], [2], [3]])  # Shape (3, 1)
arr2 = np.array([4, 5, 6])        # Shape (3,)

result = arr1 + arr2
print(result)
# Output:
# [[5 6 7]
#  [6 7 8]
#  [7 8 9]]

Rules for Broadcasting:

Trailing Dimensions: Compare the shapes of the arrays from right to left. Two dimensions are compatible when they are equal or one of them is 1.


Padding with Ones: If the arrays have different numbers of dimensions, the smaller array is padded with ones on the left side until both arrays have the same number of dimensions.


# note :
       in numpy comparision operator is gives the boolean array 


# Array slicing and indexing :

    1. 1-D array is simply arr[0]
    2. 2-D array is 
        arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print(arr2d[0, 0])  # Output: 1 (element at row 0, column 0)
         print(arr2d[1, 2])  # Output: 6 (element at row 1, column 2)


    3. 3-D array is -

        arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        print(arr3d[0, 1, 1])  # Output: 4 (depth 0, row 1, column 1)   




# for creating different type of array use numpy  function :

    1. numpy.zeros(3,2) make zero matrix 
    2. numpy.ones makes all one matrix 
    3.np.random.randn(2,3) generate random matrix
    4. np.full([2,3],num) its makes same no. matrix. 
    5.np.arange(5,15,3) its makes start end and step matrix.



