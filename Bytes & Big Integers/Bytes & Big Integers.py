from Crypto.Util.number import bytes_to_long, long_to_bytes

numbers = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
data = long_to_bytes(numbers)
print(data)