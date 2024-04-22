#!/usr/bin/python3

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.gym import Gym
from models.user import User
from models.review import Review
from models import storage
import models
import cmd
import shlex

classes = {"BaseModel": BaseModel, "User": User, "Gym": Gym,
           "City": City, "Amenity": Amenity, "Review": Review}

input_msg = {
    "User": {
        "first_name": "    -> [first_name] = ",
        "last_name": "    -> [last_name]  = ",
        "email": "    -> [email]      = ",
        "password": "    -> [password]   = ",
        },
    "Gym" : {
        "name": "    -> [name]           = ",
        "city_id": "    -> [city_id]        = ",
        "user_id": "    -> [user_id]        = ",
        "location": "    -> [location]       = ",
        "description": "    -> [description]    = ",
        "price_by_month": "    -> [price_by_month] = ",
        "price_by_year": "    -> [price_by_year]  = ",
        "amenities": "    -> [amenities]      = "
        },
    "City": {
        "name": "    -> [name] = "
        },
    "Amenity": {
        "name": "    -> [name] = "
        },
    "Review": {
        "gym_id":  "    -> [gym_id]  = ",
        "user_id": "    -> [user_id] = ",
        "text":    "    -> [text]    = "
        }
}

class HBNBCommand(cmd.Cmd):
    prompt = "gym -> "

    class_missing = "** class name missing **"
    class_nexist = "** class doesn't exist **"
    id_missing = "** instance id missing **"
    inst_missing = "** no instance found **"
    attr_name_missing = "** attribute name missing **"
    attr_value_missing = "** value missing **"

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_all(self, line):
        class_name = None
        if line:
            class_name = classes[shlex.split(line)[0]]
        all_inst = models.storage.all(class_name)
        for inst in all_inst.values():
            print(inst)

    def do_update(self, line):
        ignore = ['id', 'email', 'created_at', 'updated_at']
        args = shlex.split(line)
        if not self.class_check(args):
            return
        
        if len(args) < 2:
            print(self.id_missing)
            return

        inst = models.storage.get(classes[args[0]], args[1])
        if not inst:
            print(self.inst_missing)
            return
        print("    -> enter in key=value format")
        while True:
            tmp = input("    -> ")
            if not tmp:
                break
            items = tmp.split("=")
            if len(items) != 2:
                print("!!! format should be key=value !!!")
                continue
            key = items[0].stript()
            value = items[1].stript()
            if not key or not value:
                print("!!! format should be key=value !!!")
                continue

            if key not in ignore:
                setattr(inst, key, value)

    
    def do_create(self, line):
        """create <classname>
        Create a new instance from the <classname>"""
        new_dict = {}
        args = shlex.split(line)
        if not self.class_check(args):
            return
        
        class_input = input_msg[args[0]]
        try:
            for key, value in class_input.items():
                new_dict[key] = input(value)
        except KeyboardInterrupt:
            print(f"\n{args[0]} creation aborted.\n")
            return

        if args[0] == "Gym":
            amenity_object_list = []
            all_amenities = models.storage.all(Amenity)
            for am_id in new_dict.pop("amenities").split(", "):
                amenity = all_amenities.get(f"Amenity.{am_id}", None)
                if not amenity:
                    print("\nmissing amenity id: [" + am_id + "]\n") 
                    return
                amenity_object_list.append(amenity)
                new_dict["amenities"] = amenity_object_list

        new_obj = classes[args[0]](**new_dict)
        new_obj.save()
        print(new_obj.id)
        print()

    def do_get(self, line):
        args = shlex.split(line)
        if not self.class_check(args):
            return

        if len(args) < 2:
            print(self.id_missing)
            return

        inst = models.storage.get(classes[args[0]], args[1])
        if not inst:
            print(self.inst_missing)
            return
        
        print(inst)

    def do_destroy(self, line):
        args = shlex.split(line)
        if not self.class_check(args):
            return
        
        if len(args) < 2:
            print(self.id_missing)
        
        inst = models.storage.get(classes[args[0]], args[1])
        if not inst:
            print(self.inst_missing)
            return
        
        models.storage.delete(inst)
        models.storage.save()

    def class_check(self, args):
        """checks the <classname> and handles it's errors
        """
        if len(args) == 0 or not args[0]:
            print(self.class_missing)
            return False

        class_name = args[0]
        if class_name not in classes.keys():
            print(self.class_nexist)
            return False

        return True

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()