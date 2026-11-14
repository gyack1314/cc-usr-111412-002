"""读取当前分析资料的结构和摘要。"""
import json
from analytics import read_inputs,inspect_inputs
def main():print(json.dumps(inspect_inputs(read_inputs()),ensure_ascii=False,indent=2))
if __name__=='__main__':main()
