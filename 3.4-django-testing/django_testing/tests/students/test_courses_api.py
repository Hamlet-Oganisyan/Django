import pytest
from rest_framework.test import APIClient
from model_bakery import bakery
from students.models import Course, Student


@pytest.fixture()
def client():
    return APIClient()

@pytest.fixture()
def courses_factory():
    def factory(*args, **kwargs):
        bakery.make(Course, *args, **kwargs )
    return factory

@pytest.fixture()
def student_factory():
    def factory(*args, **kwargs):
        bakery.make(Student, *args, **kwargs )
    return APIClient()

# проверка получения 1-го курса "GET" запросом
@pytest.mark.django_db
def test_course(client):
    course = Course.create(name='java')
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course.name


# проверка получения списка курсов
@pytest.mark.django_db
def test_courses_get(client, courses_factory):
    course = courses_factory(_quantity=15)
    url = '/api/v1/courses/'
    response = client.get(url, data={'id':f'{course[0].id}'})
    url = reverse('courses-list')
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


# проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_filter_id(client, courses_factory):
    course = courses_factory(_quantity=15)
    url = '/api/v1/courses/'
    response = client.get(url, data={'id': f'{course[0].id}'})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == course[0].id


# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_filter_name(client, courses_factory):
    course = courses_factory(_quantity=15)
    url = '/api/v1/courses/'
    response = client.get(url, data={'name': f'{course[0].name}'})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course[0].name


# тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    response = client.('/api/v1/courses/', data = {'name': 'python'})
    data = response.json()
    assert response.status_code == 201
    assert data[0]['name'] == response[0].name


# тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client):
    course = Course.objects.create(name='java') # создаем курс Java
    response = client.patch(f'/api/v1/courses/{course.id}/', data={'name': 'python'}) #меняем название курса на python
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'python' # проверяем корректность возврата курса


# тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client):
    course = Course.objects.create(id=1, name='C+')  # создаем курс
    response = client.delete(f'/api/v1/courses/{course.id}/')  # Удаляем курс