import allure
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selene.support import by
from selene.support.conditions import be


def test_github_issues_with_dry_selene():
    browser.open('https:/github.com')
    s('.header-search-input').send_keys('eroshenkoam/allure-example').press_enter()
    s(by.link_text('eroshenkoam/allure-example')).click()
    s('#issues-tab').click()
    s(by.partial_text('#76')).should(be.visible)


def test_github_issues_with_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https:/github.com')
    with allure.step('Ищем репозиторий'):
        s('.header-search-input').send_keys('eroshenkoam/allure-example').press_enter()
    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()
    with allure.step('Открываем таб issues'):
        s('#issues-tab').click()
    with allure.step('Проверяем наличие Issue с номером 76'):
        s(by.partial_text('#76')).should(be.visible)


def test_github_issues_with_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('76')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https:/github.com')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').send_keys(repo).press_enter()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем таб issues')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Проверяем наличие Issue с номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(f'#{number}')).should(be.visible)
