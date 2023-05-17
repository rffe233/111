import unittest
from unittest.mock import patch
from app import app, db
from models.films import FilmInfo
from flask import url_for
import ast
import os


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def test_database_connection(self):
        # Ensure that the app configuration is set up correctly
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'])

        # Check if the connection was successful
        with app.app_context():
            self.assertTrue(len(db.session.query(FilmInfo).all()) == 16428)

    def test_count_by_year(self):
        with app.test_request_context():
            with app.app_context():
                response = self.app.get(url_for('routes.films.count_by_year'))
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json['1964'], 117)
                self.assertEqual(response.json['2012'], 475)
                self.assertEqual(response.json['2018'], 1144)

    def test_avg_rate_by_region(self):
        with app.test_request_context():
            with app.app_context():
                response = self.app.get(url_for('routes.films.avg_rate_by_region'))
                # data = response.json
                #
                # # 打印整个 JSON 数据
                # print(data)
                #
                # # 检查 'cn' 键是否存在
                # if 'cn' in data:
                #     cn_data = data['cn']
                #     # 检查 '1923' 键是否存在
                #     if '1923' in cn_data:
                #         rate_1923 = cn_data['1923']
                #         print(rate_1923)
                #     else:
                #         print("Key '1923' does not exist in 'cn' data.")
                # else:
                #      print("Key 'cn' does not exist in the response data.")  #调试
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json['cn']['1923'], 8.3)
                self.assertEqual(response.json['cn']['1966'], 7.2)
                self.assertEqual(response.json['cn']['2018'], 5.148128342245989)
                self.assertEqual(response.json['hk']['1938'], 6.8)
                self.assertEqual(response.json['hk']['1961'], 6.6625)  # 6.662499999999999
                self.assertEqual(response.json['hk']['1998'], 6.3984375)  # 6.398437499999999
                self.assertEqual(response.json['tw']['1966'], 7.4)
                self.assertEqual(response.json['tw']['2010'], 6.203125000000003)  # 6.203125000000001
                self.assertEqual(response.json['tw']['2018'], 6.475)  # 误差过小，怀疑系统误差

    def test_file_and_function(self):
        # Define the file and function names to check
        file_name_models = 'models' + os.path.sep + 'films.py'
        function_name_cby = 'count_by_year'
        function_name_arbr = 'avg_rate_by_region'
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        file_path = os.path.join(parent_directory, file_name_models)  # 拼接文件路径
        # Check if the file exists in the project directory
        self.assertTrue(os.path.exists(file_path))
        # Load the module and check if the function exists
        self.assertTrue(hasattr(FilmInfo, function_name_cby), "count_by_year method not found in FilmInfo class")
        self.assertTrue(hasattr(FilmInfo, function_name_arbr), "avg_rate_by_region method not found in FilmInfo class")


if __name__ == '__main__':
    unittest.main()
