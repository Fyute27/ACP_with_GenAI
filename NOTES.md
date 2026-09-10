# Smart AC Debugging Notes

## 1. Why did the `RecursionError` happen?

The line causing the error was:

```python
self.temperature = value
```

This calls the `temperature` setter again. The setter calls itself repeatedly, causing infinite recursion and eventually a `RecursionError`.

Changing it to:

```python
self._temperature = value
```

stores the value directly in the private variable. The setter does not call itself again, so the recursion stops.

## 2. Why did Bug 5 still allow `99`?

The constructor was directly storing the temperature:

```python
self._temperature = temperature
```

This bypassed the temperature setter and its validation rules. As a result, invalid values such as `99` were accepted.

The constructor should use the setter instead:

```python
self.temperature = temperature
```

This makes the constructor run the validation, so invalid temperatures are rejected.

## 3. Why should `is_energy_saving` be calculated each time?

The temperature can change after the AC object is created. If `is_energy_saving` is stored only once, its value can become outdated.

It should be calculated from the current temperature:

```python
return self.temperature >= 25
```

This always returns the correct result based on the current temperature.
