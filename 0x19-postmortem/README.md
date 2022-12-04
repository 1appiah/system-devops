# Postmortem

## Issue Summary

From 4pm to 6 GMT, Holberton wordpress servers started showing a “500 Internal server error” to the end users. This caused other connected applications to also fail along with it. This issue affected all traffic as the error showed on the landing page.
Other pages were still working and were only accessed by those with some knowledge on how browsers and urls work. Such people intuitively directly queried the endpoints they needed and bypassed the landing page. The root cause of this error was a typing error that rendered some of the wordpress core files missing. Apparently, the file’s name was mistakenly misspelled.

## Timeline(all times in UTC)

- 5:30pm – Configuration push begins
- 5:36pm – server failure and monitoring systems alert
- 5:36pm – necessary teams were alerted
- 5:40pm – debugging wordpress backend begins
- 5:50pm – root cause found and correction begins
- 5:55pm – error was corrected successfully
- 5:55pm – server restart restart begins
- 6:00pm – servers fully back online

## Root Cause and Resolution
The root cause of the issue was an incorrect name of one of the core wordpress backend files. Apparently an earlier work in the directory mistakenly resulted in an incorrectly spelled /var/www/html/wp-includes/class-wp-locale.php which was supposed to be /var/www/html/wp-includes/class-wp-locale.phpp. 
Using strace, the server was queried for the landing page’s endpoint, and strace attached to the apache process, logged the series of events happening to render the page.  
One of the logs contained the line “require-once(/var/www/html/wp-includes/class-wp-locale.phpp) – no such file or directory” indicating either that the file is missing or its name is changed. We looked through the /var/www/html/wp-includes/ directory for the same filename or a similar one. A similar one “class-wp-locale.php” was found and the name changed to “class-wp-locale.phpp”. The process was then automated with puppet and server restarted.

## Corrective and Preventative measures
Add monitoring on server files change
Restrict configuration files editing to experienced professionals
Develop faster mechanism for delivering status notifications during incidents
