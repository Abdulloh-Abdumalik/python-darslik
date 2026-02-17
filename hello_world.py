# -*- coding: utf-8 -*-
# 3-dars print funksiyasi
# Muallif: Abdulloh_Abdumalik


narh = 25000
choy = True
salat = False

if choy and salat:
    narh = narh + 10000
elif choy or salat:
    narh = narh + 5000
    
print(f"Jami {narh} so'm")