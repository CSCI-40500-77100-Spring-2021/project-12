from django.test import TestCase
from django.test import Client
from django.conf import settings
from django.template.loader import render_to_string
from SE.models import Assignment
from SE.forms import AssignmentForm

# Create your tests here.
class UnitTest_1(TestCase):
  def test_crsf(self):
    csrf_client = Client(enforce_csrf_checks=True)
    
  def test_syllabus(self):
    client = Client()
    response = client.get("/conveniote/syllabus")
    self.assertEqual(response.status_code, 200)

  def test_homepage(self):
    client = Client()
    response = client.get("/conveniote/home")
    self.assertEqual(response.status_code, 200)
    response.content
    
  def test_template(self):
    with self.assertTemplateUsed(template_name='index.html'):
      render_to_string('index.html')
      
  def test_notes(self):
    client = Client()
    response = client.post("/conveniote/notes", {'notes':'notes'})
    self.assertFormError(response, 'form', 'notes', None)

class UnitTest_2(TestCase):    
  def test_form(self):
      with self.assertTemplateUsed(template_name='assignment_form.html'):
          render_to_string('assignment_form.html')

  def test_file(self):
      client = Client()
      response = client.post('/conveniote/assignment', {'file': 'Child.jpeg', 'platform':'Github'})
      self.assertEqual(response.status_code, 200)

  def test_submission(self):
      client = Client()
      response = client.post('/conveniote/assignment', {'written_submission': 'This is a test'})
      self.assertEqual(response.status_code, 200)

  def test_validateForm(self):
      form_data = {'file': 'file', 'platform': 'platform'}
      form = AssignmentForm(data=form_data)
      self.assertTrue(form.is_valid())

  def test_errors(self):
      response = self.client.post("/conveniote/assignment", {'comment':'comment'})
      self.assertFormError(response, 'form', 'comment', None)
