import datetime

data_waktu = datetime.datetime.now()
print(data_waktu)

print(f"{data_waktu.microsecond}")

from collections import Counter

data = ["a","b","c","d","a","d","e"]

data_count = Counter(data)
print(data_count)
print(data_count["a"])