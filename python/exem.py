#Berilgan satrda nechta unli harf borligini hisoblaydigan dastur yozing.
def unli_harf_sanash(matn):
    unlilar = "aeiouAEIOU"
    sanash = sum(1 for harf in matn if harf in unlilar)
    return sanash

matn = input("Matn kiriting: ")
print("Unli harflar soni:", unli_harf_sanash(matn))

#Raqamlar roʻyxatini yarating va faqat juft sonlarni chop eting.
sonlar = list(range(1, 21))

# Faqat juft sonlarni chop etamiz
print("Juft sonlar:")
for son in sonlar:
    if son % 2 == 0:
        print(son)


#Satrni slicing ([::-1]) ishlatmasdan teskari chiqaradigan dastur yozing.
def teskari_satr(matn):
    teskari = ""
    for harf in matn:
        teskari = harf + teskari  # har bir harfni boshiga qo‘shamiz
    return teskari

# Foydalanuvchidan satr kiritamiz
satr = input("Satr kiriting: ")
print("Teskari satr:", teskari_satr(satr))


#Sonning faktorialini sikl yordamida hisoblaydigan dastur yozing.
def faktorial(n):
    natija = 1
    for i in range(1, n + 1):
        natija *= i
    return natija

# Foydalanuvchidan son kiritishni so‘raymiz
son = int(input("Son kiriting: "))

if son < 0:
    print("Faktorial faqat musbat sonlar uchun mavjud.")
else:
    print(f"{son} ning faktoriali: {faktorial(son)}")


#Berilgan son palindrom ekanligini tekshiradigan dastur yozing (masalan, 121 → palindrom).
def palindrommi(son):
    # Sonni satrga aylantiramiz
    satr = str(son)
    # Teskari qilib solishtiramiz
    return satr == satr[::-1]

# Foydalanuvchidan son kiritamiz
son = int(input("Son kiriting: "))

if palindrommi(son):
    print(f"{son} palindrom son.")
else:
    print(f"{son} palindrom emas.")


#10 ta sondan iborat roʻyxat yarating. Juft indekslardagi sonlar yigʻindisini hisoblang.
# 10 ta sondan iborat ro'yxat
sonlar = [5, 8, 12, 3, 7, 9, 4, 6, 10, 2]

# Juft indekslardagi elementlar yig'indisi
yigindi = 0
for i in range(0, len(sonlar), 2):  # faqat juft indekslar: 0, 2, 4, ...
    yigindi += sonlar[i]

# Natijani chiqaramiz
print("Ro'yxat:", sonlar)
print("Juft indekslardagi sonlar yig'indisi:", yigindi)



#Ikki o‘zgaruvchini uchinchi o‘zgaruvchi ishlatmasdan almashtiradigan dastur yozing.
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

a, b = b, a  # almashtirish

print("Almashtirilgandan so'ng:")
print("a =", a)
print("b =", b)

#Butun sonlar roʻyxati berilgan. Takroriy qiymatlarni olib tashlab, faqat noyob qiymatlardan iborat yangi roʻyxat yarating.
sonlar = [4, 7, 2, 4, 9, 2, 5, 7, 1, 3]

# Takroriy qiymatlarni olib tashlaymiz
noyob_sonlar = list(set(sonlar))

print("Asl ro'yxat:", sonlar)
print("Noyob qiymatlar:", noyob_sonlar)


#Satrdagi har bir belgining chastotasini hisoblab, dictionary da saqlaydigan dastur yozing.
def chastota_hisobla(satr):
    chastotalar = {}  # Bo'sh lug'at (dictionary)

    for belgi in satr:
        if belgi in chastotalar:
            chastotalar[belgi] += 1
        else:
            chastotalar[belgi] = 1

    return chastotalar

# Foydalanuvchidan satr kiritamiz
satr = input("Satr kiriting: ")

natija = chastota_hisobla(satr)

print("Belgilar chastotasi:")
for belgi, soni in natija.items():
    print(f"'{belgi}': {soni} marta")


# ["apple", "banana", "cherry"] roʻyxatini so‘zlarni key, ularning uzunligini value qilib dictionary ga aylantiring.
sozlar = ["apple", "banana", "cherry"]

# Lug'at yaratamiz: so'z -> uzunligi
lugat = {soz: len(soz) for soz in sozlar}

print("Natija:")
print(lugat)


#Sonlar roʻyxati berilgan. Ularni juft va toq sonlar roʻyxatiga ajrating.
# Asosiy sonlar ro'yxati
sonlar = [12, 7, 9, 4, 10, 3, 8, 1, 5, 6]

# Bo'sh ro'yxatlar: juft va toq sonlar uchun
juft_sonlar = []
toq_sonlar = []

# Har bir sonni tekshirib ajratamiz
for son in sonlar:
    if son % 2 == 0:
        juft_sonlar.append(son)
    else:
        toq_sonlar.append(son)

# Natijani chiqaramiz
print("Asl ro'yxat:", sonlar)
print("Juft sonlar:", juft_sonlar)
print("Toq sonlar:", toq_sonlar)


#5 ta talabaning baholarini dictionary shaklida yarating. Eng yuqori bahoga ega talabani chiqaring.
# Talabalar va ularning baholari
baholar = {
    "Ali": 87,
    "Vali": 92,
    "Aziza": 78,
    "Dilshod": 95,
    "Malika": 89
}

# Eng yuqori bahoga ega talaba
eng_yuqori_talaba = max(baholar, key=baholar.get)
eng_yuqori_baho = baholar[eng_yuqori_talaba]

# Natijani chiqaramiz
print("Eng yuqori bahoga ega talaba:")
print(f"{eng_yuqori_talaba} → {eng_yuqori_baho} ball")


#Gapdagi nechta so‘z unli harf bilan boshlanishini sanaydigan funksiya yozing.
def unli_bilan_boshlanuvchi_sozlar_soni(gap):
    unli_harf = "aeiouAEIOU"  # Unli harflar (kichik va katta)
    sozlar = gap.split()      # Gapni so'zlarga ajratamiz
    sanash = 0

    for soz in sozlar:
        if soz and soz[0] in unli_harf:
            sanash += 1

    return sanash
gap = input("Gap kiriting: ")
natija = unli_bilan_boshlanuvchi_sozlar_soni(gap)
print(f"Unli harf bilan boshlanuvchi so'zlar soni: {natija}")

#Ichma-ich roʻyxatni tekislab chiqaradigan dastur yozing. Masalan: [[1,2],[3,4],[5]] → [1,2,3,4,5].
nested = [[1, 2], [3, 4], [5]]
tekis = []

for kichik_royxat in nested:
    for element in kichik_royxat:
        tekis.append(element)

print("Tekislangan ro'yxat:", tekis)


#Ikki dictionary ni bitta dictionary ga birlashtiradigan dastur yozing.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

birlashtirilgan = dict1 | dict2

print("Birlashtirilgan dictionary:", birlashtirilgan)
