import requests
import datetime
import hashlib
import json
from fake_useragent import UserAgent
from captchafill import get_captcha

def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()



# 教务系统地址
url = 'http://zhjw.scu.edu.cn/'
# 用户名及密码
username = '' 
password = ''
session = requests.session()
im_url = url + 'img/captcha.jpg'
im_data = session.get(im_url)
ua = UserAgent()
headers = {
    "User-Agent": ua.random
}

# 验证码处理及模拟登陆
with open('captcha.jpg', 'wb') as file:
    file.write(im_data.content)
captcha = get_captcha()
print("Captcha: ", captcha)
login_url = url + 'j_spring_security_check'
post_data = {
    'j_username': username,
    'j_password': md5(password),
    'j_captcha': captcha
}

# 课表数据获取
login_res = session.post(login_url, data=post_data, headers=headers)
table_url = url + 'student/courseSelect/thisSemesterCurriculum/ajaxStudentSchedule/curr/callback'
tablePage = session.get(table_url).text
table_byte = bytes(tablePage, 'utf-8')

# 数据预处理
with open('class.json', 'wb') as file:
    file.write(table_byte)
    file.close()

with open('class.json', "a+", encoding='utf-8') as f:
    old = f.read()
    f.seek(0)
    f.write(']')
    f.close()

with open('class.json', "r+", encoding='utf-8') as f:
    old = f.read()
    f.seek(0)
    f.write('[')
    f.write(old)

# 写入日历
# 第一周周一日期
startYear = 2021
startMonth = 3
startDay = 8

beginDate = datetime.date(startYear, startMonth, startDay)

startTime = ['08:15', '09:10', '10:15', '11:10', '13:50', '14:45', '15:40', '16:45', '17:40', '19:20', '20:15', '21:10']


endTime = ['09:00', '09:55', '11:00', '11:55', '14:35', '15:30', '16:25', '17:30', '18:25', '20:05', '21:00', '21:55']

weekName = ['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA']

VCALENDAR = '''BEGIN:VCALENDAR
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:%(username)s 课程表
X-WR-TIMEZONE:Asia/Shanghai
X-WR-CALDESC:%(username)s 课程表
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
X-LIC-LOCATION:Asia/Shanghai
BEGIN:STANDARD
TZOFFSETFROM:+0800
TZOFFSETTO:+0800
TZNAME:CST
DTSTART:19700101T000000
END:STANDARD
END:VTIMEZONE
''' % {'username': username}

file = open('课程表.ics', 'w', encoding='utf-8')
file.write(VCALENDAR)

with open("class.json", 'r', encoding='utf-8') as f:
    temp = json.loads(f.read())
    for index in range(len(temp[0]['dateList'][0]['selectCourseList'])):
        # 剔除未安排教室的课程
        if temp[0]['dateList'][0]['selectCourseList'][index]['timeAndPlaceList'] is None:
            continue
        for index1 in range(len(temp[0]['dateList'][0]['selectCourseList'][index]['timeAndPlaceList'])):
            className = temp[0]['dateList'][0]['selectCourseList'][index]['courseName']
            classBuilding = temp[0]['dateList'][0]['selectCourseList'][index]['timeAndPlaceList'][index1]['teachingBuildingName'].replace('体育场', '')
            for ch in range(65, 69):
                pos = classBuilding.find(chr(ch))
                if pos != -1:
                    classBuilding = classBuilding[:pos]
            classRoom = temp[0]['dateList'][0]['selectCourseList'][index]['timeAndPlaceList'][index1]['classroomName']
            campusName = temp[0]['dateList'][0]['selectCourseList'][index]['timeAndPlaceList'][index1]['campusName']
            classSession = temp[0]['dateList'][0]['selectCourseList'][index]['timeAndPlaceList'][index1][
                'classSessions']
            classAmount = temp[0]['dateList'][0]['selectCourseList'][index]['timeAndPlaceList'][index1][
                'continuingSession']
            classWeek = temp[0]['dateList'][0]['selectCourseList'][index]['timeAndPlaceList'][index1]['classDay']
            classWeekTimes = temp[0]['dateList'][0]['selectCourseList'][index]['timeAndPlaceList'][index1][
                'weekDescription'].split(',')
            weekArray = str(temp[0]['dateList'][0]['selectCourseList'][index]['timeAndPlaceList'][index1]['classWeek'])+'0'
            index3 = 0
            while True:
                tmp = weekArray[index3:].find('1')
                if tmp == -1:
                    break
                else:
                    index3 += tmp
                WeekTimes = index3
                VEVENT = ''
                VEVENT += 'BEGIN:VEVENT\n'
                # 周次
                # 开始周
                delta = datetime.timedelta(weeks=int(WeekTimes))
                # 开始星期
                delta += datetime.timedelta(days=int(classWeek) - 1)
                classStartTime = beginDate + delta
                # 开始日期
                classStartDate = beginDate + delta
                # 开始时间
                classStartTime = datetime.datetime.strptime(
                    startTime[int(classSession)], '%H:%M').time()
                # 结束时间
                classEndTime = datetime.datetime.strptime(
                    endTime[int(classSession) + int(classAmount) - 1], '%H:%M').time()
                # 最终开始时间
                classStartDateTime = datetime.datetime.combine(
                    classStartDate, classStartTime)
                # 最终结束时间
                classEndDateTime = datetime.datetime.combine(
                    classStartDate, classEndTime)
                # 写入开始时间
                VEVENT += 'DTSTART;TZID=Asia/Shanghai:{classStartDateTime}\n'.format(
                    classStartDateTime=classStartDateTime.strftime(
                        '%Y%m%dT%H%M%S'))
                # 写入结束时间
                VEVENT += 'DTEND;TZID=Asia/Shanghai:{classEndDateTime}\n'.format(
                    classEndDateTime=classEndDateTime.strftime(
                        '%Y%m%dT%H%M%S'))

                # 设置循环
                tmp = weekArray[index3:].find('0')
                index3 += tmp
                endWeektime = index3
                VEVENT += 'RRULE:FREQ=WEEKLY;WKST=MO;COUNT={count};BYDAY={byday}\n'.format(count=str(endWeektime - WeekTimes), byday=weekName[int(classWeek)])
                # 地点
                VEVENT += ('LOCATION:' + campusName + classBuilding + classRoom + '\n')
                # 名称
                VEVENT += ('SUMMARY:' + className + '\n')
                VEVENT += 'END:VEVENT\n'
                file.write(VEVENT)

    file.write('END:VCALENDAR')
    file.close()
f.close()
print('Finished, all info is written in "课程表.ics".')