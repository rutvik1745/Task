import sys

#Check the type of sys.argv
# print(type(sys.argv))
# #print the command line arguments

# print('The command line argument are : ')

# #Iterate over sys.argv and print each argument

# for i in sys.argv:
#     print(i)

# import getopt
# argv = sys.argv[1:]
# try:
#     opts,args = getopt.getopt(argv,'hm:d',['help','my_file='])
#     print(opts)
#     print(args)
# except getopt.GetoptError:
#     print('somethng went wrong!')
#     sys.exit(2)


# import argparse    
# #create an ArgumentPaser Object
# parser = argparse.ArgumentParser(description = 'Example script using argparse')  

# #Add arguments
# parser.add_argument('-f','--file',help='Specify a file name')
# parser.add_argument('-v', '--verbose', action = 'store_true', help = 'Enable verbose mode')

# #Parse the command line arguments
# args = parser.parse_args()

# #Access the agument values
# if args.file:
#     print(f"File name:{args.file}")
# if args.verbose:
#     print("Verbose mode is enabled")


# from docopt import docopt  
  
# __doc__  =  """Usage: 
#     my_program.py [--option1] [--option2=<value>] <argument> 
 
# Options: 
#     -h, --help         Show this help message. 
#     -o, --option1      Enable option 1. 
#     -t, --option2 = <value>  Specify option 2 value. 
# """  
  
# if __name__ == '__main__':  
#     arguments = docopt(__doc__, version = 'Example 1')  
#     print(arguments)  


import fire    
class Python(object):    
    def hello(self):    
    print("Hello")    
       def openfile(self, filename):    
        print(" Open file  '" + filename + "'")    
    
if __name__ == '__main__':    
    fire.Fire(Python)   