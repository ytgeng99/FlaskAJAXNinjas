AJAX Ninja
You'll be rewriting your Disappearing Ninja assignment to include AJAX. The below steps will help you get started. Next, follow the wireframe below to build a version of Disappearing Ninja with AJAX. Remember, with AJAX, you will only need one view and your page should never be reloaded.

1. Create a new Flask project. Build it with one get route to serve up your index.html. Test to make sure you can run that server and load the html page before continuing.

2. Create a static directory with your JavaScript file inside of it. Now link your JS file to your index.html file. Test it by asking for an alert box on page load. Don't forget to link to the jQuery CDN, too. You'll be using it for AJAX just like before.

3. You'll need some event listeners in order to trigger a request to the server when a user clicks one of the color buttons.

4. When an event occurs (button click), you'll want to send a request to the server. The server should collect information about which Ninja you'd like to display, along with the correct message, and send a JSON response to the client.


Hacker: Add the option for a user to enter a custom color. If they enter a color that's not one of the Ninja Turtles' colors display a picture of April.

