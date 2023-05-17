from sqlalchemy import func
from app import db


class FilmInfo(db.Model):
    __tablename__ = 'movie_data'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(64))
    director = db.Column(db.String(64))
    language = db.Column(db.String(64))
    rate = db.Column(db.Float)
    rating_num = db.Column(db.Float)
    region = db.Column(db.String(64))
    runtime = db.Column(db.Integer)
    title = db.Column(db.String(64))
    type = db.Column(db.String(64))
    year = db.Column(db.Integer)
    is_cn = db.Column(db.Integer)
    is_hk = db.Column(db.Integer)
    is_tw = db.Column(db.Integer)

    def to_dict(self):

        return {
            'id': self.id,
            'date': self.date,
            'director': self.director,
            'language': self.language,
            'rate': self.rate,
            'rating_num': self.rating_num,
            'region': self.region,
            'runtime': self.runtime,
            'title': self.title,
            'type': self.type,
            'year': self.year,
        }

    @staticmethod
    def count_by_year():
        aresult = db.session.query(FilmInfo.year, func.count()).group_by(FilmInfo.year).all()
        count_by_year_dict = {year: count for year, count in aresult}
        result = count_by_year_dict
        return result

    @staticmethod
    def avg_rate_by_region():
        result = {'cn': {}, 'hk': {}, 'tw': {}}

        # 查询每个地区的年份和平均得分
        cn_data = db.session.query(FilmInfo.year, db.func.avg(FilmInfo.rate)).filter(
            FilmInfo.is_cn == 1).group_by(
            FilmInfo.year).all()
        hk_data = db.session.query(FilmInfo.year, db.func.avg(FilmInfo.rate)).filter(
            FilmInfo.is_hk == 1).group_by(
            FilmInfo.year).all()
        tw_data = db.session.query(FilmInfo.year, db.func.avg(FilmInfo.rate)).filter(
            FilmInfo.is_tw == 1).group_by(
            FilmInfo.year).all()

        # 将查询结果存入结果字典
        for year, avg_rate in cn_data:
            result['cn'][int(year)] = avg_rate
        for year, avg_rate in hk_data:
            result['hk'][int(year)] = avg_rate
        for year, avg_rate in tw_data:
            result['tw'][int(year)] = avg_rate

        return result
