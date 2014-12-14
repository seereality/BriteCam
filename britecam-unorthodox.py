from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
#from google.appengine.ext import blobstore
#from google.appengine.ext.webapp import blobstore_handlers

import os
import urllib
import webapp2
import jinja2

providers = {
    'Google'   : 'https://www.google.com/accounts/o8/id',
    'Yahoo'    : 'yahoo.com',
    'MySpace'  : 'myspace.com',
#    'AOL'      : 'aol.com',
    'MyOpenID' : 'myopenid.com'
   # 'Facebook' : 'facebook.com'
    # add more here
}

JINJA_ENVIRONMENT = jinja2.Environment(
		loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
		extensions=['jinja2.ext.autoescape'],
		autoescape=True)

class MainPage(webapp2.RequestHandler):

	def get(self):

		provs = []
		user = users.get_current_user()
		url_logout = ''
		url_logout_linktext = ''

		if users.get_current_user():
			user = user.nickname()
			url_logout = users.create_logout_url(self.request.uri)
			url_logout_linktext = "Logout"

		else:
			#self.redirect(users.create_login_url(self.request.uri))
			for name, uri in providers.items():
				provs.append([users.create_login_url(federated_identity=uri), name])		

		template_values = {
			'url_logout': url_logout,
			'url_logout_linktext': url_logout_linktext,
			'providers': provs,
			'user': user,
		}

		template = JINJA_ENVIRONMENT.get_template('./index.html')
		self.response.write(template.render(template_values))

class VideochatPage(webapp2.RequestHandler):

	def get(self):

		user = users.get_current_user()
		url_logout = ''
		url_logout_linktext = ''

		if users.get_current_user():
			user = user.nickname()
			url_logout = users.create_logout_url(self.request.uri)
			url_logout_linktext = "Logout"

		else:
			self.redirect('/')		

		template_values = {
			'url_logout': url_logout,
			'url_logout_linktext': url_logout_linktext,
			'user': user,
		}

		template = JINJA_ENVIRONMENT.get_template('videochat.html')
		self.response.write(template.render(template_values))

class ArchivePage(webapp2.RequestHandler):

	def get(self):

		user = users.get_current_user()
		url_logout = ''
		url_logout_linktext = ''

		if users.get_current_user():
			user = user.nickname()
			url_logout = users.create_logout_url(self.request.uri)
			url_logout_linktext = "Logout"

		else:
			self.redirect('/')		

		template_values = {
			'url_logout': url_logout,
			'url_logout_linktext': url_logout_linktext,
			'user': user,
		}

		template = JINJA_ENVIRONMENT.get_template('recording.html')
		self.response.write(template.render(template_values))

class ContactPage(webapp2.RequestHandler):

	def get(self):

		user = users.get_current_user()
		url_logout = ''
		url_logout_linktext = ''

		if users.get_current_user():
			user = user.nickname()
			url_logout = users.create_logout_url(self.request.uri)
			url_logout_linktext = "Logout"

		else:
			self.redirect('/')		

		template_values = {
			'url_logout': url_logout,
			'url_logout_linktext': url_logout_linktext,
			'user': user,
		}

		template = JINJA_ENVIRONMENT.get_template('contact.html')
		self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([
		('/', MainPage),
		('/archive', ArchivePage),
		('/chat', VideochatPage),
		('/contact', ContactPage)
], debug=True)
