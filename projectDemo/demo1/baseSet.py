#集合
set1 = {'name', 'age', 'height', 11}
print(set1)
#去除某个元素，如果没有该元素则抛错
set1.discard('2')
#去除某个元素，如果没有则返回原集合
set1.remove('23')
