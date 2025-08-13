class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        answer = []
        
        #Get powers list
        bin_list = [int(num) for num in bin(n)[2:]]
        bin_list.reverse()
        powers = [2**x for x in range(len(bin_list))]
        powers = [power for mask, power in zip(bin_list,powers) if mask == 1]
    

        for query in queries:
            result = 1
            left = query[0]
            right = query[1]+1
            for x in powers[left:right]:
                result *= x
            answer.append(result % (10**9 + 7))

        return answer