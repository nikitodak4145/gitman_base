from django.shortcuts import render, redirect
from .models import Skill, Mission, ContactMessage, CodeExample, WisdomTip
from .utils import SeedManager, AbilityManager
import random, time, json
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator

"""
Вьюхи для сайта "Хранитель Семени"
- index — главная страница, управление силой
- abilities — страница способностей
- missions — лог битв
- contact — форма обратной связи
- API для Telegram-бота
"""

def index(request):
    seed = SeedManager.get()
    last_decrease = request.session.get('last_decrease', 0)
    now = time.time()
    
    if now - last_decrease > 10:
        if seed.value > 0:
            SeedManager.reduce(1)
        request.session['last_decrease'] = now
    
    if request.method == 'POST':
        SeedManager.add(10)
        return redirect('index')
    
    # Дополнительная статистика
    total_battles = Mission.objects.count()
    random_tip = AbilityManager.get_random_tip()
    
    context = {
        'seed_force': SeedManager.get_value(),
        'total_battles': total_battles,
        'random_tip': random_tip.text if random_tip else "Пока нет советов. Добавь в админке!"
    }
    return render(request, 'main/index.html', context)

def decrease_seed(request):
    """
    API-эндпоинт для уменьшения силы (используется Telegram-ботом)
    POST-запрос -> уменьшает силу на 1, возвращает новое значение
    """
    if request.method == 'POST':
        new_value = SeedManager.reduce(1)
        return JsonResponse({'success': True, 'new_value': new_value})
    return JsonResponse({'success': False}, status=400)


def increase_seed(request):
    """
    API-эндпоинт для увеличения силы (используется Telegram-ботом)
    POST-запрос -> увеличивает силу на 10, возвращает новое значение
    """
    if request.method == 'POST':
        new_value = SeedManager.add(10)
        return JsonResponse({'success': True, 'new_value': new_value})
    return JsonResponse({'success': False}, status=400)


def skills(request):
    """
    Страница навыков героя.
    Выводит все навыки из базы данных.
    """
    skills = Skill.objects.all()
    return render(request, 'main/skills.html', {'skills': skills})


def missions(request):
    """
    Страница лога битв.
    - GET: показывает все битвы (сортировка по дате)
    - POST: добавляет новую битву из формы
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            Mission.objects.create(
                title=title,
                description=description
            )
        return redirect('missions')
    
    missions_list = Mission.objects.all().order_by('-date')
    paginator = Paginator(missions_list, 5)  # 5 записей на страницу
    page_number = request.GET.get('page')
    missions = paginator.get_page(page_number)
    
    return render(request, 'main/missions.html', {'missions': missions})
    

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        captcha = request.POST.get('captcha')
        
        if captcha != '4':
            return render(request, 'main/contact.html', {'error': 'Капча неверна!'})
        
        if name and message:
            ContactMessage.objects.create(name=name, message=message)
        return HttpResponse("Сообщение отправлено! <a href='/'>На главную</a>")
    return render(request, 'main/contact.html')

def contact_success(request):
    """
    Страница после успешной отправки сообщения.
    """
    return render(request, 'main/contact_success.html')


def abilities(request):
    """
    Страница способностей.
    Берёт случайный пример кода из базы для способности "Взгляд чистоты".
    """
    example = AbilityManager.get_random_code()
    return render(request, 'main/abilities.html', {'example': example})


def add_mission(request):
    """
    API-эндпоинт для добавления битвы (используется способностью "Поток коммитов").
    POST-запрос -> создаёт новую запись в Mission.
    """
    Mission.objects.create(
        title='Поток коммитов',
        description='Баг смыт потоком коммитов'
    )
    return JsonResponse({'success': True})

def get_tip(request):
    """
    API-эндпоинт для получения случайного совета (способность "Семя знаний").
    GET-запрос -> возвращает JSON с текстом совета.
    """
    if request.method == 'GET':
        tip = AbilityManager.get_random_tip()
        if tip:
            return JsonResponse({'tip': tip.text})
        return JsonResponse({'tip': 'Пока нет советов. Добавь их в админке!'})
    return JsonResponse({'error': 'Неверный метод'}, status=400)


def api_missions(request):
    """
    API для Telegram-бота.
    Возвращает список всех битв в формате JSON (название, дата).
    """
    missions = Mission.objects.all().order_by('-date').values('title', 'date')
    return JsonResponse(list(missions), safe=False)


def api_seed(request):
    """
    API для Telegram-бота.
    Возвращает текущее значение силы Семени.
    """
    return JsonResponse({'value': SeedManager.get().value})