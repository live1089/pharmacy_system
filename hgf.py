import os
import sys

# 获取当前文件的绝对路径和所在目录
file_path = os.path.abspath(__file__)
base_path = os.path.dirname(file_path)

# 创建可视化展示
print("路径解析结果:")
print("=" * 50)
print(f"当前文件: {os.path.basename(__file__)}")
print(f"文件绝对路径: {file_path}")
print(f"所在目录: {base_path}")
print("=" * 50)

# 显示目录结构
print("\n目录结构:")
print("=" * 50)
for root, dirs, files in os.walk(base_path):
    level = root.replace(base_path, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        if file == os.path.basename(__file__):
            print(f"{subindent}📄 {file} (当前文件)")
        else:
            print(f"{subindent}📄 {file}")
    # 只显示当前目录的内容
    break