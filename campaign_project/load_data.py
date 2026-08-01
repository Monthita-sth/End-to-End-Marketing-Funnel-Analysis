import pandas as pd
import sqlite3

print("1. กำลังอ่านไฟล์ Excel...")
# ใช้ ../ เพราะไฟล์ Excel ของคุณอยู่ข้างนอกโฟลเดอร์ campaign_project 
df = pd.read_excel("../cleaned_campaign_data.xlsx")

print("2. กำลังโหลดเข้า Database...")
# เชื่อมต่อกับไฟล์ nykaa_dw.db ที่อยู่ในโฟลเดอร์นี้
conn = sqlite3.connect("nykaa_dw.db")

# เอาข้อมูลไปใส่ในตารางชื่อ raw_campaign_data
df.to_sql("raw_campaign_data", conn, if_exists="replace", index=False)

print("✅ โหลดข้อมูลใหม่เข้า Database สำเร็จแล้ว! พร้อมไปรัน dbt ต่อได้เลย")