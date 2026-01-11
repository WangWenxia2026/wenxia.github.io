#!/usr/bin/env python3
"""
将大学logo转换为圆形PNG格式
"""

from PIL import Image, ImageDraw, ImageOps
import os

def create_circular_image(input_path, output_path, size=(200, 200)):
    """
    将图片转换为圆形PNG格式
    
    Args:
        input_path: 输入图片路径
        output_path: 输出图片路径
        size: 输出图片尺寸（宽, 高）
    """
    # 打开原始图片
    img = Image.open(input_path)
    
    # 转换为RGBA模式（支持透明度）
    img = img.convert('RGBA')
    
    # 调整图片大小（保持纵横比，取最小边）
    img.thumbnail(size, Image.Resampling.LANCZOS)
    
    # 创建一个正方形的新图片
    square_size = min(img.size)
    
    # 如果图片不是正方形，裁剪成正方形
    if img.size[0] != img.size[1]:
        left = (img.size[0] - square_size) // 2
        top = (img.size[1] - square_size) // 2
        right = left + square_size
        bottom = top + square_size
        img = img.crop((left, top, right, bottom))
    
    # 缩放到目标大小
    img = img.resize(size, Image.Resampling.LANCZOS)
    
    # 创建圆形遮罩
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    
    # 创建输出图片
    output = Image.new('RGBA', size, (0, 0, 0, 0))
    output.paste(img, (0, 0))
    output.putalpha(mask)
    
    # 保存为PNG
    output.save(output_path, 'PNG')
    print(f"✓ 已创建圆形图片: {output_path}")

def main():
    # 当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 处理吉林大学logo
    jlu_input = os.path.join(current_dir, 'jlu.jpg')
    jlu_output = os.path.join(current_dir, 'jlu-logo.png')
    
    if os.path.exists(jlu_input):
        print(f"处理: {jlu_input}")
        create_circular_image(jlu_input, jlu_output)
    else:
        print(f"❌ 找不到文件: {jlu_input}")
    
    # 处理北京大学logo（如果存在）
    pku_input = os.path.join(current_dir, 'pku.png')
    pku_output = os.path.join(current_dir, 'pku-logo.png')
    
    if os.path.exists(pku_input):
        print(f"处理: {pku_input}")
        create_circular_image(pku_input, pku_output)
    else:
        print(f"ℹ️  未找到北大logo，跳过")
    
    print("\n✅ 转换完成！")
    print("生成的文件可以直接使用，已自动裁剪为圆形并带有透明背景。")

if __name__ == '__main__':
    main()
