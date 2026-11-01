#Project Euler - Longest Collatz Sequence

We use a while loop to check all the values from 999999 till 1 .
In the while loop we have defined a varaible called count which keeps track of the no. of terms , since it is initialized to 1.
Then using a while loop , the  Operations as given in Collatz sequence are done till i reaches 1 .
Whenever any change happens to i , the count goes up by 1 which keeps track of all the terms.
Then after the loops of the operations , the value of i is restored and stored if the respective i value has the max count.
