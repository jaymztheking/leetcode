# Solution Link
[Solution](https://leetcode.com/problems/article-views-i/editorial/)

# Things I used

- pandas DataFrame constructor
- pandas method chaining
- pandas sort_values, unique
- basic SQL

# Thoughts on my solution

This problem added more wrinkles.  This time distinct and order by were necessary to solve as well as some column aliasing.  This wasn't much of a big deal in the SQL side, but the pandas portion was a little bit tedious, as I had to remember what function returned what data type (e.g. data frame vs series vs integer array).  I think that is a big detractor to pandas in that you seem to constantly be switching the same data between different data types and data structures.

After reading some comments I realize drop_duplicates method would have been better as it keeps the data frame data type but functionally does the same thing as unique in terms of the values