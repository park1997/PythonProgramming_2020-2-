import csv

# 참고
# dictionary 또는  defaultdict 또는 list 등 원하는 구조체 사용
# state_name 제공 (필요시 사용)

#from collections import defaultdict

state_name = ['Utah', 'Delaware', 'New Jersey', 'Arkansas', 'Illinois', 'Indiana', 'Arizona', 'District of Columbia', 'Montana', 'Minnesota', 'Maine', 'Virginia', 'West Virginia', 'Iowa', 'Hawaii', 'South Carolina', 'Tennessee', 'Georgia', 'Texas', 'Wyoming', 'Kentucky', 'South Dakota', 'Mississippi', 'Ohio', 'Florida', 'Idaho', 'Michigan', 'Colorado', 'Wisconsin', 'Connecticut', 'Kansas', 'Oklahoma', 'Pennsylvania', 'Washington', 'Massachusetts', 'North Carolina', 'Missouri', 'New York', 'Louisiana', 'New Hampshire', 'Maryland', 'New Mexico', 'North Dakota', 'Alaska', 'Rhode Island', 'Vermont', 'Oregon', 'Nevada', 'California', 'Alabama', 'Nebraska']

f = open("usa_alcohol_comsumption_data.csv", 'r')
reader = csv.reader(f)

new={}
dic={}

for i in reader:
    list2=[]
    if i[1] != "Year" and  2000<=int(i[1]) and int(i[1])<=2009:
        list2.append(i[2])
        list2.append(i[3])
        list2.append(i[4])

        if i[0] not in dic:
            dic[i[0]]=[float(list2[0]),float(list2[1]),float(list2[2])]
        else:
            dic[i[0]][0]+=float(list2[0])
            dic[i[0]][1]+=float(list2[1])
            dic[i[0]][2]+=float(list2[2])
sorted_dict = sorted(dic.items(), key=lambda x:x[1][1], reverse=True)

print("sorting by wine >>")
print(f'{"No.":^5}{"State":^20}{"beer":>15}{"wine":>15}{"spirits":>15}')
num=0
for i in sorted_dict:
    print("{:<3} {:^20} {:>15} {:>15} {:>13}".format(num,i[0], i[1][0], i[1][1], i[1][2]))
    num +=1
print("="*70)

## 결과 출력
