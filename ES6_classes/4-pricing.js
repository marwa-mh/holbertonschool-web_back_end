import Currency from "./3-currency";

export default class Pricing {
    constructor(amount, currency) {
        this.validateAndAssignAmount(amount);
        this.validateAndAssignCurrency(currency);
    }

    get amount() {
        return this._amount;
    }

    set amount(amount) {
        this.validateAndAssignAmount(amount);
    }

    get currency() {
        return this._currency;
    }

    set currency(currency) {
        this.validateAndAssignCurrency(currency);
    }

    validateAndAssignAmount(amount) {
      if (typeof amount === 'number') {
      this._amount = amount;
    } else {
      throw new TypeError('amount must be a number');
    }
    }

    validateAndAssignCurrency(currency) {
      if (currency instanceof Currency) {
      this._currency = currency;
    } else {
      throw new TypeError('currency must be a Currency');
    }
    }

    displayFullPrice() {
        return `${this._amount} ${this._currency.displayFullCurrency()}`;
    }

    static convertPrice(amount, conversionRate) {
        return amount * conversionRate;
    }
}
