#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    app.py create_room <room_type> <room_name>...
    app.py add_person <first_name> <second_name> <category> [<accommodation>]
    app.py print_room <room_name>
    app.py print_allocations [--o=filename]
    app.py print_unallocated [--o=filename]
    app.py exit
    app.py (-i | --interactive)
    app.py (-h | --help)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import cmd
from docopt import docopt, DocoptExit
from app.dojo import Dojo
from colorama import init
from pyfiglet import Figlet
from termcolor import cprint

init()
font = Figlet(font='slant')
introd = font.renderText('Space Allocation')
cprint(introd,"blue", attrs=['bold'])

def docopt_cmd(func):


    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Allocation(cmd.Cmd):
    intro = 'Welcome to Office space Allocation!' \
        + ' (type help for a list of commands.)'
    cprint(__doc__, "green")
    prompt = '>> '

    funt = Dojo()

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = arg['<room_type>']
        room_name = arg['<room_name>']
        print (self.funt.create_room(room_type, room_name))

    @docopt_cmd
    def do_add_person(self, arg):
        """ Usage: add_person <first_name> <second_name> <category> [<accommodation>] """
        fname = arg["<first_name>"]
        lname = arg["<second_name>"]
        category = arg["<category>"]
        accomodate = arg["<accommodation>"]
        if accomodate:
            print(self.funt.add_person(fname, lname, category, accomodate))
        else:
            print(self.funt.add_person(fname, lname, category))

    @docopt_cmd
    def do_print_room(self, arg):
        """
        Usage: print_room <room_name>
        """
        room_name = arg['<room_name>']
        print(self.funt.print_room(room_name))

    @docopt_cmd
    def do_print_allocations(self, arg):
        """
        Usage: print_allocations [--o=filename]
        """
        option = arg["--o"]
        print(self.funt.print_allocations(option))

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """
        Usage: print_unallocated [--o=filename]
        """
        option = arg["--o"]
        print(self.funt.print_unallocated(option))


    def do_exit(self, arg):
        """Usage: exit"""
        cprint ("Bye..", "yellow")
        exit()

if __name__ == '__main__':
    try:
        Allocation().cmdloop()
    except KeyboardInterrupt:
        cprint("\nApplication stopped", "yellow")
        exit()
