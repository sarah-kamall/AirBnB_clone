#!/bin/python3
"""
 entry point of the command interpreter
"""
import cmd 
 
class HBNBCommand(cmd.Cmd):
    """
    command interpreter class
    """
    prompt = '(hbnb) '
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