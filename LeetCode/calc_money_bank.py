"""Hercy wants to save money for his first car. 
He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, 
the first day. Every day from Tuesday to Sunday, 
he will put in $1 more than the day before. 
On every subsequent Monday, he will put 
in $1 more than the previous Monday.
Given n, return the total amount of money 
he will have in the Leetcode bank at the 
end of the nth day.
Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, 
the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, 
the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) 
+ (2 + 3 + 4) = 37. 
Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, 
the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) 
+ (2 + 3 + 4 + 5 + 6 + 7 + 8) 
+ (3 + 4 + 5 + 6 + 7 + 8) = 96.
 

Constraints:

1 <= n <= 1000"""

class Solutions:
    def totalMoney(self, n: int) -> int:
        
        sums = []
        if 1 <= n <= 1000:
            integer, remainder = divmod(n, 7)
            print(integer, remainder)
            for j in range(1, integer+1):
                integer_ammount =[i+j for i in range(0,7)]
                print(f"week_no: {j} - {integer_ammount}")
                week_ammount = sum(integer_ammount)
                sums.append(week_ammount)
                print(f'summ {j}: {sums}')
            if remainder:
                intermediate = [i+ integer for i in range(1,remainder +1)]
                print(f"last week: {intermediate}")
                remainder_ammount = sum(intermediate)
                sums.append(remainder_ammount)
                print(f'summ {j}: {sums}')
        total = sum(sums)
        return total
        
            

n = 20
solution = Solutions()
print(f"Total: {solution.totalMoney(n)}")
        