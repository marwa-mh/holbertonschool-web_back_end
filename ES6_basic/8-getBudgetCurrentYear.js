function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const income1 = `income-${getCurrentYear()}`;
  const gdp1 = `gdp-${getCurrentYear()}`;
  const capita1 = `capita-${getCurrentYear()}`;
  const budget = {
    [income1]: income,
    [gdp1]: gdp,
    [capita1]: capita,
  };

  return budget;
}
