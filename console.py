#!/usr/bin/python3
"""
This module is the command line interpreter for the clone project
"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class contains the entry point for the command line interpreter
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
               "Review": Review, "Place": Place, "State": State, "City": City}

    def precmd(self, line):
        """Reformat the command line text
        Ex:<class>.cmd(id)
        Becomes: cmd class id
        """
        if line.endswith(")"):
            line = line.split(".")
            class_name = line[0]
            cmd_params = line[1].split("(")
            cmd = cmd_params[0]
            all_params = cmd_params[1].strip(")")
            sep_params = all_params.split(",")

            # ---This is to evaluate the id value when inputed as str ---
            if sep_params[0] != "":
                params = eval(sep_params[0])
            else:
                params = ""
            for param in sep_params[1:]:
                params = params + param + " "

            new_line = cmd + " " + class_name + " " + params
            return new_line

        return line

    def do_EOF(self, line):
        """Exits the command line interpreter
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Executes when an emptyline + ENTER is an input
        """
        pass

    # ---Commands for the Console ---
    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it to JSON file and
        prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            inst = self.classes[line]()
            inst.save()
            print(inst.id)

    def do_show(self, line):
        """Prints the string rep of an instance based on the class
        """
        line = line.split()
        if not line:
            print("** class name missing **")
            return

        if line[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(line) == 1:
            print("** instance id missing **")
            return

        store_dict = storage.all()
        dict_key = "{}.{}".format(line[0], line[1])

        if dict_key not in store_dict:
            print("** no instance found **")
            return

        print(store_dict[dict_key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id, then save
        the change into the JSON file
        """
        line = line.split()
        if not line:
            print("** class name missing **")
            return

        if line[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(line) == 1:
            print("** instance id missing **")
            return

        store_dict = storage.all()
        dict_key = "{}.{}".format(line[0], line[1])
        if dict_key not in store_dict:
            print("** no instance found **")
            return

        storage.all().pop(dict_key)
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not
        on the class name
        """
        line = line.split()
        if not line:
            for value in storage.all().values():
                print(value)
            return

        if line[0] not in self.classes:
            print("** class doesn't exist **")
            return

        for key, value in storage.all().items():
            if key.split(".")[0] == line[0]:
                print(value)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute, saving the change into the JSON file
        """
        line = line.split()
        if not line:
            print("** class name missing **")
            return

        if line[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(line) == 1:
            print("** instance id missing **")
            return

        store_dict = storage.all()
        dict_key = "{}.{}".format(line[0], line[1])
        if dict_key not in store_dict:
            print("** no instance found **")
            return

        if len(line) == 2:
            print("** attribute name missing **")

        elif len(line) == 3:
            print("** value missing **")

        elif len(line) == 4:
            object_to_update = store_dict[dict_key]
            setattr(object_to_update, line[2], eval(line[3]))
            storage.all()[dict_key] = object_to_update
            storage.save()

    def do_count(self, line):
        """Retrieves the number of instances of a class
        """
        line = line.split()
        count = 0
        if line[0] not in self.classes:
            print("** class doesn't exist **")
            return

        for key in storage.all().keys():
            key = key.split(".")[0]
            if key == line[0]:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
