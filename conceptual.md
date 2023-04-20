### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
   javascript can be used on the clientside in the browser for frontend
   
   devleopement, Python can't

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

use get() and add a default value in the call
use setdefault() and set a default value for a key if it's not in the dict
check your key against  keys() before you query the dict


- What is a unit test?
test a single function

- What is an integration test?
test multiple function and their interaction

- What is the role of web application framework, like Flask?
to make it quicker and easier to deplay application by abstracting away
lower level details


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  query string arguments are best used when the purpose of the form is to query the system
  post paramaters are better when changing the state of the system.

- How do you collect data from a URL placeholder parameter using Flask?
  you use the request library

request.form['name_of_input']

- How do you collect data from the query string using Flask?
	request.args('name_of_arg)

- How do you collect data from the body of the request using Flask?
can use
request.form.get('name of input')
request.get_json()
	

- What is a cookie and what kinds of things are they commonly used for?

cookie is way for a server to store data on the client
can be used to keep track of state for a user. 

- What is the session object in Flask?
session is an abstration over cookies.
it allows the programmer to concat all data they want to store
in a encrypted string that is stored on the client side.

- What does Flask's `jsonify()` do?
it converts data into proper json format with content/type header set to json
