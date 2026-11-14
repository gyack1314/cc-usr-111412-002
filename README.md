# AI功能采用率的资格暴露与组织分层推断

本项目整理智能消费与数字服务分析所需的合成业务记录。示例用于检查输入结构和内容身份，不代表新闻中的平台数据或企业事实。`analytics.py`提供JSON输入读取及分区概览；`cohorts.py`读取组织历史与活跃事件并保留其来源分区身份；通用输入层会返回该分区记录摘要。字段边界见[分析契约](docs/contracts.md)。

使用Python 3.11及标准库。

```sh
python -m unittest discover -s tests -v
python -m compileall -q analytics.py tests
python analytics_cli.py
```

在Linux容器中可通过Dockerfile执行同一套基线检查。
