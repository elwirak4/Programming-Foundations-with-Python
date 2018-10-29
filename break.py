import time
import webbrowser
total_breaks = 3
breaks_count = 0
print("This program starts on "+time.ctime())
while (breaks_count < total_breaks):
    time.sleep(10)
    webbrowser.open("http://www.google.com")
    breaks_count = breaks_count + 1
