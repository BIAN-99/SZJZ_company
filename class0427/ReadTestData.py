from json import loads
import pandas


class ReadTestDataUtil:
    """
        读取文本文档
        参数是一个文件的路径
        返回一个数据的集合
    """

    def read_txt_for_single(self, file_name):
        li = []
        with open(file_name, 'r') as data:
            for line in data:
                li.append(line.strip())
        return li

    """
        读取文本文档
        参数是一个文件的路径
        返回一个数据的多维集合
    """

    def read_txt_for_many(self, file_name):
        li = []
        with open(file_name, 'r') as data:
            for line in data:
                li.append(line.strip().split(","))
        return li

    """
        kjsdhkjfshdkf
    """

    def read_properties(self, file_name):
        with open(file_name, 'r') as data:
            for line in data:
                print(line.strip())

    """
        读取json文件
    """

    def read_json(self, file_name):
        li = ''
        with open(file_name, 'r') as data:
            for line in data:
                li += line.strip()
        return loads(li)

    """
        读取csv
    """

    def read_csv_my(self, file_name):
        print(pandas.read_csv(file_name, encoding='GBK').to_string())

    """
        
    """

    def read_excel_my(self, file_name):
        print(pandas.read_excel(file_name))


ReadTestDataUtil().read_excel_my('motos.xlsx')
