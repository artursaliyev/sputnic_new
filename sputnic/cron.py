import os
import codecs
import json
import shutil

from django_cron import CronJobBase, Schedule

from core_site_sputnic.settings import BASE_DIR
from sputnic.models import Sputnic, ObjectSputnic, RubricSputnic


class SputnicCronJob(CronJobBase):

    # har 5 minutda bajarish
    RUN_EVERY_MINS = 10

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'sputnic.my_cron_job'

    def do(self):
        files = self.list_json_files()

        for file in files:
            data = self.input_file_name_return_json_data(file)

            if data:
                    self.save_file_db(data)

            try:
                shutil.move(
                    BASE_DIR + '/input_files/' + file,
                    BASE_DIR + '/finished_files/' + file,
                )
            except:
                pass

    @staticmethod
    def input_file_name_return_json_data(file_name):
        url = BASE_DIR + '/input_files/' + file_name
        try:
            data = json.load(codecs.open(url, 'r', 'utf-8-sig'), strict=False)
            return data
        except:
            return {}

    @staticmethod
    def list_json_files():
        path_input_data = BASE_DIR + '/input_files/'
        path_list = [path for path in os.listdir(path_input_data) if path.endswith('.json')]
        return path_list

    @staticmethod
    def save_file_db(obj_list):

        for key, obj in enumerate(obj_list['data']):
            try:
                sputnic_obj = Sputnic.objects.update_or_create(
                                title=obj['title'],
                                defaults={
                                    'author': obj['author'],
                                    'description': obj['description'],
                                    'date': obj['date'],
                                    'time': obj['time'],
                                    'domain': obj['domain'],
                                    'url': obj['url'],

                                    'route_api': obj_list['route-api'],
                                    'heading': obj_list['heading'],
                                    'date_get': obj_list['date'],
                                    'time_get': obj_list['time'],
                                    }
                                )

                #     agar yangi bazaga yangi object qoshilsa ishlaydi

                if sputnic_obj[1]:

                    # sleep(1)
                    for rubric_sputnic in obj['rubrics']:
                        # print(rubric_sputnic)
                        try:
                            RubricSputnic.objects.create(
                                head=rubric_sputnic['head'],
                                sputnic=sputnic_obj[0]
                            )
                        except:
                            print('RubricSputnic modeliga yozishda hatolik')

                    # sleep(1)
                    for object_sputnic in obj['objects']:
                        # print(object_sputnic)
                        try:
                            ObjectSputnic.objects.create(
                                type_o=object_sputnic['type'],
                                name_o=object_sputnic['name'],
                                rank_o=object_sputnic['rank'],
                                sputnic=sputnic_obj[0],
                            )
                        except:
                            print('ObjectSputnic modeliga yozishda hatolik')

            except:
                print('Sputnic modeliga yozishda hatolik')

        else:
            print('Bazaga yozilgan zapislar soni: ', key)






