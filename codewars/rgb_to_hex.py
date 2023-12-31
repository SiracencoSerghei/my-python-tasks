"""

The rgb function is incomplete. 
Complete it so that passing in RGB decimal values will result 
in a hexadecimal representation being returned. 
Valid decimal values for RGB are 0 - 255. 
Any values that fall out of that range must be rounded 
to the closest valid value.

Note: Your answer should always be 6 characters long, 
the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""


# def rgb(r, g, b):
#     def clamp(value):
#         return min(255, max(0, value))
#
#     r = clamp(r)
#     g = clamp(g)
#     b = clamp(b)
#
#     return f"{r:02X}{g:02X}{b:02X}"

def rgb(r, g, b):
    return ('{0:02X}{1:02X}{2:02X}'
            .format(max(min(r, 255), 0),
                    max(min(g, 255), 0),
                    max(min(b, 255), 0)))
    

result = rgb(255, 255, 255)
print(result)
