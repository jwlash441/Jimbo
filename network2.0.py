##Created by: James Walsh
##This code will help clear out disk space

import os


#paths to delete
paths = [r"C:\Users\jwals\test test", r"C:\Users\jwals\test1", r"C:\Users\jwals\test2"]

for path in paths:
    
    #will check if the path is a dir or not
    if os.path.exists(path):
    
    #iterating through subfolders
        for root_folder, folders, files in os.walk(path):
        
        #checking for files
            for file in files:
            
            #file path - will delete all files in target folders 
                file_path = os.path.join(root_folder, file)
            
            #delete the files in that path
                if not os.remove(file_path):
                   #will print if successful
                       print(f"{file_path} deleted successfully")
                   #unsuccessful message (if this prints something went wrong)
                else:
                       print(f"Unable to delete the {file_path}")
                
                
                
                

                   
       
                
                    
                    
                
                
            
