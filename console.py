#!/bin/python3
"""
 entry point of the command interpreter
"""
import cmd 
import uuid
from models.base_model import BaseModel
import json 
from models import storage
class HBNBCommand(cmd.Cmd):
    """
    command interpreter class
    """
    prompt = '(hbnb) '
    def my_error(self,line,numargs):
        """
        A function that displays errors to the users
        """
        classes = ['BaseModel']
        error_megs=["** class name missing **",
                    "** class doesn't exist **",
                    "** instance id missing **",
                    "** no instance found **",
                    "** attribute name missing **",
                    "** value missing **"]
        if not line:
            print(error_megs[0])
            return True
        args = line.split(" ")
        if numargs >=1 and (args[0] not in classes):
            print (error_megs[1])
            return True 
        elif numargs == 1:
            return 0
        if numargs >=2 and len(args) < 2:
            print(error_megs[2])
            return True 
        d = storage.all()

        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        if numargs >=2 and key not in d:
            print(msg[3])
            return 1
        elif numargs == 2:
            return 0 
    def do_create(self, line):
        """Creates a new instance of @cls_name class,
        and prints the new instance's ID.

        Args:
            line(args): Arguments to enter with command: <class name>
            Example: 'create User'

        """
        if(self.my_error(line,1)):
            return 
        args.line.split(" ")
        cls = eval(args[0])
        print(cls.id)
    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id
        Args:
            line(line): to enter with command <class name> <id>
            Example: 'show User 1234-1234-1234'

        """
        if (self.my_error(line,2)):
            return 
        args = line.split(" ")
        d = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        print(d[key])
    def do_destroy(self,line):
        """Deletes an instance of a certain class.

        Args:
            line(args): to enter with command: <class name> <id>
            Example: 'destroy User 1234-1234-1234'

        """
        rgs = line.split(" ")
        d = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        del(d[key])
        storage.save()
    def do_all(self, line):
        """
        Shows all instances, or instances of a certain class

        Args: 
            line(args): enter with command (optional): <class name>
            Example: 'all' OR 'all User'

        """
        
        store = storage.all()
        
        if not line:
            print([str(x) for x in store.values()])
            return
        args = line.split()
        if (self.my_error(line, 1)):
            return
        for my_key in store.values():
            if (args[0] == my_key.__class__.__name__):
                print(str(my_key))
     
      
   
        
    def do_quit(self, line):
        """
        exit the program
        """
        return True

    def do_EOF(self, line):
        """
        detect ctrl+D
        """
        return True
    
    def emptyline(self):
        """ 
        do nothing on empty lines
        """
        return False
    def do_help(self,args):
        """
        help : displays help for args
        """
        if (args):
            command_method = get_attr(self, 'do_'+args, None)
            if (command_method):
                doc_string = command_method.__doc__
                if (doc_string):
                    print(doc_string)
                else:
                    print("No help available for"+args)
            else:
                print("No available command:"+args)
    

        else:
            print("Available Commands: ")
            for command in self.get_names():
                if command.startswith('do_'):
                    print(command[3:])
if __name__ == '__main__':
    HBNBCommand().cmdloop()