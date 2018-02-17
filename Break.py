import webbrowser
import time


total_breaks = 1
break_count = 0

while(break_count != total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=1EA8g4-vEAQ")
    break_count = break_count+1

print("done")
