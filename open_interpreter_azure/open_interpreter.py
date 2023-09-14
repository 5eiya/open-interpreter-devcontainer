import os   
from dotenv import load_dotenv
import interpreter                                                                                                                
                                                                                                                                                 
# .envファイルのパスを指定して読み込む                                                                                                        
load_dotenv('.env')                                                                                                                                  
                                                                                                                                                 
os.environ['AZURE_API_KEY'] = os.getenv('AZURE_API_KEY')                                                                                             
os.environ['AZURE_API_BASE'] = os.getenv('AZURE_API_BASE')                                                                                             
os.environ['AZURE_API_VERSION'] = os.getenv('AZURE_API_VERSION')                                                                                        
os.environ['AZURE_DEPLOYMENT_NAME'] = os.getenv('AZURE_DEPLOYMENT_NAME')

interpreter.use_azure = True
interpreter.azure_api_type = "azure"

interpreter.chat()