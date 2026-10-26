# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:29:32 2026

@author: lab
"""

widgets = int(input("Enter the number of widgets ordered: "))

if w >= 100:
    total_cost = w * 0.20
else:
    total_cost = w * 0.25

print(f"Total cost: ${total_cost:.2f}")