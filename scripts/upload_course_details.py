import pandas as pd
import requests

SERVER = "http://127.0.0.1"
PORT = "8000"
TOKEN = "038f51f95bccd2e4d2e4957bcbd3fb3523170f49"

def import_excel(excel_name):

    df = pd.read_excel(excel_name, sheet_name='data')

    courses = list()

    for i in df.index:
        course_code = df['COURSE CODE'][i]
        course_title = df['COURSE TITLE'][i]

        if str(course_code) == 'nan':
            continue
        else:
            cd = {'code': course_code, 'name': course_title}
            if cd not in courses:
                courses.append(cd)

    for course in courses:
        response = requests.post(f"{SERVER}:{PORT}/api/subject/", course, headers={'Authorization': f'Token {TOKEN}'})
        print(response)


if __name__ == '__main__':
    import_excel('courselist.xls')