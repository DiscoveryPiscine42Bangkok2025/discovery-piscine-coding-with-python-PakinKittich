#!/usr/bin/env python3
import os

num = int(input())
folder = input()

for i in range(num):  # 0 → 14
    folder_name = f"{folder}/ex{i:02}"  # zero-padded, e.g., ex00
    os.makedirs(folder_name, exist_ok=True)
    print(f"Created {folder_name}")