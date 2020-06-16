# Daily Sudoku

## Features:
* Gets latest sudoku everyday at local 9:25AM from [daily sudoku](http://www.dailysudoku.com/sudoku/) in PDF format.
* Sends an email with the attached sudoku to an email address specified.

## Environment Options
* `PRINT_EMAIL` -- (**required**) An email to send the PDF to. This can a HP ePrint email which could automate printing the puzzle.
* `SMTP_SERVER` -- (**required**) The name of the SMTP server. You can use Google or Outlook's server as TLS is enabled.
* `SMTP_USER` -- (**required**) The name of the user for logging into the SMTP server. For Outlook and Google, this is your email address.
* `SMTP-PWD` -- (**required**) The password used for logging in. For Google's Gmail, you may need to set up an App password to avoid 2FA.

The script runs pending jobs every 5 hours.

This package was meant to be dockerised and run from a server. 
If the email is not sent, you can check the logs -- `docker logs <container_name>`. 
 
The email address was also meant to be a [HP ePrint email](https://en.wikipedia.org/wiki/HP_ePrint), 
so in effect it was supposed to print a sudoku puzzle everyday.

If running in [docker](https://hub.docker.com/r/houfu/daily_sudoku), you should set the above enivronment options for the script to work. 

Read more about the story of this project on [my blog post](https://www.lovelawrobots.com/get-your-daily-dose-of-sudoku-with-a-little-bit-of-python/). 