import webbrowser
urls = ["https://pomofocus.io/","https://leetcode.com/","https://www.youtube.com/watch?v=lcYJhHqotIQ"]

webbrowser.register('firefox',None,
webbrowser.BackgroundBrowser(r"C:\Program Files\Mozilla Firefox\firefox.exe"))
firefox = webbrowser.get('firefox')
for url in urls:
    firefox.open_new_tab(url)
    


    