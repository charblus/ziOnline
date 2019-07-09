# -*- coding: utf-8 -*-
import xadmin

from .models import Course, Lesson, Video, CourseResource


# Course的admin管理器
class CourseAdmin(object):
    list_display = [
        'name',
        'desc',
        'detail',
        'degree',
        'learn_times',
        'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = [
        'name',
        'desc',
        'detail',
        'degree',
        'learn_times',
        'students']


# 章节models注册到xadmin
class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']

    # __name代表使用外键中name字段
    list_filter = ['course__name', 'name', 'add_time']



# 视频models注册到xadmin
class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']



# 资源models注册到xadmin
class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    # __name代表使用外键中name字段
    list_filter = ['course__name', 'name', 'download', 'add_time']


# 将管理器与model进行注册关联
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
