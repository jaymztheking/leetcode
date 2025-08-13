# Solution Link
[Solution](https://leetcode.com/problems/range-product-queries-of-powers/editorial)

# Things I used

- zip function, put two lists together in a 2d list
- reverse list function, to switch the binary around
- bin function, convert integer to string binary (e.g. 0b01100010)

# Thoughts on my solution

After seeing the official answer, it was interesting to see them building the powers list computationally using mod 2 in a while loop. There was also the idea to pre compute many of the answers and then simply look up query pairs from the complete answers list.  This would be good savings if there are many, duplicate queries. 

Conceptually, I understood that we wanted to convert to binary.  I'm not sure which