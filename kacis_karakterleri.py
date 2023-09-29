"""
\n\r		-> Bir satır aşağıya
\t			-> Tab tuşuna basılmış kabul eder
\b			-> Backspace yani geri tuşu

"""

metin = '''Bugün erken kalktım.
Annem güzel bir kahvaltı hazırlamıştı.
Kahvaltıdan sonra giyinip okula gittim.
Okulda arkadaşım Erdem beni bekliyordu.
Falan filan fişman
Ali veli deli
kırkdokuz ve elli
'''
print(metin2)


#cumle = '%s bana "Nasılsın" dedi?'
#cumle = "%s bana \"Nasılsın\" dedi?"

cumle = "%s bana \n\r\"Nasılsın\" \r\tdedi?"

kim = input("Sen kimsin?")

print(cumle % kim)
