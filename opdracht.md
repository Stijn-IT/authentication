# Exercise: Authentication

wincpy start 8fd255f5fe5e40dcb1995184eaa26116

IMG plakken: Ctrl+Alt+V

For this exercise, you will need to read Flask's documentation:

[Flask -- Quickstart](https://flask.palletsprojects.com/en/2.0.x/quickstart/)

It also helps to watch this video:

[link video](https://youtu.be/8ZtInClXe1Q)

## About Auth (Abauth..?)

Whenever you are logging in to a service -- like Twitter or GitHub --, what is happening behind the scenes is a more complex version of the following: 

1. You enter your email/password combination.
2. The combination is sent to the service.
3. The email address looked up in a database
   - If the email address is not found, the user cannot be logged in and error is shown. This is the end of the road.
   - If the email address is found, the matching hash of the password is also retrieved along with it.
4. The password you entered is hashed and this hash is compared to the hash of the password that was retrieved from the database.
   - If the passwords don't match, an error is shown.
   - If the passwords do match, the path proceeds to log the user in.
5. The user is provided with a cryptographically signed cookie that is sent to the server with every request from then on, informing the server 'Hey, this is authenticated user example@example.com' so that responses may be customized to that user.

## Step 1: Log In

Implement the specification of /login according to this table.

![](2023-03-21-20-24-01.png)

## Tip

use **redirect(url_for('login', error=True))** to redirect back to the login page with an extra **error** parameter. Your only job, then, is to check for this query parameter on a **GET** request to **/login** and modify the page accordingly.

## helpers

To help you along, we implemented two functions in helpers.py: 

1. hash_password: this takes a string (str) and returns the hashed version of that string.
2. get_users: takes no arguments and returns a dictionary where the keys are all the known usernames and the matching values are hashed versions of their password. We have two users in our database:
   - Alice with password secret
   - Bob with password supersecret

## IMPORTANT

Do not simply compare the user-entered password with a string **'secret'** or **'supersecret'**. Use the hashed passwords! Watch the video above to learn why.

## Step 2: Log out

Implement the functionality that whenever there is a **GET** or **POST** request to the path **/logout**, the user is logged out. This means that if present, the **'username'** entry in their **session** dictionary is removed.

After being logged out, the user should be redirected to /.

## Step 3: Dashboard

At the path **/dashboard** (responding to **GET** requests), create a dashboard that displays different content depending on which user visits it. Keep it simple! The exercise is about authentication, so the main objective here is to make it so that each user sees something different.

- Be sure to at least display a customized greeting on this (fictional) user dashboard.
- Consider adding some extra customized content by using Jinja's {% if %} -{% else %} blocks. [More on that here](https://jinja.palletsprojects.com/en/2.11.x/templates/#if)

## Building on

You now have the basic tools to create limitless creative, interactive applications on the web!

We would expand on this approach in the real world to provide customized experiences to users that are logged in. Social networks like Twitter and Instagram look up who a user follows and shows those people's tweets in a timeline. They also enable logged-in users to contribute their own content.

This is an important milestone! You should be proud of yourself for understanding all of this material and getting this far.

