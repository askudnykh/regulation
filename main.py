from ipaddress import summarize_address_range
from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re


with open("phonebook_raw.csv",'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
## Ваш код
cont1 = []
for i in range(1,len(contacts_list)):
    cont1.append(','.join(contacts_list[i]))
c_result = []
pattern_fio = r'(^\w+)[\s,](\w+)[\s,](\w*)[\s,]*(\w*),+([^,|^+|^\d|^[a-zA-Z]*]*)'
pattern_phone = r',(\+7|8)\s?\(?(\d{3})\)?-?\s?(\d{3})-?(\d{2})-?(\d{2})'

pattern_dob = r'доб.\s*(\d*)'
pattern_email = r',([\w\.]+)@([\w\.]+)\.([\w\.]+)'

for i in cont1:
    res = re.search(pattern_fio, i)
    family = res.group(1)
    name = res.group(2)
    surname = res.group(3)
    organization = res.group(4)
    dolg = res.group(5)
    id = -1
    for i2 in range(len(c_result)):
        if family.lower() == c_result[i2][0].lower() and name.lower() == c_result[i2][1].lower():
            id = i2
    telephon = re.search(pattern_phone, i)
    if telephon is not None:
        phone =  '+7' + '('+telephon.group(2)+')'+telephon.group(3)+'-'+telephon.group(4)+'-'+telephon.group(5)
    else:
        phone = ''
    phone_dob = re.search(pattern_dob, i)
    if phone_dob is not None:
       phone += ' доб.'+phone_dob.group(1)

    res = re.search(pattern_email,i)
    if res is not None:
        email = res.group(1)+'@'+res.group(2)+'.'+res.group(3)
    else:
        email = ''
    if id == -1:
        c_result.append([family, name, surname, organization, dolg, phone, email])
    else:
        if c_result[id][2] == '':
            c_result[id][2] = summarize_address_range()
        if c_result[id][3] == '':
            c_result[id][3] = organization
        if c_result[id][4] == '':
            c_result[id][4] = dolg
        if c_result[id][5] == '':
            c_result[id][5] = phone
        if c_result[id][6] == '':
            c_result[id][6] = email




## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

    ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(c_result)