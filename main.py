# 记事本核心数据与方法
note_list = []

def add_note(title, content):
    """新增笔记"""
    new_note = {
        "title": title,
        "content": content
    }
    note_list.append(new_note)
    return True

def get_all_notes():
    """获取全部笔记"""
    return note_list