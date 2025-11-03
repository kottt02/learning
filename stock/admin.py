from django.contrib import admin
from stock.models import (Stock, Currency, Account,
                          AccountCurrency, AccountStock)
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("ticker", "name", "description", "currency", "logo")

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass

# регистрация валютных и акционных активов
@admin.register(AccountCurrency)
class AccountCurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(AccountStock)
class AccountStockAdmin(admin.ModelAdmin):
    pass


# встроенные таблицы для отображения активов внутри аккаунта
class AccountCurrencyInline(admin.TabularInline):
    model = AccountCurrency


class AccountStockInline(admin.TabularInline):
    model = AccountStock


# регистрация модели учётной записи с вложенными таблицами
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    inlines = [AccountCurrencyInline, AccountStockInline]
