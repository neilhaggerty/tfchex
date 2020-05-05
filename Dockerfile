FROM python:latest                                                              
                                                                                                                                               
WORKDIR /code                                                                                                                                                                                                                                                                 
COPY chex.py .                                                                                                                                 
RUN pip install pyhcl                                                           
CMD python main.py 
