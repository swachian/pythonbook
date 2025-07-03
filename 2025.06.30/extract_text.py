# from PIL import Image
# import pytesseract
# import csv

# # 从图片提取文字
# custom_config = r'--oem 3 --psm 6 -l chi_sim+eng' 
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# text = pytesseract.image_to_string(
#     Image.open("processed.png"), 
#     config=custom_config)
# print(text)
# lines = text.split("\n")


# # 保存为CSV
# with open("output.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Text"])
#     for line in lines:
#         if line.strip():  # 跳过空行
#             writer.writerow([line.strip()])

from paddleocr import PaddleOCR
import cv2
import numpy as np

# image = cv2.imread("image.png")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转灰度
# gray = cv2.medianBlur(gray, 3)  # 去噪
# gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]  # 二值化
# cv2.imwrite("processed.png", gray)  # 保存处理后的图片


# 初始化OCR（自动下载模型）
ocr = PaddleOCR(
        # 基础配置
    lang="ch",                # 中文模型
    use_angle_cls=False,      # 关键！关闭方向分类（避免误判竖向文本）
    show_log=False,           # 关闭日志输出（可选）

    # 文本检测优化
    det_model_dir=None,       # 默认使用PP-OCRv4检测模型（高精度）
    det_db_unclip_ratio=2.0,  # 放宽检测框（适应文字间距）
    det_db_thresh=0.3,        # 降低检测阈值（提升小文本检出）
    use_dilation=True,        # 膨胀检测（增强密集文本）

    # 文本识别优化
    rec_model_dir=None,       # 默认使用PP-OCRv4识别模型
    rec_algorithm="SVTR_LCNet",  # 平衡速度与精度
    )
result = ocr.predict("processed.png")  

# 打印结果
for line in result:
    line.print()
    line.save_to_json("output")