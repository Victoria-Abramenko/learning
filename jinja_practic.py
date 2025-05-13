# from jinja2 import Template
#
# name = "Макс"
# tm = Template("Привет {{ name }}")
# msg = tm.render(name=name)
#
# print(msg)

#
# from jinja2 import Template
#
# name = "Макс"
# age = 28
#
# tm = Template("Привет мне {{ age }} лет и меня зовут {{ name }}")
# msg = tm.render(name=name, age = age)
#
# print(msg)


# from jinja2 import Template
#
# name = "Макс"
# age = 28
#
# tm = Template("Привет мне {{ age * 2 }} лет и меня зовут {{ name.upper() }}")
# msg = tm.render(name=name, age = age)
#
# print(msg)


# from jinja2 import Template
#
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# per = Person("Саша", 33)
#
# tm = Template("Привет мне {{ p.age }} лет и меня зовут {{ p.name }}")
# msg = tm.render(p = per)
#
# print(msg)

#
# from jinja2 import Template
#
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
# per = Person("Саша", 33)
#
# tm = Template("Привет мне {{ p.get_age() }} лет и меня зовут {{ p.get_name() }}")
# msg = tm.render(p = per)
#
# print(msg)


# from jinja2 import Template
#
# per = {"name" : "Макс", "age" : 28}
#
# tm = Template("Привет мне {{ p.age }} лет и меня зовут {{ p.name }}")
# msg = tm.render(p = per)
#
# print(msg)


# from jinja2 import Template
#
# per = {"name" : "Макс", "age" : 28}
#
# tm = Template("Привет мне {{ p['age'] }} лет и меня зовут {{ p['name'] }}")
# msg = tm.render(p = per)
#
# print(msg)


# from jinja2 import Template
#
# data = """ {% raw %}Какой-то текст, который не нужно преобразовывать {{ name }} {% endraw %}"""
# name = "Заяц"
#
# tm = Template(data)
# msg = tm.render(name= name)
#
# print(msg)


# from jinja2 import Template
#
# data = """ В HTML документе ссылки определяются так:
#     <a href='#'>link</a>"""
#
# tm = Template("{{ data | e}}")
# msg = tm.render(data=data)
#
# print(msg)


#
# from markupsafe import escape
#
# data = """ В HTML документе ссылки определяются так:
#     <a href='#'>link</a>"""
#
# msg = escape(data)
#
# print(msg)


# from jinja2 import Template
#
# cities = [{'id' : 1, 'city' : 'Moscow'},
#           {'id' : 2, 'city' : 'Paris'},
#           {'id' : 3, 'city' : 'London'}
#           ]
#
# link = '''<select name="cities">
# {% for c in cities %}
#     <option value="{{ c['id'] }}">{{ c['city'] }}</option>
# {% endfor %}
# </select>'''
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

#
# from jinja2 import Template
#
# cities = [{'id' : 1, 'city' : 'Moscow'},
#           {'id' : 2, 'city' : 'Paris'},
#           {'id' : 3, 'city' : 'London'}
#           ]
#
# link = '''<select name="cities">
# {% for c in cities -%}
#     <option value="{{ c['id'] }}">{{ c['city'] }}</option>
# {% endfor -%}
# </select>'''
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)



# from jinja2 import Template
#
# cities = [{'id' : 1, 'city' : 'Moscow'},
#           {'id' : 2, 'city' : 'Paris'},
#           {'id' : 3, 'city' : 'London'},
#           {'id' : 4, 'city' : 'Orel'}
#           ]
#
# link = '''<select name="cities">
# {% for c in cities -%}
# {% if c.id > 2 -%}
#     <option value="{{ c['id'] }}">{{ c['city'] }}</option>
# {% elif c.city == 'Moscow' -%}
#     <option>{{ c['city'] }}</option>
# {% else -%}
#     {{ c['city'] }}
# {% endif -%}
# {% endfor -%}
# </select>'''
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)