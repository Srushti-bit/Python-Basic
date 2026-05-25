''''
Hashing: is a technique to convert data into a fixed size value called a hash value or hash code
--------
this hash code help us to store and search data very fast

this of hashing as: 
  "Converting a big peice of information into a small actions."

------------------------------------------------------------------------------------------------
  ques 1) Why hashing is needed?

  ans: imagine you have :
  10 students - easy to search
  10 lakh students - searching becomes slow

  without hashing :
  searching may take lot of time

  with hashing:
  data can be found almost instantly.


  ques 2) problems solved by hashing ?

  before hashing, searching required:
   linear search - O(n)
   binary search - O(log n)

   hashing provides:
   avg O(1) lookup time

   that means:
      constant 


      ques 3) Time complexity
       operations without hashing  hashing
      search -        O(n)         O(1)
      insert -        O(n)         O(1)
      delete -        O(n)         O(1)

      ques4) Applications:

       Google search    -  fast indexing
       python dictionary - key value storage
       database indexing - fast queries
       password storage  - security
       ATM system     - card verification
       cachiing  - fast access
       blockchain - data integrity
       compiler  - symbol tables

       ques 5) what is hash function?

       a hash function converts:
       input -> fixed index

       example:
       hash("apple")

       might produce"
       2354789

       ques 6) simpple hash fucntion example:
        
       suppose table size = 10
       formula:
       index = key %10

       example:
       25 % 10 = 5

       so 25 stored at index 5

       * DRY RUN PROCESS:

       key % 10

       key     calculation     index
       15           15%10        5
       25           25%10        5
       35           35%10        5

       problem?

       all map to same index 
       this is called collision

       ques7)  properties of good hashing ?

         1) uniform distribution
         2) deterministic
         3) fast computation

         ques 8)  hash string --"CAT"

          ans:

                ASCII values:
                C  = 67
                A  = 65
                T  = 84
                
                sum:  67 + 65 + 84 = 216

                  216 % 10 = 6

                  CAT will be stored at index 6

        ques 9) why O(1)?
        ans: hash fucntion directly gives location


       ques 10) why is dictionary lookup fast ?

        ques 11)  why list cannot be dictionary keys?
        ans : because it is mutable

        ques 12)  why tuple cannot be dictionary keys?

        ques 13)  why collision happens ?
          ans:  because :
               infinite inputs
               limited table size

        ques 14) real life analogy of collision?

''' 


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key%self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        print(self.table)        
    