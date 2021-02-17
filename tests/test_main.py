import os
from unittest import TestCase

from main import api002


class TestMain(TestCase):
    def test_api002(self):
        api_key = os.environ['api_key']
        exp_dclr_no = '122100900340033'
        expected = {
            "mnurConm": "티지에스파이프(주)",
            "acptDt": "20091229",
            "exppnConm": "티지에스파이프(주)",
            "loadDtyTmlm": "20100128",
            "sanm": "OCEAN HOPE",
            "acptDttm": "110958",
            "shpmPckGcnt": "61",
            "csclPckUt": "BE",
            "shpmPckUt": "GT",
            "shpmCmplYn": "Y",
            "shpmWght": "60678",
            "expDclrNo": "122100900340033",
            "csclWght": "60678.0",
            "csclPckGcnt": "61",
            "details": [
                {
                    "shpmPckUt": "GT",
                    "shpmWght": "60678",
                    "tkofDt": "20100107",
                    "shpmPckGcnt": "61",
                    "blNo": "HDMUPGOHS9311600"
                }
            ]
        }

        result = api002(api_key=api_key, exp_dclr_no=exp_dclr_no)
        self.assertDictEqual(expected, result)
