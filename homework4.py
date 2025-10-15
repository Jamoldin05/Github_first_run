from dataclasses import dataclass


@dataclass
class MyManager:
    def __init__(self): # 1
        print('Init method called')
    
    def __enter__(self):
        print('Enter method called') # 2
    
    def __exit__(self,exc_type, exc_value, tb):
        print('Exit method called') # 4
        