# Solution Link
[Solution](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/editorial/)

# Things I used

- SQL left join
- pandas merge

# Thoughts on my solution
The core left join is a standard use case for SQL.  For pandas I initially tried join, but realized that method uses the "other" data frame's index rather than a column.  The way to do the most SQL-like join is actually using merge.
