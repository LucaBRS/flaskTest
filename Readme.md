

# Solutions to problems:
- pip list --format=freeze > requirements.txt (this to avoid the wierd poop of "pip freeze")
- installing the database:
  - in this case you have to start python then "from app import app", and because you need to work in the context of the
    you also have to "with app.app_context():" and inside create/delete other.
- if u change the name of the database mode...well...you should track this changes int the database!! so... or delete 
    and recreate or renaming....(follow step before..)

# Problems or Todos
- structure the project in "modules": model, dao, service (or business logic), controller (or route), utils, config



