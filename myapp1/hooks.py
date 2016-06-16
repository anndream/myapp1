# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "myapp1"
app_title = "Myapp1"
app_publisher = "kajookdev"
app_description = "Demo app "
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "kajookdev@demo.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/myapp1/css/myapp1.css"
# app_include_js = "/assets/myapp1/js/myapp1.js"

# include js, css files in header of web template
web_include_css = "/assets/myapp1/css/myapp1.css"
web_include_js = "/assets/myapp1/js/myapp1.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "myapp1.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "myapp1.install.before_install"
# after_install = "myapp1.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "myapp1.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"myapp1.tasks.all"
# 	],
# 	"daily": [
# 		"myapp1.tasks.daily"
# 	],
# 	"hourly": [
# 		"myapp1.tasks.hourly"
# 	],
# 	"weekly": [
# 		"myapp1.tasks.weekly"
# 	]
# 	"monthly": [
# 		"myapp1.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "myapp1.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "myapp1.event.get_events"
# }

