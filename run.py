import argparse
import subprocess

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--test', choices=['Main_page','\n',
                                       'Create_page','\n',
                                       'Search_page','\n',
                                       'Searched_result_page','\n',
                                       'Notifications_page','\n',
                                       'Shorts_page','\n' ],
                    help='Choose name for run test')
parser.add_argument('--allure', choices=['Yes', 'No'],
                    help='Choose Yes if you want generate allure document about tests result')

args = parser.parse_args()

if(args.test == 'Main_page'):
    subprocess.call(['pytest','--alluredir=allure-report/', r'.\venv\tests\test.py'], shell=True)
elif(args.test == 'Create_page' ):
    subprocess.call(['pytest','--alluredir=allure-report/', r'.\venv\tests\test_for_create_page.py'], shell=True)
elif(args.test == 'Search_page' ):
    subprocess.call(['pytest','--alluredir=allure-report/', r'.\venv\tests\test_for_search_page.py'], shell=True)
elif(args.test == 'Searched_result_page' ):
    subprocess.call(['pytest','--alluredir=allure-report/', r'.\venv\tests\test_for_searched_result.py'], shell=True)
elif(args.test == 'Notifications_page' ):
    subprocess.call(['pytest','--alluredir=allure-report/', r'.\venv\tests\test_notifications_page.py'], shell=True)
elif(args.test == 'Shorts_page' ):
    subprocess.call(['pytest','--alluredir=allure-report/', r'.\venv\tests\test_shorts_page.py'], shell=True)

if(args.allure == 'Yes'):
    subprocess.call(['allure','serve', r".\allure-report\ "], shell=True)

