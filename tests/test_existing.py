"""基础资料读取及错误路径。"""
import unittest,tempfile,json
from pathlib import Path
from analytics import read_inputs,inspect_inputs
from analytics_cli import main

class InputTests(unittest.TestCase):
    def test_sample_integrity(self):
        data=read_inputs();result=inspect_inputs(data)
        self.assertEqual(set(result),{'sections','sha256','domain'});self.assertEqual(len(result['sha256']),64)
        self.assertEqual(result['domain']['records'],result['sections'][result['domain']['section']])
        self.assertEqual(result['sections'],{k:len(v) if isinstance(v,(list,dict)) else int(v is not None) for k,v in sorted(data.items())})
    def test_root_type(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json';p.write_text('[]',encoding='utf-8')
            with self.assertRaises(ValueError):read_inputs(p)
