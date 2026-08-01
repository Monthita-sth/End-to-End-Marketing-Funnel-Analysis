### Using the starter project

Try running the following commands:
- dbt run
- dbt test

# 📊 End-to-End Marketing Funnel Analysis

โปรเจกต์ระบบท่อส่งข้อมูลการตลาด (Data Pipeline) แบบอัตโนมัติ เปลี่ยนข้อมูลดิบจากไฟล์ Excel ผ่านกระบวนการทำ Data Transformation ด้วย **dbt (data build tool)** บนฐานข้อมูล **SQLite** และประมวลผลด้วย **Python** ไปจนถึงการแสดงผลลัพธ์ผ่าน **Power BI Dashboard**

---

## 🚀 ขั้นตอนการทดสอบการอัปเดตข้อมูล (End-to-End Testing Workflow)

หากต้องการทดสอบระบบเมื่อมีข้อมูลแคมเปญการตลาดชุดใหม่เข้ามา สามารถทำตามขั้นตอนแบบจับมือทำได้ดังนี้:

### 📝 ขั้นตอนที่ 1: เพิ่มข้อมูลจำลองในไฟล์ต้นทาง
1. เปิดโฟลเดอร์หลัก `Marketing Funnel Analysis`
2. เปิดไฟล์ **`cleaned_campaign_data.xlsx`** ด้วยโปรแกรม Excel
3. เลื่อนลงไปที่บรรทัดล่างสุด แล้วเพิ่มข้อมูลจำลอง 1 แถว (แนะนำให้ใส่ตัวเลขสูงๆ เพื่อให้สังเกตความเปลี่ยนแปลงบน Dashboard ได้ชัดเจน):
   * **Campaign_ID:** `TEST-999`
   * **Duration:** `30`
   * **Channel_Used:** `Social Media`
   * **Impressions:** `10000000` (10 ล้าน)
   * **Clicks:** `500000` (5 แสน)
   * **Leads:** `50000`
   * **Conversions:** `10000`
   * **Revenue:** `50000000` (รายได้ 50 ล้านบาท)
   * **Acquisition_Cost:** `1000`
   * **Customer_Segment:** `Youth`
4. กด **Save** และ **ปิดไฟล์ Excel** *(สำคัญ: ต้องปิดโปรแกรม Excel ก่อนเริ่มรันโค้ดทุกครั้ง)*

---

### 💻 ขั้นตอนที่ 2: เปิด Terminal และ Activate Virtual Environment
1. เปิดโปรแกรม VS Code
2. ไปที่เมนู **Terminal** > **New Terminal**
3. ตรวจสอบว่าระบบอยู่ที่ตำแหน่งโฟลเดอร์ `campaign_project`
4. รันคำสั่งเปิดใช้งาน Virtual Environment:
   ```cmd
   ..\venv\Scripts\activate
### ⚙️ ขั้นตอนที่ 3: รันคำสั่งอัปเดตข้อมูลตามลำดับ (Data Pipeline)
พิมพ์คำสั่งใน Terminal ตามลำดับทีละคำสั่งดังนี้:
1. นำเข้าข้อมูลใหม่สู่ฐานข้อมูล SQLite:
   ```python load_data.py
   python load_data.py
   dbt run
   dbt test //ไม่จำเป็น
   python export_data.py //ส่งออกข้อมูลชุดใหม่สำหรับ Power BI
### 📊 ขั้นตอนที่ 4: อัปเดตการแสดงผลบน Power BI
- Link [Dashborad](https://app.powerbi.com/view?r=eyJrIjoiM2Q0NGIwMDQtZjQxNy00MDFiLTljYTQtNGUxZmRhOTFiYmE3IiwidCI6IjhlNjM0ZTY3LTlkNjYtNDZkMi1hNTI5LWUxYjcwOGM1ZDhiYyIsImMiOjEwfQ%3D%3D)
### 📚 dbt Project Starter Resources
- Learn more about dbt in the docs
- Check out Discourse for commonly asked questions and answers
- Join the chat on Slack for live discussions and support
- Find dbt events near you
### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
