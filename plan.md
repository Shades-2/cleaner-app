# Registration page
write bullet points with an arrow so its a flwo of how to user will use the application and we start with clearners user jouinryey 
1 reg with app, 
2 login details ( 3rd party login)
3 when they login they will have a screen where they can see aplicaitons for teir services
4 some way of those 2 interacting 
5 thats it for now

docker
venv get flask and sqlalchemy
with venv folder have a folder claled src 
tests folder

get mysql db
use flask sqlalchemy 
2 sqlalchemy classes one called user() inherits from sqlalchemy.odel() secdon class cleaner_details()
put the clasess into models.py file

get tables set up with details for cleaners/ end users
test will post a cleaners details to database and checks its correct

get flask set up first method register_clkeaner takes reg details as a json object as its argument method = post request object in request.params or request. args
for first draft write details to table 
write an api test will post some json 
lookup flask testing framework

make a factory application
make a route 
use testing framework
check it returns 200 in the test
