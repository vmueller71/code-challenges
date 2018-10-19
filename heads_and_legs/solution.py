"""
Write a program to solve this puzzle: 
We count 35 heads and 94 legs among the cats and parrots in a pet store. 
How many cats and how many parrots do we have?

It is possible that no solution can be found!

examples:
heads_and_legs(10, 40) returns (10, 0)
heads_and_legs(10, 20) returns (0, 10)
heads_and_legs(10, 30) returns (5, 5)
heads_and_legs(35, 94) returns (12, 23)
heads_and_legs(5, 15) returns (0, 0)

"""

def heads_and_legs(num_heads, num_legs):
    ns = 0
    for i in range(num_heads + 1):
        j = num_heads - i
        if (4 * i) + (2 * j)==num_legs:
            return i, j
    return ns, ns

