# JustHost Test Assignment
Код выполненного тестового задания в JustHost от [waflawe](https://t.me/waflawe). Кодовая база соответствует стилистике [ruff](https://github.com/astral-sh/ruff). Выполнение задания включает:
- Само выполненное задание - разработан REST-сервис для управления VPS серверами с использованием DRF (создание нового сервера, чтение деталей по конкретному, чтение всех серверов с возможностью фильтровать их по характеристикам, обновление статуса сервера)
- Как перевыполнение:
- - **Docker'изация** - проект полностью Docker'изирован.
- - Возможность **удаления** серверов.
- - **Swagger документация** - сгенерирована к API через drf-spectacular.
- - **100-процентное** покрытие **тестами** с помощью pytest.

## Как установить и протестировать?
Убедитесь, что у вас установлен Docker и Git, а затем:
1. Склонируйте репозиторий:
```cmd
git clone https://github.com/wondererlie/justhost-assignment.git
cd justhost-assignment
```
2. Поднимите Docker-Compose:
```cmd
docker-compose up
```
3. Документацию к API можно найти на `http://localhost:8000/api/schema/docs/`, а все `endpoint`'ы доступны на `http://localhost:8000/api/vps/`.
