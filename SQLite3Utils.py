# _*_ coding: utf-8 _*_
# coding: utf-8
# @Author : waylanpunch
# @Time : 2021/7/19 7:50
# @File : SQLite3Utils.py
# @Software : PyCharm
import sqlite3  # 进行sqlite数据库操作
from datetime import datetime
import os.path


def checkIfSQLitePrepared(databasePath):
    if (os.path.isfile(databasePath)):
        print("Already Have It")
    else:
        print("Don't Have It")
        initSQLite(databasePath)


def initSQLite(databasePath):
    try:
        connection = sqlite3.connect(databasePath)
        cursor = connection.cursor()
        sqlTable = '''
        create table if not exists job 
        (type VARCHAR,
          jt VARCHAR,
          tags VARCHAR,
          ad_track VARCHAR,
          jobid VARCHAR,
          coid VARCHAR,
          effect VARCHAR,
          is_special_job VARCHAR,
          job_href TEXT,
          job_name VARCHAR,
          job_title VARCHAR,
          company_href TEXT,
          company_name VARCHAR,
          providesalary_text VARCHAR,
          workarea VARCHAR,
          workarea_text VARCHAR,
          updatedate VARCHAR,
          iscommunicate VARCHAR,
          companytype_text VARCHAR,
          degreefrom VARCHAR,
          workyear VARCHAR,
          issuedate VARCHAR,
          isFromXyz VARCHAR,
          isIntern VARCHAR,
          jobwelf VARCHAR,
          jobwelf_list TEXT,
          isdiffcity VARCHAR,
          attribute_text TEXT,
          companysize_text VARCHAR,
          companyind_text VARCHAR,
          adid VARCHAR)
        '''
        cursor.execute(sqlTable)
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
        print("init end")


def removeAllDataFromSQLite(databasePath):
    print("Starting to truncate table...")
    try:
        connection = sqlite3.connect(databasePath)
        cursor = connection.cursor()
        truncateSql = "DELETE FROM job"
        cursor.execute(truncateSql)
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
        print("truncate end")


def storeDataToSQLite(dataList, databasePath):
    print("Starting to store data...")
    try:
        connection = sqlite3.connect(databasePath)
        cursor = connection.cursor()
        # columnCount = 10
        # rowCount = len(dataList)

        for data in dataList:
            print(type(data))

            tags = data["tags"]
            tagsStr = ",".join([str(item) for item in tags])
            data["tags"] = tagsStr

            updatedate = data["updatedate"]
            year = datetime.today().year
            data["updatedate"] = str(year) + "-" + updatedate

            jobwelf_list = data["jobwelf_list"]
            jobwelf_listStr = ",".join([str(item) for item in jobwelf_list])
            data["jobwelf_list"] = jobwelf_listStr

            attribute_text = data["attribute_text"]
            attribute_textStr = ",".join([str(item) for item in attribute_text])
            data["attribute_text"] = attribute_textStr

            for (k, v) in data.items():
                data[k] = '"' + data[k] + '"'
            sqlRow = '''
                    insert into job 
                    (type ,
                      jt ,
                      tags ,
                      ad_track ,
                      jobid ,
                      coid ,
                      effect ,
                      is_special_job ,
                      job_href ,
                      job_name ,
                      job_title ,
                      company_href ,
                      company_name ,
                      providesalary_text ,
                      workarea ,
                      workarea_text ,
                      updatedate ,
                      iscommunicate ,
                      companytype_text ,
                      degreefrom ,
                      workyear ,
                      issuedate ,
                      isFromXyz ,
                      isIntern ,
                      jobwelf ,
                      jobwelf_list ,
                      isdiffcity ,
                      attribute_text ,
                      companysize_text ,
                      companyind_text ,
                      adid )
                    values (%s)
                    ''' % ",".join(list(data.values()))
            # print(sqlRow)
            cursor.execute(sqlRow)
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
        print("store end")


def readDataFromSQLite(databasePath):
    try:
        connection = sqlite3.connect(databasePath)
        cursor = connection.cursor()
        sqlRows = '''
        select jobid,
        coid,
        job_href,
        job_name,
        job_title,
        company_href,
        company_name,
        providesalary_text,
        workarea,
        workarea_text,
        updatedate,
        companytype_text,
        jobwelf_list,
        attribute_text,
        companysize_text,
        companyind_text from job
        '''
        result = cursor.execute(sqlRows)
        jobs = []
        for row in result:
            print(type(row))
            for column in row:
                print(column)
            print("\n")
            jobs.append(row)
        return jobs
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
        print("read end")


if __name__ == '__main__':
    # databasePath = "51job.db"
    # initSQLite(databasePath)
    # readDataFromSQLite(databasePath)
    # checkIfSQLitePrepared(databasePath)
    a = ["d", "g"]
    b = ",".join([str(item) for item in a])
    print(b)
    dt = datetime.today()
    d = {'Michael': "sdf", 'Bob': "dt", 'Tracy': "dt"}
    print(d.values())
    print(type(d))
    st = ","
    print(st.join(list(d.values())))
    year = datetime.today().year
    print(str(year))
