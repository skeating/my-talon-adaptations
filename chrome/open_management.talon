app: chrome
-
tag(): browser
tag(): user.tabs

 
open management meeting:
    browser.go("https://github.com/orgs/UCL-ARC/projects/7/views/14")
    app.tab_open()
    browser.go("https://github.com/orgs/UCL-ARC/projects/7/views/27")
    app.tab_open()
    browser.go("https://github.com/orgs/UCL-ARC/projects/18")
    app.tab_open()
    browser.go("https://github.com/orgs/UCL-ARC/projects/7/views/4")
    app.tab_open()
    browser.go("https://github.com/orgs/UCL-ARC/projects/7/views/2")

open work tribe:
    browser.go("https://ucl-research.worktribe.com")

open funding service:
    browser.go("https://funding-service.ukri.org/signIn")

open my opportunities:
    browser.go("https://github.com/UCL-ARC/arc-opportunities-tracker/issues?q=is%3Aissue%20state%3Aopen%20assignee%3Askeating")
    