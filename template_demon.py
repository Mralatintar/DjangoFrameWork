# template = """
# 尊敬的%s:
#     我们将于%s在%s举办毕业典礼，邀请您昨晚这次典礼的观礼嘉宾
#                                                 %s
# """
#
# print(template%("懒洋洋","1888-02-04","羊村大酒店","灰太狼"))

template = """
尊敬的%(name)s:
    我们将于%(time)s在%(address)s举办毕业典礼，邀请您昨晚这次典礼的观礼嘉宾
    受邀嘉宾名单：
        %(name)s
        %(name)s
        %(name)s
        %(name)s
                                                %(yours)s
"""

print(template%{"name":"懒洋洋","time":"1888-02-04","address":"羊村大酒店","yours":"灰太狼"})