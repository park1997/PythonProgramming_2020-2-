import csv

f = open("korea_floating_population_data.csv", 'r')
reader = csv.reader(f)

jongro = 0
dobong = 0

jongro_two = 0
jongro_five = 0

dobong_two = 0
dobong_five = 0


for i in reader:
    if "종로구" in i[7]:
        jongro += int(i[9])+int(i[10])+int(i[11])+int(i[12])+int(i[13])+int(i[14])+int(i[15])+int(i[16])+int(i[17])+int(i[18])
        jongro_two += int(i[10])+int(i[15])
        jongro_five += int(i[13])+int(i[18])
    if "도봉구" in i[7]:
        dobong += int(i[9])+int(i[10])+int(i[11])+int(i[12])+int(i[13])+int(i[14])+int(i[15])+int(i[16])+int(i[17])+int(i[18])
        dobong_two += int(i[10])+int(i[15])
        dobong_five += int(i[13])+int(i[18])

f.close()

## 출력 format
print("*"*55)
print("{:<4s}   {:<5s}  {:<4s}    {:<5s}   {:<5s}  {:<8s}".format("조사지역", "전체수 ", "20대", "20대비율", "50대", "50대비율"))
print("{:<8s}   {:<8s}  {:<8s}  {:<8s}   {:<8s} {:<8s}".format("Area", "Total ", "No.", "Rate%", "No.", "Rate%"))
print("*"*55)
# print("{:<4s}   {:<5}  {:<4}    {:<5}   {:<5}  {:<8}".format("종로구")
# print("{:<4s}   {:<5}  {:<4}    {:<5}   {:<5}  {:<8}".format("도봉구")
print(jongro,jongro_two,jongro_five,dobong,dobong_two,dobong_five)
