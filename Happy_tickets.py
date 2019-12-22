x = 1
count = 0
while x < 1000000 :
    if (x%1000000//100000 + x%100000//10000 + x%10000//1000
        == x%1000//100 + x%100//10 + x%10) :
        print (str(x).zfill(6))
        count += 1
        x += 1
    else:
        x += 1
print ("Итого счастливых билетов: ", str(count))

