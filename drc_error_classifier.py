# DRC错误分类器 v0.1
import pandas as pd

error_db = {
    'MET1': ['Width Violation', 'Spacing Error'],
    'VIA1': ['Overlap Issue', 'Enclosure Fail']
}

def classify_error(layer, code):
    return error_db.get(layer, ['Unknown']) if code < 50 else 'Critical Error'

# 示例用法
print(classify_error('MET1', 30))  # 输出: Width Violation
print(classify_error('VIA1', 60))  # 输出: Critical Error