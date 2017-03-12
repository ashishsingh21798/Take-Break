import time
import webbrowser

total_break = 3
break_count = 0

print("This program started on "+ time.ctime())

while(break_count < total_break):
    time.sleep("put time in second without quort")
    webbrowser.open("put your link here")
    break_count = break_count + 1
