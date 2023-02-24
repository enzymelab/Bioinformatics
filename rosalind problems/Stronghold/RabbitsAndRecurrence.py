def FibonacciLoop(months, offspring):
    parent = 1
    child = 1
    for itr in range(months-1):
        tmpVal = child
        child = parent
        parent = parent + tmpVal * offspring
    return child


print(FibonacciLoop(34, 2))

"""o - small (children) rabbits. They have to mature and reproduce in the next cycle only.
0 - mature(parents) rabbits. They can reproduce and move to the next cycle.
Month 5 offspring 2
Month 1: [o]
Month 2: [0]
Month 3: [0 o o]
Month 4: [0 o o 0 0]
Month 5: [0 o o 0 0 0 o o 0 o o] 
Month 6: [0 o o 0 0 0 o o 0 o o 0 o o 0 0 0 o o 0 0]   


"""


# Rabbits with a recursion
# def WascallyWabbits(month, offspringCount):
#     if month == 1:
#         return 1

#     elif month == 2:
#         return offspringCount

#     oneGen = WascallyWabbits(month - 1, offspringCount)
#     twoGen = WascallyWabbits(month - 2, offspringCount)

#     if month <= 4:
#         return (oneGen + twoGen)

#     return (oneGen + (twoGen * offspringCount))


# # TESTS

# print(WascallyWabbits(35, 5))
