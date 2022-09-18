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
    first_table_not_selected = final_df.pivot_table(index='Department',
                                                    columns=['left', 'salary'],
                                                    values='average_monthly_hours',
                                                    aggfunc='median').round(2)
    first_table = first_table_not_selected[
        (first_table_not_selected[0.0]['high'] < first_table_not_selected[0.0]['medium']) | (
                first_table_not_selected[1.0]['low'] < first_table_not_selected[1.0]['high'])]

    second_table_not_selected = final_df.pivot_table(index='time_spend_company',
                                                     columns='promotion_last_5years',
                                                     values=['satisfaction_level', 'last_evaluation'],
                                                     aggfunc=['min', 'max', 'mean']).round(2)

    second_table = second_table_not_selected[
        second_table_not_selected['mean']['last_evaluation'][0] > second_table_not_selected['mean']['last_evaluation'][
            1]]

    print(first_table.to_dict())
    print(second_table.to_dict())
