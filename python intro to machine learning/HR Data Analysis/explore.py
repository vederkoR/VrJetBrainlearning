import pandas as pd
import requests
import os


def files_formation():
    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    if ('A_office_data.xml' not in os.listdir('../Data') and
            'B_office_data.xml' not in os.listdir('../Data') and
            'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')


def re_indexer(pd_df, series):
    re_indexed_list = [series + str(i) for i in list(pd_df['employee_office_id'].values)]
    pd_df.index = re_indexed_list


def round_2(x):
    return round(x, 2)


if __name__ == '__main__':
    files_formation()
    pd_a = pd.read_xml("../Data/A_office_data.xml")
    pd_b = pd.read_xml("../Data/B_office_data.xml")
    pd_hr = pd.read_xml("../Data/hr_data.xml")
    re_indexer(pd_a, "A")
    re_indexer(pd_b, "B")
    pd_hr = pd_hr.set_index('employee_id')
    united_office = pd.concat([pd_a, pd_b])
    final_df = united_office.join(pd_hr, how='left')
    final_df = final_df.drop(columns=['employee_office_id'])
    final_df.dropna(inplace=True)
    final_df = final_df.sort_index()
    final_df.left = final_df.left.astype(int)
    final_dict = dict()
    final_dict[('number_project', 'median')] = \
        final_df.groupby('left').agg({'number_project': 'median'}).to_dict()['number_project']
    final_dict[('number_project', 'count_bigger_5')] = \
        final_df[final_df.number_project > 5].groupby('left').agg({'number_project': 'count'}).to_dict()[
            'number_project']
    final_dict[('time_spend_company', 'mean')] = \
        final_df.groupby('left').agg({'time_spend_company': 'mean'}).apply(round_2).to_dict()['time_spend_company']
    final_dict[('time_spend_company', 'median')] = \
        final_df.groupby('left').agg({'time_spend_company': 'median'}).apply(round_2).to_dict()['time_spend_company']
    final_dict[('Work_accident', 'mean')] = \
        final_df.groupby('left').agg({'Work_accident': 'mean'}).apply(round_2).to_dict()['Work_accident']
    final_dict[('last_evaluation', 'mean')] = \
        final_df.groupby('left').agg({'last_evaluation': 'mean'}).apply(round_2).to_dict()['last_evaluation']
    final_dict[('last_evaluation', 'std')] = \
        final_df.groupby('left').agg({'last_evaluation': 'std'}).apply(round_2).to_dict()['last_evaluation']
    print(final_dict)
