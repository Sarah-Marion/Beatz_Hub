from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User

# app = create_app('test')
app = create_app('development')
# app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server(port=4200))

migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db=db, User = User)

@manager.command
def test():
    '''
    Runs the unittest
    '''
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__=='__main__':
    manager.run()