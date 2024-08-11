app: chrome
-
tag(): browser
tag(): user.tabs


start my day:
    app.window_open()
    browser.go("https://outlook.office.com/mail/")
    app.window_open()
    browser.go("https://outlook.office.com/calendar/")
    app.window_open()
    browser.go("https://uclrsdt.harvestapp.com/time")
    app.window_open()
    browser.go("https://otter.ai/home")
    app.window_open()
    browser.go("https://mail.google.com/mail/u/0/?ogbl#inbox")

open male:
    app.window_open()
    browser.go("https://outlook.office.com/mail/")
    
open calendar:
    app.window_open()
    browser.go("https://outlook.office.com/calendar/")

open time sheet:
    app.window_open()
    browser.go("https://uclrsdt.harvestapp.com/time")

open otter:
    app.window_open()
    browser.go("https://otter.ai/home")

open google mail:
    app.window_open()
    browser.go("https://mail.google.com/mail/u/0/?ogbl#inbox")

open personal time sheet:
    app.window_open()
    browser.go("https://docs.google.com/spreadsheets/d/1PlwrassxaYlM2lyRDQEcbMSEhV1EA00pC7Ye_yW5lW4/edit#gid=621060324")
