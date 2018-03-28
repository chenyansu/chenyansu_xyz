import multiprocessing

bind = "0.0.0.0:8080"
workers = 2  #workers是工作线程数，一般设置成：服务器CPU个数 + 1
errorlog = '/var/log/gunicorn_chenyansu_xyz.error.log'
#accesslog = './gunicorn.access.log'
#loglevel = 'debug'
proc_name = 'chenyansu_xyz'