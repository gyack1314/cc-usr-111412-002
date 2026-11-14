"""AI功能采用率的资格暴露与组织分层推断的数据读取入口。"""
from pathlib import Path
import json,hashlib
from cohorts import inspect_records

def read_inputs(path='data/source.json'):
    value=json.loads(Path(path).read_text(encoding='utf-8'))
    if not isinstance(value,dict):raise ValueError('分析资料根节点必须是对象')
    return value

def inspect_inputs(value):
    if not isinstance(value,dict):raise ValueError('分析资料必须是对象')
    sections={k:len(v) if isinstance(v,(list,dict)) else int(v is not None) for k,v in sorted(value.items())}
    encoded=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')
    return {'sections':sections,'sha256':hashlib.sha256(encoded).hexdigest(),'domain':inspect_records(value)}
