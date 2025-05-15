# from jinja2 import Template
#
# name = "Макс"
# tm = Template("Привет {{ name }}")
# msg = tm.render(name=name)
#
# print(msg)
from operator import index

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


# from jinja2 import Template
#
# cars = [
#     {'model' : 'audi', 'price' : 23000},
#     {'model' : 'skoda', 'price' : 17300},
#     {'model' : 'volvo', 'price' : 44300},
#     {'model' : 'lada', 'price' : 11000},
# ]
#
# my_str = "Суммарная стоимость всех автомобилей {{ cs | sum(attribute='price') }}"
# tm = Template(my_str)
# msg = tm.render(cs = cars)
#
# print(msg)


# from jinja2 import Template
#
# digs = [1, 2, 3, 4, 5, 6]
#
# my_str = "Сумма чисел списка {{ dg | sum }}"
# tm = Template(my_str)
# msg = tm.render(dg = digs)
#
# print(msg)


# from jinja2 import Template
#
# cars = [
#     {'model' : 'audi', 'price' : 23000},
#     {'model' : 'skoda', 'price' : 17300},
#     {'model' : 'volvo', 'price' : 44300},
#     {'model' : 'lada', 'price' : 11000},
# ]
#
# my_str = "Самый дорогой автомобиль {{ cs | max(attribute='price') }}"
# tm = Template(my_str)
# msg = tm.render(cs = cars)
#
# print(msg)



# from jinja2 import Template
#
# cars = [
#     {'model' : 'audi', 'price' : 23000},
#     {'model' : 'skoda', 'price' : 17300},
#     {'model' : 'volvo', 'price' : 44300},
#     {'model' : 'lada', 'price' : 11000},
# ]
#
# my_str = "Самый дорогой автомобиль {{ (cs | max(attribute='price')).model }}"
# tm = Template(my_str)
# msg = tm.render(cs = cars)
#
# print(msg)


# from jinja2 import Template
#
# cars = [
#     {'model' : 'audi', 'price' : 23000},
#     {'model' : 'skoda', 'price' : 17300},
#     {'model' : 'volvo', 'price' : 44300},
#     {'model' : 'lada', 'price' : 11000},
# ]
#
# my_str = "Самый дорогой автомобиль {{ cs | random }}"
# tm = Template(my_str)
# msg = tm.render(cs = cars)
#
# print(msg)


# from jinja2 import Template
#
# cars = [
#     {'model' : 'audi', 'price' : 23000},
#     {'model' : 'skoda', 'price' : 17300},
#     {'model' : 'volvo', 'price' : 44300},
#     {'model' : 'lada', 'price' : 11000},
# ]
#
# my_str = "Самый дорогой автомобиль {{ cs | replace('a', 'A') }}"
# tm = Template(my_str)
# msg = tm.render(cs = cars)
#
# print(msg)


#
# from jinja2 import Template
#
# persons = [
#     {'name' : 'Alexandr', 'old' : 18, 'weight' : 78.5},
#     {'name' : 'Vlad', 'old' : 38, 'weight' : 88.5},
#     {'name' : 'Oleg', 'old' : 37, 'weight' : 50.5},
#     {'name' : 'Ivan', 'old' : 23, 'weight' : 94.0}
# ]
#
# my_str = """
# {%- for u in users -%}
# {% filter upper %}{{ u.name }}{% endfilter %}
# {% endfor -%}
# """
# tm = Template(my_str)
# msg = tm.render(users = persons)
#
# print(msg)



# from jinja2 import Template
#
# html = """
# {% macro input(name, value='', type='text', size=20) -%}
# <input type="{{ type }}" name="{{ name }} value="{{ value | e }}" size="{{ size }}">
# {%- endmacro %}
#
# <p>{{ input('username') }}
# <p>{{ input('email') }}
# <p>{{ input('password') }}
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

#
# from jinja2 import Template
#
# persons = [
#     {'name' : 'Alexandr', 'old' : 18, 'weight' : 78.5},
#     {'name' : 'Vlad', 'old' : 38, 'weight' : 88.5},
#     {'name' : 'Oleg', 'old' : 37, 'weight' : 50.5},
#     {'name' : 'Ivan', 'old' : 23, 'weight' : 94.0}
# ]
#
# html2 = """
# {% macro list_users(list_of_user) -%}
# <ul>
# {% for u in list_of_user -%}
#     <li>{{ u.name }} {{ caller(u) }}
# {%- endfor %}
# </ul>
# {%- endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#     <li>age: {{ user.old }}
#     <li>weight: {{ user.weight }}
#     </ul>
# {% endcall -%}
# """
#
# tm = Template(html2)
# msg = tm.render(users=persons)
#
# print(msg)



# from jinja2 import Environment, FileSystemLoader
#
# persons = [
#     {'name' : 'Alexandr', 'old' : 18, 'weight' : 78.5},
#     {'name' : 'Vlad', 'old' : 38, 'weight' : 88.5},
#     {'name' : 'Oleg', 'old' : 37, 'weight' : 50.5},
#     {'name' : 'Ivan', 'old' : 23, 'weight' : 94.0}
# ]
#
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main.html')
# msg = tm.render(users = persons)
#
# print(msg)
#
#
# from jinja2 import Environment, FunctionLoader
#
# persons = [
#     {'name' : 'Alexandr', 'old' : 18, 'weight' : 78.5},
#     {'name' : 'Vlad', 'old' : 38, 'weight' : 88.5},
#     {'name' : 'Oleg', 'old' : 37, 'weight' : 50.5},
#     {'name' : 'Ivan', 'old' : 23, 'weight' : 94.0}
# ]
#
# def load_tpl(path):
#     if path == "index":
#         return """Имя {{ u.name }}, возраст {{ u.old }}"""
#     else:
#         return """Данные: {{ u }}"""
#
# file_loader = FunctionLoader(load_tpl)
# env = Environment(loader=file_loader)
#
# tm = env.get_template('index')
# msg = tm.render(u = persons[0])
#
# print(msg)