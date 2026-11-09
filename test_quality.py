import sys,unittest
from pathlib import Path
from datetime import date
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from quality import evaluate
class TestQuality(unittest.TestCase):
    def test_good_and_bad(self):
        a={'transaction_id':'1','day':'2026-01-01','amount':'3'}
        self.assertTrue(evaluate([a],as_of=date(2026,1,5))['passed'])
        self.assertFalse(evaluate([a,a],as_of=date(2026,1,5))['passed'])
