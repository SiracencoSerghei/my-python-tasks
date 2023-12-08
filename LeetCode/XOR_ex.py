# Initializing two integers a and b
a = 4
b = 6

# Finding XOR of a and b using ^ operator
c = a ^ b
print(c)


"""There is a hidden integer array arr that consists 
of n non-negative integers.

It was encoded into another integer array encoded 
of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. 
For example, if arr = [1,0,2,1], then encoded = [1,2,3].

You are given the encoded array. You are also given 
an integer first, that is the first element of arr, i.e. arr[0].

Return the original array arr. 
It can be proved that the answer exists and is unique.

 

Example 1:

Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
Explanation: If arr = [1,0,2,1], 
then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]

Example 2:

Input: encoded = [6,2,7,3], first = 4
Output: [4,2,0,7,4]
 

Constraints:

2 <= n <= 104
encoded.length == n - 1
0 <= encoded[i] <= 105
0 <= first <= 105"""

class Solution:
    def encode(self, decoded):
        encoded = []
        for i in range(len(decoded)):
            encoded.append(decoded[i] ^ decoded[i+1])
        return encoded
    def decode(self, encoded, first):
        decoded = [first]
        for i in range(len(encoded)):
            decoded.append(encoded[i] ^ decoded[-1])
        return decoded


# ex_1 : 

solution_instance = Solution()
encoded = [1, 2, 3]
first = 1
decoded = solution_instance.decode(encoded, first)
print(decoded)  # Output: [1,0,2,1]

# ex_2 :

solution_instance2 = Solution()  # Create an instance of the Solution class
encoded = [6,2,7,3]
first = 4
decoded = solution_instance2.decode(encoded, first)
print(decoded)  # Output: [4,2,0,7,4]

