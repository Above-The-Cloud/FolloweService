from django.contrib import admin

from guide.models import Guide


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'username','avatar','position', 'title', 'content','cover','link','liked')

    #搜索字段
    # search_fields = ('id', 'trainno', 'start','end')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    # ordering = ('id',)

    # list_editable 设置默认可编辑字段
    # list_editable = ['username']

    # 设置哪些字段可以点击进入编辑界面
    # list_display_links = ('id', 'caption')
