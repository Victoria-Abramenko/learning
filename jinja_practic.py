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