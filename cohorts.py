"""AI功能采用率的资格暴露与组织分层推断的来源分区接口。"""
def inspect_records(data):
    rows=data.get('orgs')
    if not isinstance(rows,list):raise ValueError('业务分区必须为列表')
    if any(not isinstance(row,dict) for row in rows):raise ValueError('业务记录必须为对象')
    return {'section':'orgs','records':len(rows),'keys':sorted({k for row in rows for k in row})}
