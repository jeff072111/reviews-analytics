data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完成', '總共有: ', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('每筆留言的平均長度為: ', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '個留言字母小於100')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('總共有', len(good), '筆留言裡面有Good')
print(good[0])

#清單快寫法
good = [d for d in data if 'good' in d]
print(len(good))
bad = ['bad' in d for d in data]
print(bad[0])