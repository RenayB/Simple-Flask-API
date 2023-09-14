# Simple Flask Program

## What is Flask ?
 A web application framework that allows developers to write applications without having to worry about 
 low level details

## Purpose of Project 
The purpose of this project is to display some the basic fundemtnetals and use of the Flask framework

### Application 
- A Flask application is created by intializing the the Flask class as an object ( line 3) and ran by calling the `run()` method on line 32
- Side note. By  passing `debug=true` to the run method , this allows the developer to make changes to the application while its running and not have to worry about re-running the code after the change  

### Routes 
- The `route()` function of the Flask library tells the application which URL which function is binded to it. 
- In our example the default route `"/"` is binded to the function `def home()`

### Flask and HTTP Protocols 
 - Flask allows the user to use HTTP protocols for its data communication 

 - `GET` : A method that sends data from server to the user. In our example the path parameter `@app.route("/get-user/<user_id>")` and the function `get_user` returns user data based on a provided id in the path url.

 - `POST` : A method used to send data to the server . In our post example , we accept from the user data to store ( if a database was present ) and return the data 

