from django_crontab import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'blood_donation_app.my_cron_job'


    def do(self):
        print("hello")
        
