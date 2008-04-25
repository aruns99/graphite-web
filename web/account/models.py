"""Copyright 2008 Orbitz WorldWide

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

from django.db import models


class Profile(models.Model):
  class Admin: pass
  username = models.CharField(maxlength=64)
  history = models.TextField(default="")
  advancedUI = models.BooleanField(default=False)
  __str__ = lambda self: self.username

class Variable(models.Model):
  class Admin: pass
  profile = models.ForeignKey(Profile)
  name = models.CharField(maxlength=64)
  value = models.CharField(maxlength=64)

class View(models.Model):
  class Admin: pass
  profile = models.ForeignKey(Profile)
  name = models.CharField(maxlength=64)
  
class Window(models.Model):
  class Admin: pass
  view = models.ForeignKey(View)
  name = models.CharField(maxlength=64)
  top = models.IntegerField()
  left = models.IntegerField()
  width = models.IntegerField()
  height = models.IntegerField()
  url = models.TextField()
  interval = models.IntegerField(null=True)

class MyGraph(models.Model):
  class Admin: pass
  profile = models.ForeignKey(Profile)
  name = models.CharField(maxlength=64)
  url = models.TextField()
