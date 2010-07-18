Polish, utilities for Sparkle
=============================

'Polish your software so it will [Sparkle][0] even brighter!'

About
-----
Polish is a set of tools meant to complement [Sparkle][0], by making appcasts
and release notes simpler to create and maintain.

It also adds support for something I call 'cumulative release notes', which
basically means that a user upgrading from 0.1 to 0.4 will not just see the
changes in 0.4 (current Sparkle behavior), but also changes in any intermediate
updates, like 0.2 and 0.3.

Eventually I intend to add support for capturing system profile information (or
extract it from web server logs) and slightly unrelated - tools to create and
submit usage statistics from your Cocoa app.

Quickstart
----------
* Copy config.dist.py to config.py, and edit it. Read [Configuration Options][1]
  for a more in-depth description of these options.
* Create release information for your tool in releases/. Copy example.yaml to
  <version number>.yaml, e.g. 0.1.yaml, edit and save. Filename is important!
    * You will probably want to read Sparkle's page about [publishing
      updates][2] on instructions on how to sign your release and get the
      signature, which you need for your release YAML.
    * You can use `LC_TIME=en_US date +\"%a, %d %b %G %T %z\"` to generate the
      date for the 'date' field.
* Generate appcast and release notes, using `./generate appcast > appcast.xml` and
 `./generate releasenotes > releasenotes.html`.
* Copy appcast.xml, releasenotes.html, html/polish.js and html/polish.css to
  your webserver. Put the zip of your app into a subdir called 'updates' unless
  you changed 'release\_dir' and 'release\_url'.

[0]: http://sparkle.andymatuschak.org/
[1]: http://wiki.github.com/jorgenpt/Polish/configuration-options
[2]: http://wiki.github.com/andymatuschak/Sparkle/publishing-an-update
