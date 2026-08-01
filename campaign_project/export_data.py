import pandas as pd
import sqlite3

# เชื่อมต่อกับไฟล์ฐานข้อมูล SQLite ของเรา
conn = sqlite3.connect('nykaa_dw.db')

# ใช้คำสั่ง SQL ดึงข้อมูลจากตารางที่ dbt สร้างไว้
query = "SELECT * FROM fact_campaign_performance"
df_final = pd.read_sql_query(query, conn)

# บันทึกเป็นไฟล์ .xlsx สำหรับใช้ใน Power BI
df_final.to_excel("final_campaign_dashboard_data.xlsx", index=False)

print("Export ไฟล์สำหรับ Power BI สำเร็จแล้ว!")