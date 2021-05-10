from rest_framework import status
from rest_framework.test import APITestCase
from main.models import Task
from main.serializers import TaskSerializer


class TodoAPITestCase(APITestCase):

    def setUp(self):
        Task.objects.create(
            title='task1',
            content='task content',
            created='2021-05-08'
        )
        Task.objects.create(
            title='task2',
            content='task content',
            created='2021-05-09'
        )

    def test_get_list(self):
        task_1 = Task.objects.get(title='task1')
        task_2 = Task.objects.get(title='task2')
        url = '/api/v1/todo/'
        response = self.client.get(url)
        serializer_data = TaskSerializer([task_1, task_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        task_1 = Task.objects.get(title='task1')
        url = '/api/v1/todo/1/'
        response = self.client.get(url)
        serializer_data = TaskSerializer(task_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
