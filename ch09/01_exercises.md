# Exercises

1. Suppose you can steal another item: an MP3 player. It weighs 1 lb
and is worth $1,000. Should you steal it?

|            | 1                  | 2                            | 3                                   | 4                                   |
|------------|--------------------|------------------------------|-------------------------------------|-------------------------------------|
| guitar (0) | (1500, ['guitar']) | (1500, ['guitar'])           | (1500, ['guitar'])                  | (1500, ['guitar'])                  |
| stereo (1) | (1500, ['guitar']) | (1500, ['guitar'])           | (1500, ['guitar'])                  | (3000, ['stereo'])                  |
| laptop (2) | (1500, ['guitar']) | (1500, ['guitar'])           | (2000, ['laptop'])                  | (3500, ['guitar', 'laptop'])        |
| iphone (3) | (2000, ['iphone']) | (3500, ['guitar', 'iphone']) | (3500, ['guitar', 'iphone'])        | (4000, ['laptop', 'iphone'])        |
| mp3 (4)    | (2000, ['iphone']) | (3500, ['guitar', 'iphone']) | (4500, ['guitar', 'iphone', 'mp3']) | (4500, ['guitar', 'iphone', 'mp3']) |


Yes. You should steal a guitar, an iPhone and a MP3 player ($4500)


2. Suppose you’re going camping. You have a knapsack that holds
6 lb, and you can take the following items. They each have a value,
and the higher the value, the more important the item is:

* Water, 3 lb, 10
* Book, 1 lb, 3
* Food, 2 lb, 9
* Jacket, 2 lb, 5
* Camera, 1 lb, 6

What’s the optimal set of items to take on your camping trip?

|            | 1               | 2             | 3                        | 4                                | 5                                  | 6                                 |
|------------|-----------------|---------------|--------------------------|----------------------------------|------------------------------------|-----------------------------------|
| water (0)  | (0, [])         | (0, [])       | (10, ['water'])          | (10, ['water'])                  | (10, ['water'])                    | (10, ['water'])                   |
| book (1)   | (3, ['book'])   | (3, ['book']) | (10, ['water'])          | (13, ['water', 'book'])          | (13, ['water', 'book'])            | (13, ['water', 'book'])           |
| food (2)   | (3, ['book'])   | (9, ['food']) | (12, ['book', 'food'])   | (13, ['water', 'book'])          | (19, ['water', 'food'])            | (22, ['water', 'book', 'food'])   |
| jacket (3) | (3, ['book'])   | (9, ['food']) | (12, ['book', 'food'])   | (14, ['food', 'jacket'])         | (19, ['water', 'food'])            | (22, ['water', 'book', 'food'])   |
| camera (4) | (6, ['camera']) | (9, ['food']) | (15, ['food', 'camera']) | (18, ['book', 'food', 'camera']) | (20, ['food', 'jacket', 'camera']) | (25, ['water', 'food', 'camera']) |

Yes. You should put water, food and camera ($4500)


3. Draw and fill in the grid to calculate the longest common
substring between blue and clues.

|     | C   | L   | U   | E   | S   |
|-----|-----|-----|-----|-----|-----|
| B   | 0   | 0   | 0   | 0   | 0   |
| L   | 0   | 1   | 0   | 0   | 0   |
| U   | 0   | 0   | 2   | 0   | 0   |
| E   | 0   | 0   | 0   | 3   | 0   |

