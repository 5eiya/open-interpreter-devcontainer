import os   
from dotenv import load_dotenv
import interpreter                                                                                                                
                                                                                                                                                 
# .envファイルのパスを指定して読み込む                                                                                                        
load_dotenv('.env')

interpreter.api_key = os.getenv('OPEN_API_KEY_GPT4')
interpreter.chat()