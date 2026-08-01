WITH raw_data AS (
    SELECT 
        Campaign_ID,
        Campaign_Type,
        Customer_Segment,
        Duration,
        Impressions,
        Clicks,
        Conversions,
        Revenue,
        Acquisition_Cost,
        ROI
    FROM raw_campaign_data
),

calculated_metrics AS (
    SELECT 
        *,
        -- คำนวณ Conversion Rate เป็นเปอร์เซ็นต์
        CASE 
            WHEN Clicks > 0 THEN ROUND((CAST(Conversions AS FLOAT) / Clicks) * 100, 2)
            ELSE 0 
        END AS Conversion_Rate_Pct,
        
        -- จัดหมวดหมู่ประสิทธิภาพ (Feature Engineering)
        CASE 
            WHEN ROI >= 3.0 THEN 'High Performance'
            WHEN ROI >= 1.0 AND ROI < 3.0 THEN 'Medium Performance'
            ELSE 'Low/Negative Performance'
        END AS Performance_Status
    FROM raw_data
)

SELECT * FROM calculated_metrics