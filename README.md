# Beep Boop Bot

## Commands List

### Help / Docs
Commands for help and documentation

##### .docs
Sends an embed linking to this page
<pre>Usage: .docs</pre>

##### .help
Displays the default help message, showing all the commands
The official documentation (this page) is recommended, however, as it's a lot more helpful
<pre>Usage: .help</pre>

### Admin
Commands for administrators, mods, etc.

##### .ban
Bans a user from a server. Requires the 'Ban members' permission
<pre>Usage: .ban [discord user to ban] [reason (optional)]</pre>

##### .kick
Kicks a user from a server. Requires the 'Kick members' permission
<pre>Usage: .kick [discord user to kick] [reason (optional)]</pre>

##### .restrict
Assigns a role called 'Restrict' to a user. This role must exist on the server already - you can configure the restrictions however you'd like. Requires 'Manage roles' permission
<pre>Usage: .restrict [discord user to restrict] [duration in seconds]</pre>

### Greetings
Greeting related commands

##### .hello
Replies with hello to the user of the command. Replies with hello again if used twice in a row
<pre>Usage: .hello -> Beep Boop Bot: "Hello [user]!"</pre>
Alternatively, if you use it twice in a row:
<pre>-> Beep Boop Bot: "Hello again, [user]"</pre>

The greetings category also contains an event listener that mentions a user with a welcome message when they join a server. Currently, the welcome message is not customisable. However, this feature will be added

### Miscellaneous
Misc. commands for doing dumb stuff

##### .russianroulette
Has a 1 in 6 chance of kicking the user
<pre>Usage: .russianroulette -> (NO KICK) Beep Boop Bot: "You were lucky... This time ;)"</pre>
If the user was unlucky and got kicked:
<pre>-> (KICK) Beep Boop Bot: "Oops... You lost"</pre>

#### .beep
Beep Boop Bot replies with "boop"
<pre>Usage: .beep</pre>
