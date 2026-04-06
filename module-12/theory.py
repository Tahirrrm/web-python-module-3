import json
import pickle

product = {
    "id": 1,
    "name": "Product-1",
    "price": 900
}

json_text = json.dumps(product, indent = 2)
print(json_text)

restored_product = json.loads(json_text)
# print(restored_product)

with open ("product.json","w", encoding = "utf-8") as f:
    json.dump(product, f, indent=2)

with open("product.json", "r", encoding = "utf=8") as f:
    loaded_product = json.load(f)
print(loaded_product)

data = pickle.dumps(product)
print(data)

restored_pk1_product = pickle.loads(data)
print(restored_pk1_product)

with open("product.pkl","wb") as f:
    pickle.dump(product, f)

with open("product.pkl","rb") as f:
    loaded_product_pkl = pickle.load(f)
print(loaded_product_pkl)

#Prototype

import copy

template_order = {
    "deivery" :"standart",
    "promo": False,
    "items": ["book"]
}
fast_order = copy.deepcopy(template_order)
fast_order["delivery"] = "express"
print(template_order,fast_order)

#Cтруктурные паттерны
#Adapter
class OldSmsService:
    def send_sms(self, phone, text):
        print(f"old service: {phone}:{text}")

class SmsAdapter:
    def __init__(self, service, phone):
        self.service = service
        self.phone = phone

    def send(self, message):
        self.service.send_sms(self.phone,message)

SmsAdapter(OldSmsService(), "+79999999999"). send("Сообщение")
#Bring

class TV:
    def turn_on(self):
        return "TV is on"
    
class Radio:
    def turn_on(self):
        return "Radio is on"
    
class RemoveControl:
    def __init__(self,device):
        self.device = device

    def power(self):
        return self.device.turn_on()
    
print(RemoveControl(TV()).power())

# Composite

class File:
    def __init__(self,name,size):
        self.name = name
        self.size = size
    
    def get_size(self):
        return self.size
    
class Folder:
    def __init__(self,name):
        self.name = name
        self.children = []

    def add(self, child):
        self.children.append(child)
    
    def get_size(self):
        return sum(child.get_size() for child in self.children)
    
docs = Folder("docs")
docs.add(File("text_1.txt", 10))
docs.add(File("text_2.txt",20))
print(docs.get_size())

#Decorator

class Coffee:
    def price(self):
        return 120
    
    def description(self):
        return "Кофе"
    
class MilkDecorator:
    def __init__(self,drink):
        self.drink = drink

    def price(self):
        return self.drink.price() + 30
    
    def description(self):
        return self.drink.description() + ", молоко"

class SyrupDecorator:
    def __init__(self,drink):
        self.drink = drink

    def price(self):
        return self.drink.price() + 25
    
    def description(self):
        return self.drink.description() + ", сироп"
    
drink = SyrupDecorator(MilkDecorator(Coffee()))
print(drink.price(), drink.description())

#Facade
class PaymentService:
    def pay(self, amount):
        print(f"Оплата {amount} подтверждена")
class WarehouseService:
    def reserve(self,item):
        print(f"Доставка для {item} создана")
    
class DeliveryService:
    def create(self,item):
        print(f"Доставка для {item} создана")

class OrderFacade:
    def __init__(self):
        self.payment = PaymentService()
        self.warehouse = WarehouseService()
        self.delivery = DeliveryService()

    def place_order(self, item, amount):
        self.payment.pay(amount)
        self.warehouse.reserve(item)
        self.delivery.create(item)
        print("Заказ оформлен")

OrderFacade().place_order("Наушники", 9999)

#Flyweight

class Flayweight:
    def __init__(self,color):
        self.color = color

    def draw(self, x, y):
        print(self.color, x, y)
class Factory:
        _cached = {}
        @classmethod
        def get(cls,color):
            if color not in cls._cached:
                cls._cached[color] = Flayweight(color)
            return cls._cached[color]
            
red1 = Factory.get("red")
red2 = Factory.get("red")

print(red1 is red2)

#Proxy

class Image:
    def __init__(self,path):
        print("Загрузка")
        self.path = path

    def show(self):
        print(f"Show {self.path}")

class ImageProxy:
    def __init__(self,path):
        self.path = path
        self._real = None

    def show(self):
        if self._real is None:
            self._real = Image(self.path)
        self._real.show()
        

img = Image("photo.png")
img.show() #Загрузка
img.show() #Пусто

# Поведенчиские паттерны

# Chain of Responsibility
class Handler:
    def __init__(self, next_handler = None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return "Unhandled"
    
class AuthHandler(Handler):
    def handle(self, request):
        if not request.get("user"):
            return "401 Unathorized"
        return super().handle(request)
    
class RoleHandler(Handler):
    def handle(self, request):
        if request.get("role") !="admin" :
            return "403 Forbidden"
        return super().handle(request)
chain = AuthHandler(RoleHandler())
print(chain.handle({"user": "alice", "role":"admin"}))


#Command
class Light:
    def on(self):
        print("Light is on")

class TurnOncommand:
    def __init__(self,light):
        self.light = light

    def execute(self):
        self.light.on()

class Button:
    def __init__(self,command):
        self.command = command

    def press(self):
        self.command.execute()

Button(TurnOncommand(Light())).press()

#Mediator
class ChatMediator:
    def send(self,message,user):
        for c in user.colleagues:
            if c is not user:
                c.receive(message)

class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        self.colleagues = []

    def send(self, message):
        self.mediator.send(f"{self.name}: {message}", self)

    def receive(self,message):
        print(message)

mediator = ChatMediator()
alice = User("Alice", mediator)
bob = User("Bob", mediator)
alice.colleagues = [alice,bob]
bob.colleagues = [alice,bob]
alice.send("Привет")

#Memento

class Editor:
    def __init__(self):
        self.text = ""
    
    def write(self,text):
        self.text += text
    
    def save(self):
        return self.text
    
    def restore(self,snapshot):
        self.text = snapshot
    
editor = Editor()
editor.write("Hello")
snapshot = editor.save()
editor.write(", world")
print(editor.text)
editor.restore(snapshot)
print(editor.text)

#Observer

class Order:
    def __init__(self):
        self.subscribers = []
    
    def subscribe(self, listener):
        self.subscribers.append(listener)

    def set_status(self, status):
        for subscriber in self.subscribers:
            subscriber(status)
def email_listener(status):
    print(f"Email: Произошла смена статуса на {status}")

def sms_listener(status):
    print(f"SMS: Произошла смена статуса на {status}")

order = Order()
order.subscribe(email_listener)
order.subscribe(sms_listener)
order.set_status("delivery")

#State

class DraftState:
    def publish(self, document):
        document.state = ReviewState()
        return "Черновик отправлен на проверку"
    
class ReviewState:
    def publish(self, document):
        document.state = PublishedState()
        return " Документ опубликован"
    
class PublishedState:
    def publish(self,document):
        return "Уже опубликовано"
    
class Document:
    def __init__(self):
        self.state = DraftState()

    def publish(self):
            return self.state.publish(self)
        
doc = Document()
doc.publish()
doc.publish()
doc.publish()

# Strategy

class StandardDelivery:
    def calculate(self, weight):
        return 200 + weight * 10
    
class ExpressDelivery:
    def calculate(self, weight):
        return 500 + weight * 20
    
class PickupDelivery:
    def calculate(self, weight):
        return 0
    
class DeliveryCalc:
    def __init__(self, strategy):
        self.strategy = strategy

    def get_price(self, weigth):
        return self.strategy.calculate(weigth)
    
print(DeliveryCalc(PickupDelivery()).get_price(10))