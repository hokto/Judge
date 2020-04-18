#ファイルの読み込み、書き込みに関する関数をモジュール化

def read(file_name="",separate_word=""):
    try:
        file_=open(file_name)
        file_data=file_.read()
        file_data_list=file_data.split(separate_word)
        #余計な空白文字が入ることがあったため追加
        if file_data_list[len(file_data_list)-1]=="":
            file_data_list.pop(-1)
        return file_data_list
    except Exception as exc:
        print("FileError:",exc)
        return []


def write(file_name="",separate_word="",data=None,mode="w"):
    try:
        file_=open(file_name,mode)
        if data==[] or data is None:
            print("DataError:No datas in data")
            return
        data_write=separate_word.join(data)
        file_.write(data_write)
    except Exception as exc:
        print("FileError:",exc)
