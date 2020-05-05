#!/bin/bash                                                                                                                                    
                                                                                                                                               
image_name=tfchex                                                               
terraform_loc=$(pwd)                                                            
                                                                                                                                               
docker build -t $image_name "$HOME/dev/tfchex/"                                
docker run \                                                                                                                                   
    --rm \                                                                                                                                     
    --name $image_name \                                                        
    -v "$(pwd)":/"$terraform_loc" \                                             
    -it $image_name \                                                           
    python chex.py "$terraform_loc"
