from dataclasses import dataclass
from abc import ABC,abstractmethod

@dataclass
class Ingredient:
    name: str
    key: str
    category: str
    price: float
    cost: float

@dataclass
class Recipe:
    name: str
    ingredient_keys: list[str]

class RecipeFactory:
    def get_standard_recipes() -> dict[int, Recipe]:
        return {
            0: Recipe("Пицца-1", ["dough","cheese","tomate","mayonaise","chiken"]),
            1: Recipe("Пицца-2", ["dough","cheese","tomate","ketchup","chiken"]),
            2: Recipe("Пицца-3", ["dough","cheese","tomate","chiken"]),
        }
class PizzaBuilder:
    def __init__(self):
        self._ingredient - ["dough","cheese"]

    def add_ingredient(self,key:str):
        if key not in self._ingredient:
            self._ingredient.append(key)
        return self
    def build(self):
        return Recipe("Своя пицца",self._ingredient)
    
@dataclass   
class OrderItem:
    recipe: Recipe
    quantity: int
    def total_price(self, ingredients: dict [int, Ingredient]) -> float:
        one_pizza_price = sum(
            ingredients[key].price for key in self.recipe.ingredient_keys
        )
        return one_pizza_price *self.quantity
    def total_cost(self, ingredients: dict [int, Ingredient]) -> float:
        one_pizza_cost = sum(
            ingredients[key].price for key in self.recipe.ingredient_keys
        )
        return one_pizza_cost *self.quantity

@dataclass
class Order:
    items: list[OrderItem]
    payment_type: str

    def total_price(self,ingredients:dict[str,Ingredient]):
        return sum(item.total_price(ingredients) for item in self.items)
    
    def total_cost(self,ingredients:dict[str,Ingredient]):
        return sum(item.total_cost(ingredients) for item in self.items)
    
    def total_profit(self,ingredients:dict[str,Ingredient]):
        return self.total_price(ingredients) - self.total_cost(ingredients)
    
    def to_text(self, ingredients: dict[str, Ingredient]) -> str:
        lines = ["Информация о заказе:"]
        for item in self.items:
            ingredients_names = [
                Ingredient[key].name for key in item.recipe.ingredient_keys
            ]
            lines.append(f"Пицца: {item.recipe.name}")
            lines.append(f"Количество: {item.quantity}")
            lines.append("Состав:")
            for name in ingredients_names:
                lines.append(f"-{name}")
            lines.append(f"Цена позиции: {item.total_price(ingredients)} руб.")
            lines.append(f"Способ  оплаты: {self.payment_type}")

        return "\n".join(lines)
    
    class PaymentStrategy(ABC):
        @abstractmethod
        def pay(self,amount:float):
            pass
    class CashPayment(PaymentStrategy):
        def pay(self,amount:float):
            return f"Оплата наличными выполнена на сумму {amount} руб"
        
    class CardPayment(PaymentStrategy):
        def pay(self,amount:float):
            return f"Оплата картой выполнена на сумму {amount} руб"
        
    class FileOrderSaver:
        def __init__(self,filename: str = "order.txt"):
            self.filename = filename
        def save(self, order: Order, ingredients: dict[str, Ingredient]):
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(order.to_text(ingredients))
                file.write("\n" + "-" *50 + "\n")

    def create_ingredients():
        return{
            "dough": Ingredient("Тесто", "dough", 70,30),
            "cheese": Ingredient("Сыр", "cheese", 80,20),
            "tomate": Ingredient("Помидор", "tomate",20,5),
            "mayonaise": Ingredient("Майонез", "mayonaise",50,10),
            "chiken": Ingredient("курица", "chiken",100,50),
            "ketchup": Ingredient("кетчуп", "ketchup",15,3),
        }
