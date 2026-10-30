#Project Euler - Largest Product in the Grid

First we store the 20*20 matrix as a text so that we could call it with a single parameter instead of 2.
Then we define a max_p( and initialize it to 1) to store the max product till that operation.
Then we find of the product in rows using a double while loop in which we update i+=1 in the inner loop for all elements in the same row and j+=20 in the outer while loop to update the row.
We use a While loop and the fact that the elements in the same column will have a constant index difference of 20.
Then we use a while loop for Right Diagonal elements since they all have a constant index difference of 21.
But in the Right diagonal elements , the first three rows(0,1,2) cannot have it since we anchor our right diagonal at the bottom  so we remove them
We also use a while loop for left diagonal elements since they have a constant index difference of 19.
But for similar reason as mentioned above , we remove the 19,18,17 rows from it.
