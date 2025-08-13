# Solution Link
[Solution](https://leetcode.com/problems/recyclable-and-low-fat-products/editorial/)

# Things I used

- pandas to_frame
- enums for SQL creation
- very basic SQL

# Thoughts on my solution

The problem itself is about as straightforward as a problem gets.  Standard predicates.  The interesting things were in the setup.  Instead of a standard varchar column, they wanted to create enums.  The syntax didn't work natively and I had to make user-defined enums, then run the table DDL.  Seems like overkill for example tables.