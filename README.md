# pyfire
A basic python wrapper for the Firebase REST API

#### Background

Firebase (v.3) has the following available SDKs:

* Android
* iOS
* Web (javascript)
* C++ (beta)
* [Server Side](https://firebase.google.com/docs/server/setup)
  * Java
  * Node.js

#### Issue

There is no SDK to use with the Google App Engine/Python stack. - This means using the Firebase REST API.

While Python already has some 3rd party wrappers for the Firebase REST API, they ( [1](https://github.com/ozgur/python-firebase), [2](https://github.com/mikexstudios/python-firebase) ) all seem to use the [python `requests` library.](https://pypi.python.org/pypi/requests/) and while [installing extra python libraries is possible on App Engine](https://cloud.google.com/appengine/docs/python/tools/using-libraries-python-27#installing_a_library) the `requests` library doesn't (and will not) support running on App Engine as GAE doesn't use the same standard library as core Python does. (See links below).

[Requests Python Library Issues On App Engine -  Stack Overflow](http://stackoverflow.com/questions/9762685/using-the-requests-python-library-in-google-app-engine)

[GitHub Issue for the requests library. - Stating GAE support will NOT be added](https://github.com/kennethreitz/requests/issues/1905)

#### The App Engine restrictions

App Engine uses the [urlfetch](https://pypi.python.org/pypi/urlfetch) library for outbound requests ([Read more about their outbound requests here](https://cloud.google.com/appengine/docs/python/outbound-requests)), so that is this project will aim to use

#### Other useful links:

[Generating Firebase JWT with python](https://github.com/firebase/firebase-token-generator-python)

[Firebase REST API reference](https://firebase.google.com/docs/reference/rest/database/)
