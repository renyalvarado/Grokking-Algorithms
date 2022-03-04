# Exercises

1. Write out the code for the earlier sum function.

   [custom_sum.py](custom_sum.py)


2. Write a recursive function to count the number of items in a list.

   [custom_count.py](custom_count.py)


3. Find the maximum number in a list.

   [custom_max.py](custom_max.py)


4. Remember binary search from chapter 1? It’s a divide-and-conquer algorithm, too. Can you come up with the base case
   and recursive case for binary search?
   
   Yes, because it divides the problem into a similar one but with half the elements.

   [recursive_binary_search.py](recursive_binary_search.py)

How long would each of these operations take in Big O notation?
5. Printing the value of each element in an array.

    O(log n)


6. Doubling the value of each element in an array.

    O(n)


7. Doubling the value of just the first element in an array.

    O(1)


8. Creating a multiplication table with all the elements in the array. So
if your array is [2, 3, 7, 8, 10], you first multiply every element by 2,
then multiply every element by 3, then by 7, and so on.

    O(n^2)
