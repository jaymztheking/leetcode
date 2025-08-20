# Solution Link
[Solution](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/editorial/)

# Things I used

- basic SQL, left joins, group by
- pandas loc with lambda for chaining, groupby and count, merge

# Thoughts on my solution

Again this one is a pretty easy problem in pure SQL, a left join filtered out non-nulls and grouped and counted.  I try to keep the pandas method chaining pattern and this time it involved loc and lambda to do the non-null filtering operation.  Still impressed/horrified at how many different data types Pandas methods accept and return.