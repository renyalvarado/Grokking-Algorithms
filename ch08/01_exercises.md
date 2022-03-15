# Exercises

1. You work for a furniture company, and you have to ship furniture
all over the country. You need to pack your truck with boxes. All
the boxes are of different sizes, and you’re trying to maximize the
space you use in each truck. How would you pick boxes to maximize
space? Come up with a greedy strategy. Will that give you the
optimal solution?

    It would be to put the biggest boxes first. I won't be the optimal
    solution.


2. You’re going to Europe, and you have seven days to see everything
you can. You assign a point value to each item (how much you want
to see it) and estimate how long it takes. How can you maximize the
point total (seeing all the things you really want to see) during your
stay? Come up with a greedy strategy. Will that give you the optimal
solution?

    It would be to go first to the city with most important things to do.
    It wouldn't be the optimal solution.


For each of these algorithms, say whether it’s a greedy algorithm or not.

3. Quicksort

    No greedy.    


4. Breadth-first search

    Greedy


5. Dijkstra’s algorithm

    Greedy


6. A postman needs to deliver to 20 homes. He needs to find the
shortest route that goes to all 20 homes. Is this an NP-complete
problem?

    Yes, it is like the travelling salesman problem. 


7. Finding the largest clique in a set of people (a clique is a set of people
who all know each other). Is this an NP-complete problem?

    Yes. It looks like a factorial growth problem, because every time we add some to
    a clique candidate we have to verify that the new person knows the rest of the people.


9. You’re making a map of the USA, and you need to color adjacent
states with different colors. You have to find the minimum number
of colors you need so that no two adjacent states are the same color.
Is this an NP-complete problem?

    Yes.
