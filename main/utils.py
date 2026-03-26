# main/utils.py
import random
from .models import SeedForce, Mission, WisdomTip, CodeExample

class SeedManager:
    """Управление силой Семени"""
    
    @staticmethod
    def get():
        """Получить объект силы"""
        return SeedForce.get_instance()
    
    @staticmethod
    def get_value():
        """Получить текущее значение силы"""
        return SeedForce.get_instance().value
    
    @staticmethod
    def add(amount):
        """Увеличить силу на amount"""
        seed = SeedForce.get_instance()
        seed.increase(amount)
        return seed.value
    
    @staticmethod
    def reduce(amount):
        """Уменьшить силу на amount (не ниже 0)"""
        seed = SeedForce.get_instance()
        seed.decrease(amount)
        return seed.value

class AbilityManager:
    """Управление способностями"""
    
    @staticmethod
    def add_mission():
        """Добавить запись о битве"""
        return Mission.objects.create(
            title='Поток коммитов',
            description='Баг смыт потоком коммитов'
        )
    
    @staticmethod
    def get_random_code():
        """Получить случайный пример кода"""
        examples = CodeExample.objects.all()
        return random.choice(examples) if examples else None
    
    @staticmethod
    def get_random_tip():
        """Получить случайный совет"""
        tips = WisdomTip.objects.all()
        return random.choice(tips) if tips else None