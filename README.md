# Sorting-by-minimum-elements
## Как это работает?
Сортировка по минимальным элементам работает следующим образом. Из списка берётся самое маленькое число. Дальше это число добавляется в новый список, а из старого удаляется. Вот пример работы алгоритма со списком [3, 1, 5, 2, 4]:
```python
a = []; arr = [3, 1, 5, 2, 4]
a = [1]; arr = [3, 5, 2, 4]
a = [1, 2]; arr = [3, 5, 4]
a = [1, 2, 3]; arr = [5, 4]
a = [1, 2, 3, 4]; arr = [5]
a = [1, 2, 3, 4, 5]; arr = []
```
Время выполнения этой сортировки всегда будет O(n)

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Coquettec&duration=3000&pause=3000&color=FFDB4F&background=FFFFFF00&center=true&vCenter=true&width=600&lines=%D0%9C%D0%BE%D0%B6%D0%B5%D1%88%D1%8C+%D0%BF%D0%BE%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C+%D1%81+%D0%BA%D0%BE%D0%B4%D0%BE%D0%BC)](https://git.io/typing-svg)