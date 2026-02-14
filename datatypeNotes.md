# Data types 

 -Number : decimal() , fraction , 0b990
 Sting : 'hello' , "sap'n" , 0/1xcys

 List :  [ 2, [1,'two'], 4.5] , list(range(10))
 You can change, add, or remove elements.
 mainly writes in square bracket 

 Tuple: (1, 'spam',4,'U'),tuple('spam'), namedTuple 
You cannot change the elements of a tuple once it is created.

 Dictionary :d = {"name": "Alice", "age": 25}
 d["age"] = 26          # Change
 d["city"] = "New York" # Add
 del d["name"]          # Remove

 set : takes uniquely s = {1, 2, 3}

 -AdvanceData - Decorators , iterators, generator 


 Note :  for power in python 
       use : double *
        example : 2**4=16

    in python we can easily import Math and Random lib . 

      example : random.choice([1,2,3,4,5,6])
      
      Note : 1. name= "hero"
             len(name)
             output 4
             
             2. name[0]  gives h

             3 . if we assign value 
                  name[0] = A
                  it gives an error Because it is 
                   immutable data 
                  types .
             4. name[-1]  gives o

             5. name[1:3] gives er


      note : in python list is reffered as array .  

# Numbers 

  repr('hello') gives " 'hello' "
  str('hello') gives 'hello'
   print('hello') gives hello

   1==2<3 means 1== 2 and 2<3
   output is false 

   octal 0o20
   Hex 0xFF
   binary 0b1000

   for changing value
   oct(num) hex(num) bin(num)

   random.choice(1,100) is gives random num between 1 to 100
   random.suffle is change the set of array 

   Note : 
        if we 0.1+0.1+0.1-0.1 it not gives 0.0 in python 
        for correct result 

        use from decimal import Decimal 

     decimal('0.1')+decimal('0.1')-decimal('0.2')
     gives __ decimal('0.0')

# Set 
      for intersection &
           union |
          if set - set
          gives set()     
          and this result type is Dict.



# loops 
       1.  basic syntax is 
            for i in range (1,11);

       2. CONTINUE is used for skip the iteration 
          example ;
                 for i in range (1,3)   
                 if i ==2
                 continue:
                 The continue statement is used to skip the 
                   current iteration of the loop and continue 
                    with the next iteration.
                 print(num , 'x' , i , '=' , num*i)            
               then in output num x 2 is skip. 

               break is use for complete stop for loop.
# Functions 
      Basic Syntax 

       def function_name(parameters):
       # code block
         return value

         exmaple :

       1.  Function with Default Parameters
         def power(base, exponent=2):
         return base ** exponent

         print(power(3))      # Uses default exponent
         print(power(3, 3))   # Uses provided exponent
         # Output:
         # 9
         # 27

      2.    greeting problem
          def greet(name = "User")
           return "Hello, " + name + " !"
          print(greet("puneesh"))

      3. lambda function 
        Lambda functions are anonymous functions defined using 
          the lambda keyword.this type of function are also known 
          as no name function .
          basic syntax : 
          lambda arguments: expression
           problem : find cube 
              cube = lambda x:x**3
              print(cube(4))
              output:64
         lambda with map funtion :

          numbers = [1, 2, 3, 4, 5]
     squared_numbers = list(map(lambda x: x ** 2, numbers))
     print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

4. Function with Variable-Length Arguments

           *args is use  
           The *args parameter allows a function to accept any number of positional arguments. Inside the function, args will be a tuple containing all the passed positional arguments.

5.            for taking the input 
     python have built-in function Input() which takes input from user 
     and specification of this function is it store the data in string .

# Scope And Closure 
        
Scope refers to the region of the program where a variable is defined and accessible. Python has several types of scope:

    Local Scope: Variables defined inside a function.
    Enclosing Scope: Variables in the local scope of enclosing functions 
      (i.e., nested functions).
     Global Scope: Variables defined at the top level of a script or
     module.
     Built-in Scope: Special reserved 
      names within Python itself.
 Example :
      
     username = "puneesh" // global 
     def func(): 
        username ="diwakar"//local
        print(username)
     print(username)
     func()   
     OUTPUT:
     puneesh
     diwakar 

# closure
    Closure allows a function to capture and remember the state of its surrounding environment, enabling the function to access those variables even after the outer function has finished execution.     

# Oops    



          basic syntax of Class and Object
            class car:
            def __init__(self, userbrand, usermodel):
            self.brand = userbrand 
            self.model = usermodel


            #how to add functionality 
            def full_name(self):
            return F"{self.brand},{self.model}"

            #inheritence property 

            class petrol(car):
          def __init__(self, brand, model, petorl):
            super().__init__(brand, model)
           self.__petorl = petrol 

           # Encapsulation 

        __ is use for encapsulate 

             
        # static method 

           when we gives the description of class 

          first use @staticmethod 
          def general description() # no self is use 

             return "full description "

          #print method 
          print(car.general description)   

          # note object is not access the static method 
          my_car = car("A","B")   
           print(my_car.brand)
     
          # Base class (Superclass)
class Animal:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age    # Protected attribute

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract 
         method")

    def __str__(self):
        return f"{self._name} is {self._age} years old."

# Derived class (Subclass) - Inheritance
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.__breed = breed  # Private attribute

    # Overriding the make_sound method - Polymorphism
    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self._name} is fetching the ball."

    def __str__(self):
        return super().__str__() + f" It is a {self.__breed}."

# Derived class (Subclass) - Inheritance
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.__color = color  # Private attribute

    # Overriding the make_sound method - Polymorphism
    def make_sound(self):
        return "Meow!"

    def climb(self):
        return f"{self._name} is climbing the tree."

    def __str__(self):
        return super().__str__() + f" It is {self.__color} in color."

# Example of encapsulation - getters and setters
class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.__can_fly = can_fly  # Private attribute

    def make_sound(self):
        return "Tweet!"

    def get_can_fly(self):
        return self.__can_fly

    def set_can_fly(self, can_fly):
        self.__can_fly = can_fly

    def __str__(self):
        return super().__str__() + f" Can it fly? {'Yes' if self.__can_fly else 'No'}."

# Abstraction in action
def animal_sound(animals):
    for animal in animals:
        print(f"{animal} makes a sound: {animal.make_sound()}")

# Creating objects (instances) of the classes
dog = Dog("Buddy", 5, "Golden Retriever")
cat = Cat("Whiskers", 3, "black")
bird = Bird("Tweety", 2, True)

# List of animals
animals = [dog, cat, bird]

# Using the abstraction function to demonstrate polymorphism
animal_sound(animals)

# Demonstrating encapsulation
print(bird)
bird.set_can_fly(False)
print(f"After setting can_fly to False: {bird}")

# Output specific behaviors
print(dog.fetch())
print(cat.climb())


# File System 

    #READ_CSV Function 

     def read_csv(path) :
       result=[]
       #open file 
      with open(path,r)  as f:
      # get a list of lines 
      lines =f.readlines()
      # parse Header 
      headers = parse_header(lines[0])
      # loops over remaning lines 
      for data_lines in lines[1:]:
      # parse Value
      values = parse_values(data_lines)
      #create dict for value and header
      item_dict =create_item_dict(value,header)
      # add dict to result
      result.append(item_dict)
      return result

    # Write file 

       def write_csv(path):
       #open file 
       with open(path,w) as f:
       # return if there is nothing to write 
        if len(item)==0
          return 
        #write header in first line
         headers = list(item[0].keys())  
         f.write(','.join(headers)+'\n')

          # write one item in line 
            for item in items 
            values = []
              for header in headers
              values.append(str(item.get(headers ,"")))
              f.write(',' .join(values)+'\n')


      

 
    
     



