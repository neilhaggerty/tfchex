import os                                                                        
import sys                                                                       
import hcl                                                                       
                                                                                 
                                                                                 
def find_unused_vars(tfdir):                                                     
    all_vars = {}                                                                
    for root, dirs, files in os.walk(tfdir):                                     
        if not any(_file.endswith('.tf') for _file in files):                    
            continue                                                             
        for _file in os.listdir(root):                                           
            if _file.endswith('.tf'):                                            
                tf_vars = set()                                                  
                with open(os.path.join(root, _file)) as terraform:               
                    _tf = hcl.load(terraform)                                    
                    try:                                                         
                        tf_vars.update(_tf["variable"].keys())                   
                    except KeyError:                                             
                        tf_vars.update([])                                       
                for var in tf_vars:                                              
                    all_vars[var] = f"{root}/{_file}"                            
                                                                                 
        for _file in os.listdir(root):                                           
            if _file.endswith('.tf'):                                            
                _tf = open(os.path.join(root, _file)).read()                     
                for _var in list(all_vars):                                      
                    if f"var.{_var}" in _tf:                                     
                        del all_vars[_var]                                       
        for _var, _path in all_vars.items():                                     
            print(f'var.{_var} in {_path}')                                      
                                                                                 
                                                                                 
if __name__ == "__main__":                                                       
    find_unused_vars(sys.argv[1]) 
