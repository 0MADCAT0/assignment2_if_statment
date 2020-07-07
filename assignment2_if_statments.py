# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:53:35 2020

@author: E2060-Fatih(MADCAT)
"""

a = age = input("Are you older than 75? (Y/N):").strip().upper()
b = addict = input("Are you addictted to cigaratte or side pruducts? (Y/N):").strip().upper()
c = chronic = input("Do you have a severe chronic disease? (Y/N):").strip().upper()
d = immune = input("Is your immune system too weak? (Y/N):").strip().upper()

if a == "Y" and b == "Y" and c == "Y" and d == "Y" :
  
   print("You are in risky group")

elif a == "Y" or b == "Y" or c == "Y" or d == "Y" :   

     print("Caution")
 
else :
    
   print("You are not in risky group")
