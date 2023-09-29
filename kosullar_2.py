# ve - veya
"""
                and (ve) için
        DEĞER1		DEĞER2		SONUÇ

        False		False		False
        True		False		False
        False		True		False
        True		True		True
        
        
        
                or (veya) için
        DEĞER1		DEĞER2		SONUÇ

        True		True		True
        True		False		True
        False		True		True
        False		False		False





"""

yas = 11
sinif = 51


if yas == 10 and sinif == 5:
    print("yaş ve sınıf doğru")
else:
    print("yaş ve sınıf yanlış")
    
if yas == 10 or sinif == 5:
    print("yaş ve/veya sınıf doğru")
else:
    print("yaş ve sınıf yanlış")



if yas == 10:
    if sinif == 5:
        print("yaş ve sınıf doğru")
    else:
        print("yaş doğru sınıf yanlış")
else:
    if sinif == 5:
        print("yaş yanlış ve sınıf doğru")
    else:
        print("yaş yanlış ve sınıf yanlış")
