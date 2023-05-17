import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = {
    'ENGINE': 'mysql+pymysql',
    'URI': 'root:0000@localhost:3306/moviedata',  # 根据实际情况修改
    'ECHO': False}
