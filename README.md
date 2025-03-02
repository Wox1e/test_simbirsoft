# Описание

UI-автотесты по тест-кейсу ниже

# Кейс:

1. Заполнить поле *Name*
2. Заполнить поле *Password*
3. Из списка *What is your favorite drink?* выбрать *Milk* и *Coffee*
4. Из списка *What is your favorite color?* выбрать *Yellow*
5. В поле *Do you like automation?* выбрать любой вариант
6. Поле *Email* заполнить строкой формата *name@example.com*
7. В поле *Message* написать количество инструментов, описанных в пункте *Automation tools*
8. В поле *Message* дополнительно написать инструмент из списка *Automation tools*, содержащий
наибольшее количество символов
9. Нажать на кнопку *Submit*

# Ожидаемый результат:
Появился алерт с текстом *Message received!*
  

# Запуск

1) Установка репозитория

```
git clone https://github.com/Wox1e/test_simbirsoft
```
2) Запуск автотестов 
```
   cd test_simbirsoft
   pip install -r requirements.txt
   cd src
   python main.py
```
**Примечание**
Если вам необходимо использовать драйвер, отличный от ChromeWebDriver, загрузите его в папку drivers
и укажите путь к нему в init.py:

```
# init.py

service = Service(executable_path="../drivers/*имя файла*")
driver = webdriver.*Драйвер*(service = service)
```
* Драйвер должен поддерживаться Selenium! 

<br /><br />
