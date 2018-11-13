import os
import rarfile
import datetime

timer_start_time = datetime.datetime.now()

unrarpath = os.getcwd() + '\\unrar.exe'
rarfile.UNRAR_TOOL = unrarpath

