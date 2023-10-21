"""
Вложенные классы
"""


class Woman:
    title = 'object_1'
    photo = 'Photo_1'
    ordering = 'class_object'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw

    class Meta:
        ordering = ['id']

        def __init__(self, acs):
            self._access = acs

        # Из этого класса образаться классу выше уже нельзя будет ошибка, что класс не определён, это происходит потому
        # что мы обращаемся по сути к несуществующему пространству имём, что бы это обойти, нужно в инициализаторе
        # класса Meta создать экземпляр Woman, но на практике так делатиь нельзя


w = Woman('admin', '1234')  # Тут важно понимать, что несмотря на вложенность создаётся только экземпляр класса Woman,
# без Meta что бы это сделать нужно явно вызвать экземпляр Meta в инициализаторе в примере выше именно так и сделано

print(Woman.ordering)
print(Woman.Meta.ordering)
