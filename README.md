Evercal
===

![](img/evercal.png?raw=true)

Evernote allows you to associate "reminder" dates with your notes. Evercal is a local python web app which uses those dates to display your notes in calendar form.

This repository is still in a very rough state, and will probably stay that way. Worse is better!

Evernote setup
---
Go to your Evernote account and add a reminder date to a few notes. Also tag them with the tag "post", so that Evercal can find them. If you can also give them a short title and attach a picture, the calendar will look even better. Only one post per day!

![](img/evernote.png?raw=true)

Python Setup
---
This project requires python 2.x, it won't work with Python 3. Tested on 2.6.1.

1. Get an [Evernote developer token](http://dev.evernote.com/doc/articles/authentication.php#devtoken), which you should put in the file `sample/client/dev_token`. This token is secret, don't share it!
1. Navigate to `sample/client` and run `export PYTHONPATH=../../lib; python -m CGIHTTPServer` inside a shell.
1. Point your browser to [`localhost:8000/evercal`](http://localhost:8000/evercal) and wait a few seconds.
1. Enjoy your calendar!

FAQ
---
As I said, this repository is in a very rough state, especially the error handling. If the page stays blank instead of displaying a calendar, well, good luck. The javascript console will probably say something unhelpful like "error: parsererror". I advise examining the output of `./sample/client/cgi-bin/EDAMTest.py`.

Acknowledgment
---
The bulk of the work comes straigh from the [MooTools Events Calendar](http://dansnetwork.com/mootools/events-calendar/) and the [Evernote Python SDK](https://github.com/evernote/evernote-sdk-python). All I did was to add a bit of plumbing and adjust the style here and there.
