from flask import Blueprint, jsonify, request
from models.films import FilmInfo
import logging  # 使用日志记录相关信息

logging.basicConfig(filename='films_api.log', level=logging.DEBUG)
films_bp = Blueprint('films', __name__)


@films_bp.route('/', methods=['GET'])
def get_films():
    # 返回所有的电影信息
    try:  # 在所有的路由中，都要进行错误处理
        films = FilmInfo.query.all()
        results = [films.to_dict() for film in films]
        logging.info('All films were successfully retrieved from the database.')  # 用logging模块记录日志
        return jsonify(results)
    except Exception as e:
        logging.error('Error occurred while retrieving films from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


@films_bp.route('/count_by_year', methods=['GET'])
def count_by_year():
    try:
        result = FilmInfo.count_by_year()  # 直接调用FilmInfo类中构建的静态方法count_by_year()
        logging.info('获得各年份电影数量序列')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


@films_bp.route('/avg_rate_by_region', methods=['GET'])
def avg_rate_by_region():
    try:
        result = FilmInfo.avg_rate_by_region()  # 直接调用FilmInfo类中构建的静态方法count_by_region()
        logging.info('获得地区电影均分')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})
