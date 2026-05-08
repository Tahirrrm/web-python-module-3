from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Ingredient:
    name: str
    key: str
    price: float
    cost: float


@dataclass
class Recipe:
    name: str
    ingredient_keys: list[str]


class RecipeFactory:
    @staticmethod
    def get_standard_recipes() -> dict[int, Recipe]:
        return {
            1: Recipe("Классический хот-дог", ["sausage", "bun", "ketchup", "mustard"]),
            2: Recipe("Сырный хот-дог", ["sausage", "bun", "cheese_sauce", "onion"]),
            3: Recipe("Острый хот-дог", ["sausage", "bun", "chili", "jalapeno", "mustard"]),
        }


class HotDogBuilder:
    def __init__(self):
        self._ingredients = ["sausage", "bun"]

    def add_ingredient(self, key: str):
        if key not in self._ingredients:
            self._ingredients.append(key)
        return self

    def build(self) -> Recipe:
        return Recipe("Свой хот-дог", self._ingredients.copy())


@dataclass
class OrderItem:
    recipe: Recipe
    quantity: int

    def total_price(self, ingredients: dict[str, Ingredient]) -> float:
        one_price = sum(
            ingredients[key].price for key in self.recipe.ingredient_keys
        )
        return one_price * self.quantity

    def total_cost(self, ingredients: dict[str, Ingredient]) -> float:
        one_cost = sum(
            ingredients[key].cost for key in self.recipe.ingredient_keys
        )
        return one_cost * self.quantity


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, amount: float, quantity: int) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, amount: float, quantity: int) -> float:
        return amount


class QuantityDiscount(DiscountStrategy):
    def __init__(self, thresholds: list[tuple[int, float]]):
        self.thresholds = sorted(thresholds, reverse=True)

    def apply(self, amount: float, quantity: int) -> float:
        for min_qty, discount_pct in self.thresholds:
            if quantity >= min_qty:
                return amount * (1 - discount_pct)
        return amount


DISCOUNT_RULES = [
    (10, 0.20),
    (7, 0.15),
    (5, 0.10),
    (3, 0.05),
]


@dataclass
class Order:
    items: list[OrderItem]
    payment_type: str
    discount_strategy: DiscountStrategy = None

    def total_quantity(self) -> int:
        return sum(item.quantity for item in self.items)

    def total_price_before_discount(self, ingredients: dict[str, Ingredient]) -> float:
        return sum(item.total_price(ingredients) for item in self.items)

    def total_price(self, ingredients: dict[str, Ingredient]) -> float:
        base = self.total_price_before_discount(ingredients)
        if self.discount_strategy:
            return self.discount_strategy.apply(base, self.total_quantity())
        return base

    def total_cost(self, ingredients: dict[str, Ingredient]) -> float:
        return sum(item.total_cost(ingredients) for item in self.items)

    def total_profit(self, ingredients: dict[str, Ingredient]) -> float:
        return self.total_price(ingredients) - self.total_cost(ingredients)

    def to_text(self, ingredients: dict[str, Ingredient]) -> str:
        lines = ["Информация о заказе:"]
        for item in self.items:
            ingredient_names = [
                ingredients[key].name for key in item.recipe.ingredient_keys
            ]
            lines.append(f"Хот-дог: {item.recipe.name}")
            lines.append(f"Количество: {item.quantity}")
            lines.append("Состав:")
            for name in ingredient_names:
                lines.append(f"  - {name}")
            lines.append(f"Цена позиции: {item.total_price(ingredients):.2f} руб.")

        base_price = self.total_price_before_discount(ingredients)
        lines.append(f"Итого до скидки: {base_price:.2f} руб.")

        if self.total_quantity() >= 3:
            discount = self.discount_strategy.apply(base_price, self.total_quantity())
            lines.append(f"Скидка: {(base_price - discount):.2f} руб.")

        lines.append(f"Итого к оплате: {self.total_price(ingredients):.2f} руб.")
        lines.append(f"Способ оплаты: {self.payment_type}")

        return "\n".join(lines)


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class CashPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Оплата наличными выполнена на сумму {amount:.2f} руб."


class CardPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Оплата картой выполнена на сумму {amount:.2f} руб."


class FileOrderSaver:
    def __init__(self, filename: str = "orders.txt"):
        self.filename = filename

    def save(self, order: Order, ingredients: dict[str, Ingredient]):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(order.to_text(ingredients))
            f.write("\n" + "-" * 50 + "\n")


class Inventory:
    def __init__(self, ingredients: dict[str, Ingredient], stock: dict[str, int]):
        self.ingredients = ingredients
        self.stock = stock

    def has_enough(self, ingredient_keys: list[str], quantity: int) -> bool:
        for key in ingredient_keys:
            if self.stock.get(key, 0) < quantity:
                return False
        return True

    def reduce_stock(self, ingredient_keys: list[str], quantity: int):
        for key in ingredient_keys:
            self.stock[key] -= quantity

    def get_low_stock(self, threshold: int = 3) -> list[str]:
        return [
            self.ingredients[key].name
            for key, count in self.stock.items()
            if count <= threshold
        ]

    def show(self):
        print("\nНаличие ингредиентов:")
        for key, count in self.stock.items():
            ingredient = self.ingredients[key]
            print(f"  {ingredient.name}: {count}")

        low = self.get_low_stock()
        if low:
            print("\nВНИМАНИЕ! Требуется закупить:")
            for name in low:
                print(f"  - {name}")


class SalesReport:
    def __init__(self):
        self.profit = 0.0
        self.revenue = 0.0
        self.sold_count = 0

    def add_order(self, order: Order, ingredients: dict[str, Ingredient]):
        self.sold_count += order.total_quantity()
        self.revenue += order.total_price(ingredients)
        self.profit += order.total_profit(ingredients)

    def show(self):
        print("\n=== Отчёт о продажах ===")
        print(f"Продано хот-догов: {self.sold_count}")
        print(f"Выручка: {self.revenue:.2f} руб.")
        print(f"Прибыль: {self.profit:.2f} руб.")


def create_ingredients() -> dict[str, Ingredient]:
    return {
        "sausage": Ingredient("Сосиска", "sausage", 50, 20),
        "bun": Ingredient("Булка", "bun", 20, 8),
        "ketchup": Ingredient("Кетчуп", "ketchup", 15, 4),
        "mustard": Ingredient("Горчица", "mustard", 10, 3),
        "mayonnaise": Ingredient("Майонез", "mayonnaise", 15, 5),
        "cheese_sauce": Ingredient("Сырный соус", "cheese_sauce", 30, 12),
        "onion": Ingredient("Сладкий лук", "onion", 10, 4),
        "jalapeno": Ingredient("Халапеньо", "jalapeno", 20, 8),
        "chili": Ingredient("Чили", "chili", 20, 7),
        "pickle": Ingredient("Солёный огурец", "pickle", 15, 5),
    }


def create_stock() -> dict[str, int]:
    return {
        "sausage": 30,
        "bun": 30,
        "ketchup": 20,
        "mustard": 20,
        "mayonnaise": 20,
        "cheese_sauce": 15,
        "onion": 15,
        "jalapeno": 15,
        "chili": 15,
        "pickle": 15,
    }


def get_toppings() -> list[str]:
    return [
        "ketchup",
        "mustard",
        "mayonnaise",
        "cheese_sauce",
        "onion",
        "jalapeno",
        "chili",
        "pickle",
    ]


def create_custom_recipe(inventory: Inventory) -> Recipe:
    builder = HotDogBuilder()
    print("\nСоздание своего хот-дога")

    for key in get_toppings():
        ingredient = inventory.ingredients[key]
        choice = input(f"  Добавить {ingredient.name}? (да/нет): ")
        if choice.lower() == "да":
            builder.add_ingredient(key)

    return builder.build()


def show_menu():
    print("\n=== Киоск хот-догов ===")
    print("1. Создать заказ")
    print("2. Отчёт о продажах")
    print("3. Наличие ингредиентов")
    print("4. Выход")


def show_standard_recipes(
    recipes: dict[int, Recipe],
    ingredients: dict[str, Ingredient],
):
    print("\nСтандартные хот-доги:")
    for number, recipe in recipes.items():
        price = sum(ingredients[key].price for key in recipe.ingredient_keys)
        print(f"  {number}. {recipe.name} — {price:.2f} руб.")


def choose_recipe(
    recipes: dict[int, Recipe],
    ingredients: dict[str, Ingredient],
    inventory: Inventory,
) -> Recipe:
    show_standard_recipes(recipes, ingredients)
    print("  0. Свой хот-дог")

    while True:
        choice = input("Выберите рецепт (0-3): ")
        if choice == "0":
            return create_custom_recipe(inventory)
        if choice in ("1", "2", "3"):
            return recipes[int(choice)]
        print("Введите число от 0 до 3.")


def choose_payment():
    print("\nСпособ оплаты:")
    print("  1. Наличные")
    print("  2. Карта")

    while True:
        choice = input("Выберите (1-2): ")
        if choice == "1":
            return CashPayment(), "Наличные"
        if choice == "2":
            return CardPayment(), "Карта"
        print("Введите 1 или 2.")


def choose_discount(quantity: int) -> DiscountStrategy:
    if quantity >= 3:
        for min_qty, pct in DISCOUNT_RULES:
            if quantity >= min_qty:
                print(f"  Применена скидка {int(pct * 100)}% (от {min_qty} шт.)")
                return QuantityDiscount(DISCOUNT_RULES)
    return NoDiscount()


def create_order(
    ingredients: dict[str, Ingredient],
    inventory: Inventory,
    report: SalesReport,
    file_saver: FileOrderSaver,
):
    recipes = RecipeFactory.get_standard_recipes()
    items: list[OrderItem] = []

    while True:
        recipe = choose_recipe(recipes, ingredients, inventory)
        quantity = int(input("Введите количество: "))

        if not inventory.has_enough(recipe.ingredient_keys, quantity):
            print("\nНедостаточно ингредиентов!")
            low = [
                inventory.ingredients[k].name
                for k in recipe.ingredient_keys
                if inventory.stock.get(k, 0) < quantity
            ]
            print("Требуется закупить:", ", ".join(low))
            return

        items.append(OrderItem(recipe, quantity))
        more = input("Добавить ещё один вид хот-дога? (да/нет): ")
        if more.lower() == "нет":
            break

    total_qty = sum(item.quantity for item in items)
    discount = choose_discount(total_qty)

    payment_strategy, payment_type = choose_payment()
    order = Order(items, payment_type, discount)

    for item in items:
        inventory.reduce_stock(item.recipe.ingredient_keys, item.quantity)

    amount = order.total_price(ingredients)
    print(f"\n{payment_strategy.pay(amount)}")

    file_saver.save(order, ingredients)
    report.add_order(order, ingredients)

    print(f"\n{order.to_text(ingredients)}")


def main():
    ingredients = create_ingredients()
    stock = create_stock()
    inventory = Inventory(ingredients, stock)
    report = SalesReport()
    file_saver = FileOrderSaver()

    while True:
        show_menu()
        choice = input("Выберите пункт меню (1-4): ")

        if choice == "1":
            create_order(ingredients, inventory, report, file_saver)
        elif choice == "2":
            report.show()
        elif choice == "3":
            inventory.show()
        elif choice == "4":
            break
        else:
            print("Неверный ввод.")


if __name__ == "__main__":
    main()
