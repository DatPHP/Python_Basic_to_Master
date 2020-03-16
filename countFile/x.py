from functools import reduce


def count_files(folder, extension):
    ext = extension.split(".")[-1]

    def f(count, next_item):
        try:
            count += count_files(next_item['items'], extension)
        except KeyError:
            if next_item["name"].split(".")[-1] == ext:
                count += 1
        return count
    return reduce(f, folder, 0)
folder =  [{'name':'eee.py'}, {'name':'aaa.py'}, {'name':'bbb.html'}, {'name':'ccc.js'}, {'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}, {'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}]}]},{'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}, {'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}]}]}, {'name':'aaa.py'}, {'name':'bbb.py'}];
print(count_files(folder,".py"))