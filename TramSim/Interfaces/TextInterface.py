'''
Created on 29/06/2014

@author: Joel Pagliuca
'''
import sys

class TextInterface:
    '''
    An interface to the user through the console
    
    METHODS:
        setFunctions
        tick
        uiHelp
        uiExit
        uiExample
        hasParameters
        hasDescription
        runInterface
        
    PROPERTIES:
        FUNCTIONS - the string representation of the functions
        MAP - maps the string representation to the actual function
        DESCRIPTION - contains the descriptions of the functions for the user
        PARAMETERS - contains the parameters (list) required for the function
        WELCOME - the welcome message
        EXIT - the exit message
    '''


    def __init__(self):
        '''
        Constructor
        '''        
        self.MAP = {}
        self.FUNCTIONS = list(self.MAP.keys())
        
        self.DESCRIPTION = {}
        self.PARAMETERS = {}
        
        self.WELCOME = "##### WELCOME #####"
        self.EXIT = "##### EXITING #####"
        
        self.setFunctions()
        self.FUNCTIONS = list(self.MAP.keys())

    
    def setFunctions(self):
        '''
        OVERLOAD THIS
        this sets all the functions and their mappings, descriptions and parameters
        '''
        # uiHelp
        func = "help"
        self.MAP[func] = self.uiHelp
        self.DESCRIPTION[func] = "Display all the commands"
        # uiExample
        func = "example"
        self.MAP[func] = self.uiExample
        self.PARAMETERS[func] = ['p1', 'p2']
        # uiExit
        func = "exit"
        self.MAP[func] = self.uiExit
        
    def uiHelp(self, args=None):
        '''
        prints out all of the commands
        '''
        print("Commands:")
        for func in self.FUNCTIONS:
            funcString = " " + str(func)
            if self.hasParameters(func):
                for param in self.PARAMETERS[func]:
                    funcString += " <{0}>".format(param)
            if self.hasDescription(func):
                funcString += " - " + self.DESCRIPTION[func]
            print(funcString)
    
    def uiExit(self, args=None):
        print(self.EXIT)
        sys.exit()
    
    def uiExample(self, args):
        '''
        just an example function
        '''
        print("This is just an example")
        print("{0} and {1} were your parameters".format(str(args[0]), str(args[1])))
            
    def hasParameters(self, func):
        '''
        checks if a function has any parameters
        '''
        return func in self.PARAMETERS.keys()
    
    def hasDescription(self, func):
        '''
        checks if a function has any parameters
        '''
        return func in self.DESCRIPTION.keys()
    
    def tick(self):
        '''
        a function to run stuff that happens after every input
        e.g. an automated save or something like that
        '''
        pass
    
    def runInterface(self):
        '''
        main function of the TextInterface
        '''
        print(self.WELCOME)
        self.uiHelp()
        user_input = ""
        func = None
        
        while func != self.uiExit:
            user_input = input("\nCommand: ").split()
            if user_input and user_input[0] in self.FUNCTIONS:
                func = user_input[0]
                args = user_input[1:]
                # check for the correct parameters
                if self.hasParameters(func):
                    if len(args) < len(self.PARAMETERS[func]):
                        print("not enough arguments were given.")
                        continue
                func = self.MAP[func]
                try:
                    print()
                    func(args)
                    self.tick()
                    self.uiHelp()
                except Exception as e:
                    print("the function ran into a problem.")
                    print(e)
            else:
                print("that was an invalid command.")
        
        return

########## ##### ##########

if __name__ == '__main__':
    t1 = TextInterface()
    t1.runInterface()