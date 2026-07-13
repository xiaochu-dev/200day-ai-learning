#
# squares = [x**2 for x in range(10)]
# print(squares)
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)
# pairs = [(x, y) for x in range(10) for y in range(10)]
# print(pairs)
# sentence = "hello world this is a python learning day"
# long_words=[w.upper() for w in sentence.split() if len(w) > 3]
# print(long_words)
#
# word_length = {w:len(w) for w in sentence.split()}
# print(word_length)
# text = "apple banana apple orange banana apple"
# words = text.split()
# freq = {}
# for w in words:
#     freq[w] = freq.get(w, 0) + 1
# print(freq)
# sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
# print(sorted_freq)
#
# nums = [1,2,2,3,3,3,4]
# unique = set(nums)
# print(unique)
#
# a={1,2,3,4}
# b={3,4,5,6}
# print("交集：",a&b)
# print("并集：",a|b)
# print("差集：",a-b)
# print("对称差：",a^b)

digit = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6]
digit_qc = set(digit)
print(digit_qc)
digit_cs = {}
for d in digit:
    digit_cs[d] = digit_cs.get(d, 0) + 1
print(digit_cs)
digit_two = [d for d in digit_cs if digit_cs[d] >= 2]
print(digit_two)