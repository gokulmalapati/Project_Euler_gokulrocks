#Project Euler - Largest Product in a Series

First we assign the 1000 digit number to a variable in this case x .
we then use a while loop in which we use the moduli operator to obtain 13 consequetive numbers and store it in y
And we update the value of x by x/10 to keep the values for y moving.
then we another while loop to caluclate the product of thr digits of y.
Note: Be sure to use // instead of int(a/b) since the latter gives an overflow error.
