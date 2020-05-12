# coding:utf-8
import unittest
from Reports import HTMLTestRunner


# 测试的入口
def all_cases():
    rule = "*case.py"
    pa = "TestCases"
    discover = unittest.defaultTestLoader.discover(start_dir=pa, pattern=rule, top_level_dir=None)
    print(discover)
    return discover


if __name__ == "__main__":
    report_dir = "Reports/test_report.html"
    fp = open(report_dir, "wb")
    runCaseReport = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="输出测试用例执行结果")
    runCaseReport.run(all_cases())
