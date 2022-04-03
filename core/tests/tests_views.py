from django.test import TestCase
from django.urls import reverse, resolve

from core.views import home, board_topics
from core.models import Board, Topic, Post


class HomeTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.board = Board.objects.create(name='Django', description='Django board.')

    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolve_home_view(self):
        self.assertEquals(resolve('/').func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board-topic', kwargs={'pk': self.board.pk})
        self.assertContains(self.client.get(reverse('home')), 'href="{0}"'.format(board_topics_url))


class TopicsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Board.objects.create(name='Django', description='Django board.')

    """
     def test_board_topics_view_success_status_code(self):
        url = reverse('board-topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    """

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board-topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board-topic', kwargs={'pk': 1})
        self.assertContains(self.client.get(board_topics_url), 'href="{0}"'.format(reverse('home')))
