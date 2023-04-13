# class StackObj:  # - для описания объектов односвязного списка;
#
#     def __init__(self, data):
#         self.__data = data  # - ссылка на строку с данными, указанными при создании объекта;
#         self.__next = None  # -ссылка на следующий объект класса StackObj
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, value):
#         self.__data = value
#
#     @property
#     def next(self):  # - для записи и считывания информации из локального приватного свойства __next;
#         return self.__next
#
#     @next.setter
#     def next(self, obj):
#         if isinstance(obj, StackObj) or obj == None:
#             self.__next = obj
#
#
# class Stack:  # - для управления односвязным списком.
#
#     def __init__(self):
#         self.top = None
#         self.last = None
#
#     def push(self, obj):  # - добавление объекта класса StackObj в конец односвязного списка;
#         if self.last:
#             self.last.next = obj
#
#         self.last = obj
#
#         if self.top is None:
#             self.top = obj
#
#     def pop(self):  # - извлечение последнего объекта с его удалением из односвязного списка;
#         t = self.top
#         if t is None:
#             return
#         while t and t.next != self.last:
#             t = t.next
#         if t:
#             t.next = None
#         last = self.last
#         self.last = t
#         if self.last is None:
#             self.top = None
#
#         return last
#
#     def get_data(self):  # -
#         s = []
#         h = self.top
#         while h:
#             s.append(h.data)
#             h = h.next
#
#         return s

# class PhoneNumber:
#
#     def __init__(self, number, fio):
#         self.number = number
#         self.fio = fio
#
#
# class PhoneBook:
#
#     def __init__(self):
#         self.phone_list = []
#
#     def add_phone(self, phone):
#         self.phone_list.append(phone)
#
#     def remove_phone(self, indx):
#         self.phone_list.remove(indx)
#
#     def get_phone_list(self):
#         return self.phone_list


# class HandlerGET:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, request, *args, **kwargs):
#         m = request.get('method', 'GET')
#         if m == 'GET':
#             return self.get(self.func, request)
#
#     def get(self, func, request, *args, **kwargs):
#         return f'GET: {func(request)}'

class Handler:
    def __init__(self, methods=('GET', )):
        self.__methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request, *args, **kwargs):
            m = request.get('method', 'GET')
            if m in self.__methods:
                method = m.lower()
            return self.__getattribute__(method)(func, request)

        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}}'
