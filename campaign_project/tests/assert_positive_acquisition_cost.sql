-- ใช้คอนเซปต์ BVA: ตรวจสอบขอบเขตล่างของต้นทุน (ต้องไม่ต่ำกว่า 0) ถ้าค้นเจอข้อมูลที่ต้นทุนติดลบ ให้ถือว่าเทสต์ "ไม่ผ่าน"
SELECT
    Campaign_ID,
    Acquisition_Cost
FROM {{ ref('fact_campaign_performance') }}
WHERE Acquisition_Cost < 0