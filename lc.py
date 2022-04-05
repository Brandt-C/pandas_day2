

# def beams(arr):
#     ones = 0
#     for a in arr:
#         for x in range(len(arr[a])):
#             if arr[a].count('1'):
#                 ones +=1
#     return ones





# print(beams(["011001","000000","010100","001000"]))



def numBeams(bank):
    c = 0
    b = 0
    a = 0
    for x in range(len(bank)):
        if bank[x].count('1') != 0:
            b = bank[x].count('1')
            c += a*b
            a = b
    
    return c

print(numBeams(["000","111","000"]))



        # result = 0
        # onceki = 0

        # for index in bank:
        #   ones = index.count('1')
        #   if ones:
        #     result += onceki * ones
        #     onceki = ones

