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
There are a few simple steps needed to get started with Polish. I've tried
designing Polish to be as close to zero-setup as possible, but there is some
action required.

(If you have thoughts on how to make this easier for first-time users, 
[contact me][3]!)

1. Copy config.dist.py to config.py, and edit it. Read 
   [Configuration Options][1] for a more in-depth description of these options.
2. Create release information for your tool in releases/. Copy example.yaml to
   $VersionNumber.yaml, e.g. 0.1.yaml, edit and save. Filename is important!
    * You will probably want to read Sparkle's page about [publishing
      updates][2] on instructions on how to sign your release and get the
      signature, which you need for your release YAML.
    * You can use `LC_TIME=en_US date +\"%a, %d %b %G %T %z\"` to generate the
      date for the 'date' field.
    * Version numbers must be an unbounded number of integers separated by
      periods. [Apple recommends][7] using at most 3 components (x.y.z).
3. Generate appcast and release notes, using `./generate appcast > appcast.xml`
   and `./generate releasenotes > releasenotes.html`.
4. Copy appcast.xml, releasenotes.html, html/polish.js and html/polish.css to
   your webserver. Put the zip of your app into a subdir called 'updates' unless
   you changed 'release\_dir' and 'release\_url', and name it *MyExampleApp
   0.1.zip* - the filename must be in this format, where *MyExampleApp* is
   whatever you set `app_name` to in config.py, and 0.1 is the name of the
   release description file minus the extension.

That's it! Point your Sparkle setup to this new appcast, and you should be good
to go. See [Sparkle Setup][4] for more information on how to set your app up
with Sparkle and set the appcast URL.

For a more complete description of initial setup, see [Initial Setup][8]. For a
more complete description of the steps to add a new release, see 
[Publishing An Update][9].

Further customization
---------------------
If you want to customize it more, you can change the files in template/ for
the HTML and XML layout of the release notes and the appcast, respectively. See
[Templates][5] for more information about these.

For setups that aren't compatible with the default config, see 
[Configuration Options][1] for a complete documentation of the available
configuration options and their values.

When a release for some reason doesn't fit the standard bill in some way, there
are some overrides you can put in a release info file to customize it farther.
You can see [Release Description][6] for an overview of these.

[0]: http://sparkle.andymatuschak.org/
[1]: http://wiki.github.com/jorgenpt/Polish/configuration-options
[2]: http://wiki.github.com/andymatuschak/Sparkle/publishing-an-update
[3]: http://github.com/jorgenpt
[4]: http://wiki.github.com/andymatuschak/Sparkle/
[5]: http://wiki.github.com/jorgenpt/Polish/templates
[6]: http://wiki.github.com/jorgenpt/Polish/release-description
[7]: http://developer.apple.com/mac/library/technotes/tn/tn1132.html
[8]: http://wiki.github.com/jorgenpt/Polish/initial-setup
[9]: http://wiki.github.com/jorgenpt/Polish/publishing-an-update
