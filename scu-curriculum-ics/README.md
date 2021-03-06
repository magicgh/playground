# SCU Curriculum ICS
自动获取四川大学教务管理系统的课程表信息并生成 `.ics` 日历文件。
## Usage
在 `main.py` 中填写本学期第一周周一的日期、四川大学教务系统用户名及密码信息，即可运行。
```python
startYear = 2021
startMonth = 3
startDay = 1
```
```python
# 用户名及密码
username = '' 
password = ''
```
## Miscellaneous
* 导入非江安校区的课程信息，课程时间以江安校区的教学时间为准。
* 支持单双周、非连续周课程的导入。
* （可选）导入未安排教室的课程。