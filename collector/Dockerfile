# 1) ใช้ Python เวอร์ชัน 3.10 แบบ official image ขนาดเล็ก
FROM python:3.10-slim

# 2) ตั้ง working directory ใน container
WORKDIR /app

# 3) คัดลอก requirements.txt ก่อน เพื่อให้ Docker cache การติดตั้ง library ได้
COPY requirements.txt .

# 4) ติดตั้ง dependencies จาก requirements.txt
#    --no-cache-dir เพื่อลดขนาด image
RUN pip install --no-cache-dir -r requirements.txt

# 5) คัดลอกไฟล์โค้ดทั้งหมดจาก host ลงใน container
COPY . .

# 6) คำสั่งเริ่มต้นเมื่อ container รัน
CMD ["python", "main.py"]
