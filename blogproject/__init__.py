# 导入函数:
import pymysql

# change mysqlclient version
pymysql.version_info = (1, 4, 6, 'final', 0)

# 调用该函数:
pymysql.install_as_MySQLdb()