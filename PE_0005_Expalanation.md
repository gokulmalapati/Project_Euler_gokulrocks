Project Euler - Smallest Multiple

For this question , they have told us that 2520 is the least positive integer that is evenly divisible by all integers in [1,10] .
The question asked to find the smallest +ve Int which is divisible by all int in [1,20].
For that we find all the prime numbers in [1,20]
Then we increase their powers to the max value of them below 20 and multiple all of these .
The reason why we did that is to ensure all of the other larger composites like 16 and 18 and others can evenly divide the integer.
And when we do that , we get 232792560.
