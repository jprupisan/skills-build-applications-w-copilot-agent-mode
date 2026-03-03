from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Deleting old data...'))
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()
            Workout.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Creating teams...'))
            marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
            dc = Team.objects.create(name='DC', description='DC superheroes')

            self.stdout.write(self.style.SUCCESS('Creating users...'))
            users = [
                User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
                User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
                User.objects.create(name='Hulk', email='hulk@marvel.com', team=marvel),
                User.objects.create(name='Superman', email='superman@dc.com', team=dc),
                User.objects.create(name='Batman', email='batman@dc.com', team=dc),
                User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            ]

            self.stdout.write(self.style.SUCCESS('Creating workouts...'))
            workouts = [
                Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy'),
                Workout.objects.create(name='Running', description='Cardio', difficulty='Medium'),
                Workout.objects.create(name='Swimming', description='Full body', difficulty='Hard'),
            ]

            self.stdout.write(self.style.SUCCESS('Creating activities...'))
            Activity.objects.create(user=users[0], workout=workouts[0], duration=30, notes='Morning session')
            Activity.objects.create(user=users[1], workout=workouts[1], duration=45, notes='Afternoon run')
            Activity.objects.create(user=users[2], workout=workouts[2], duration=60, notes='Evening swim')
            Activity.objects.create(user=users[3], workout=workouts[0], duration=20, notes='Quick pushups')
            Activity.objects.create(user=users[4], workout=workouts[1], duration=35, notes='Jogging')
            Activity.objects.create(user=users[5], workout=workouts[2], duration=50, notes='Pool training')

            self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
            Leaderboard.objects.create(user=users[0], score=100, rank=1)
            Leaderboard.objects.create(user=users[1], score=90, rank=2)
            Leaderboard.objects.create(user=users[2], score=80, rank=3)
            Leaderboard.objects.create(user=users[3], score=95, rank=1)
            Leaderboard.objects.create(user=users[4], score=85, rank=2)
            Leaderboard.objects.create(user=users[5], score=75, rank=3)

            self.stdout.write(self.style.SUCCESS('Test data successfully populated!'))
