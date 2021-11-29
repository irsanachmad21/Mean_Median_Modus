import statistics

x = [0]*9
a = 1

while a <= 9:
    print("masukan bilangan ke ", a)
    x[a-1] = int(input())
    a = a+1

urutan = sorted(x)
hasil_mean = f"meannya adalah       = {statistics.mean(x):.2f}"
hasil_median = f"mediannya adalah     = {statistics.median(x)}"
hasil_modus = f"modusnya adalah      = {statistics.mode(x)}"
print()
print(5*"="+"HASILNYA"+"="*5)
print()
print("data awal ", x)
print("data urut ", urutan)
print(hasil_mean)
print(hasil_median)
print(hasil_modus)
