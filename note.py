num_data = 100

k = 10

bins = int(num_data/k)  # 1000

start = 2*bins # 2000
end = (2+1)*bins # 3000

train_index = list(range(0,start)) + list(range(end, num_data))

print(train_index) # [0 ~ 1999] + [3000~9999]
