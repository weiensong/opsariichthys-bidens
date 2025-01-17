from enum import unique, Enum


@unique
class API(Enum):
    PROVINCE = 'province'  # 各个省份包含大学
    DUAL_CLASS = 'dual_class'  # 各省份包含双一流数量
    TYPE = 'type'  # 学校类别统计
    MAJOR = 'major'  # 所有专业统计
    ADMISSIONS = 'admissions'  # 招生统计
    BIG_DATA = 'big_data'  # 不同大数据专业统计
    BIG_DATA_PROVINCE = 'big_data_province'  # 含大数据专业的省份内大学统计
    BIG_DATA_TYPE = 'big_data_type'  # 大数据本科专科统计
    BIG_DATA_LEVEL2 = 'big_data_level2'  # 大数据二级类目统计
    BIG_DATA_LEVEL3 = 'big_data_level3'  # 大数据一级类目统计
    BIG_DATA_IN_DUAL = 'big_data_in_dual'  # 大数据在双一流占比
    BIG_DATA_IN_NULL = 'big_data_in_null'  # 大数据在普通院校占比
    ARTIFICIAL_INTELLIGENCE_IN_DUAL = 'artificial_intelligence_in_dual'  # 人工智能在双一流占比
    ARTIFICIAL_INTELLIGENCE_IN_NULL = 'artificial_intelligence_in_null'  # 人工智能在普通院校占比

    @staticmethod
    def _get_description() -> dict:
        return {
            'province': 'Each province contains a university.',
            'dual_class': 'Each province contains the number of double first-class.',
            'type': 'School category statistics.',
            'major': 'All majors statistics.',
            'admissions': 'Admissions Statistics.',
            'big_data': 'Statistics of different big data majors.',
            'big_data_province': 'Statistics of provincial universities including Big data majors.',
            'big_data_type': 'Statistics of universities in provinces with big data majors.',
            'big_data_level2': 'Big data secondary category statistics.',
            'big_data_level3': 'Big data primary category statistics.',
            'big_data_in_dual': 'Proportion of Big Data in 211/985.',
            'big_data_in_null': 'The proportion of big data in ordinary colleges and universities.',
            'artificial_intelligence_in_dual': 'The proportion of artificial intelligence in 211/985.',
            'artificial_intelligence_in_null': 'The proportion of artificial intelligence in ordinary universities.',
        }

    def __str__(self):
        descriptions = self._get_description()
        return descriptions.get(self.value)

    @staticmethod
    def get_api():
        for api in API:
            yield api.value, api
