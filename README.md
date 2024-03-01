
```python
Приклад 1:
piles = `[3,6,7,11]`, 
H = 8  
Результат: 
4  

Приклад 2:
piles = `[30,11,23,4,20]`,
H = 5  
Результат: 
30  
  
Приклад 3:
piles = `[30,11,23,4,20]`,
H = 6  
Результат: 
23

Важливо:
1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= `piles[i]` <= 10^9
```
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити роботу вашої функції на прикладах, наведених вище
## Рівень 3

### Варіант 1

Зоомагазин займається продажем хом’ячкiв. Це мирнi домашнi iстоти, проте, як
виявилося, вони мають цiкаву харчову поведiнку.
Для того, щоб прогодувати хом’ячка, який живе наодинцi, потрiбно H пакетiв корму
на день. Однак, якщо кiлька хом’ячкiв живуть разом, у них прокидається жадiбнiсть.
У такому випадку кожен хом’ячок з’їдає додатково G пакетiв корму в день за
кожного сусiда. Денна норма H та жадiбнiсть G є iндивiдуальними для кожного
хом’ячка.
Всього в магазинi є C хом’ячкiв. Ви бажаєте придбати якомога бiльше, проте у вас
є всього S пакетiв їжi на день. Визначте максимальну кiлькiсть хом’ячкiв, яку ви
можете прогодувати.

Реалізуйте функцію, яка поверне число - максимальне число хо
