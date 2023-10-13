#!/usr/bin/python3
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    This class contains the entry point for the command line interpreter
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Exits the command line interpreter"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Executes when an emptyline + ENTER is an input"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
