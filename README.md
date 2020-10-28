# Judging Web Server
## Functional Wireframe

## Description:
This is a complete Flask/Server implementation of the judging service spec developed by Kaiden. Everything here works, but is not ready for a production environment.

## Overview
#
The login page is the start for everything:

![Login](/docs/login.png)

From here there are 3 options:
- Username: "display", no password -> Team Judging Display
- Username: "admin", Password: "pyrsadmin" -> Admin Pannel (password can change)
- Username and Password for Judge specific account (create 1 for each judge)

### Submission
#
The most common form is submission for each judge:

![Submission](/docs/judge.png)

It displays the name of the judge, and a section to enter a team number and judged score. This can be expanded later.

### Admin
#
The admin display is as follows:

![Admin](/docs/admin.png)

It shows the tournament name which decides the save directory for the event, and the ip of the vex Tournament manager (Bugged in this image but it does work).
It has the ability to change those properties, or view the team score summary.

### Summary
#
The Summary view is for the judges and shows the collected information for each team from both judging scores and VexTM.

![Summary](/docs/summary.png)

AP are missing due to a VexTM issue. Other statistics are available but not displayed.

### Display
#
This menue shows all teams who have not been judged. It uses VexTM to provide a master list of all teams, and subtracts each team which has been judged by the associated form.

![Display](/docs/display.png)

Javascript is used to reload the page every 10 seconds, this updates the display. (This should be client side with a RestAPI though)

## Other Notes
#
Lastly, the web scraper runs once every 10 seconds on VexTM.

Known issues:
- If VexTM cannot be reached, the system freezes on initialization.
- Judge accounts cannot yet be created by a ui or configuration system.
- While team data should be saved and loaded it does not work and will be overwritten when VexTM pulls data.