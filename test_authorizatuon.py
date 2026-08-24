import os
from selene import browser, have, be


def test_authorization():
    url = "https://app.leantech.ai/profile"

    browser.open(url)
    browser.element('[class="ref-anon__cta"]').click()
    browser.element('[type="email"]').type('5--@mail.ru')
    browser.element('[type="password"]').type('555@mail.ru')
    browser.element('[class="ui-check__box"]').click()
    browser.element('[class="ui-btn ui-btn--primary ui-btn--l ui-btn--block"]').click()
    browser.element('[class="prof-kpi__val"]').with_(timeout=10).should(have.text('100'))
    browser.element('[class="page__head prof-head"]').with_(timeout=10).should(have.text('mail.ru'))