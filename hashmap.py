nums = [1, 2, 2, 3, 1]
 
freq = {}
 
for num in nums:

    if num in freq:

        freq[num] += 1

    else:

        freq[num] = 1
 
print(freq)  # Output: {1: 2, 2: 2, 3: 1}
res = []
for key in freq:
    res.append(key)
print(res)

for key,value in freq.items():
    if value > 1:
        freq[key] = [value, True]
    else:
        freq[key] = [value, False]
print(freq)


 