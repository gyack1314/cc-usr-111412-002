# 分析资料契约

organization_id带有效起止时间，可变更industry与size；eligibility、enabled、first_call和daily_usage是事件而非互斥状态。组织合并有effective_at和source_id，冲突不得随意覆盖。cohort由首次enabled月冻结，随访截尾日统一；留存定义需在配置固定，活跃日按一次以上有效调用。报告含风险集分母、右截尾数、组织归属规则及整体/分层指标；不作因果解释。

资料按UTF-8 JSON保存，字段缺失与显式null须区分；报告使用实际可识别的观察范围。
