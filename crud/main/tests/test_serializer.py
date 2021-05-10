from collections import OrderedDict

from django.test import TestCase
from main.serializers import TaskSerializer
from main.models import Task


class TaskSerializerTestCase(TestCase):
    def test_serializer(self):
        task_1 = Task.objects.create(
            title='task1',
            content='task content',
            created='2021-05-08'
        )
        task_2 = Task.objects.create(
            title='task2',
            content='task content',
            created='2021-05-09'
        )
        data = TaskSerializer([task_1, task_2], many=True).data
        expected_data = [
            OrderedDict(
                [
                    ('id', task_1.id),
                    ('title', 'task1'),
                    ('content', 'task content'),
                    ('created', '2021-05-08')
                ]
            ),
            OrderedDict(
                [
                    ('id', task_2.id),
                    ('title', 'task2'),
                    ('content', 'task content'),
                    ('created', '2021-05-09')
                ]
            )
        ]
        self.assertEqual(expected_data, data)
