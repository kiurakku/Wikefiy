# Wikefiy - WiFi Password Tools

Набір інструментів для роботи з WiFi паролями на Windows.

## 🚀 Швидкий старт

### Найшвидший спосіб отримати пароль

```bash
python wifi-fast.py "TP-Link_284_5G"
```

Це перевірить збережені паролі в Windows і створить файл `TP-Link_284_5G.txt` з паролем.

## 📦 Встановлення

### Вимоги

- Python 3.7+
- Windows (для більшості скриптів)
- Права адміністратора (рекомендовано)

### Встановлення залежностей

```bash
pip install -r requirements.txt
```

## 🛠️ Скрипти

### 1. `wifi-fast.py` - Найшвидший спосіб

Простий скрипт для отримання збереженого пароля:

```bash
python wifi-fast.py "SSID"
```

**Що робить:**
- Перевіряє збережені WiFi профілі в Windows
- Створює файл `SSID.txt` з паролем
- Працює миттєво для мереж, до яких ви вже підключалися

### 2. `wifi-brute-python.py` - Підбір паролів

Скрипт для підбору паролів через pywifi:

```bash
python wifi-brute-python.py -ssid "SSID" -dict "password-dictionary.txt"
```

**Параметри:**
- `-ssid, --ssid` - Назва WiFi мережі (обов'язково)
- `-dict, --dictionary` - Шлях до словника (за замовчуванням: password-dictionary.txt)
- `-d, --delay` - Затримка між спробами в секундах (за замовчуванням: 1.0)
- `-i, --interface` - Індекс WiFi адаптера (за замовчуванням: 0)

### 3. PowerShell скрипти

#### `wifi-connect.ps1` - Підбір зі словника

```powershell
.\wifi-connect.ps1 -SSID "TP-Link_284_5G"
```

#### `wifi-brute.ps1` - Розумна генерація паролів

```powershell
.\wifi-brute.ps1 -SSID "TP-Link_284_5G"
```

#### `wifi-show-passwords.ps1` - Всі збережені паролі

```powershell
.\wifi-show-passwords.ps1
```

#### `wifi-get-password.ps1` - Пароль конкретної мережі

```powershell
.\wifi-get-password.ps1 -SSID "TP-Link_284_5G"
```

## 📝 Структура проєкту

```
Wikefiy/
├── README.md                    # Цей файл
├── requirements.txt              # Python залежності
├── password-dictionary.txt      # Словник паролів
├── wifi-fast.py                 # Найшвидший спосіб (Python)
├── wifi-brute-python.py         # Підбір паролів (Python)
├── wifi-connect.ps1              # Підбір зі словника (PowerShell)
├── wifi-brute.ps1               # Розумна генерація (PowerShell)
├── wifi-show-passwords.ps1      # Всі паролі (PowerShell)
└── wifi-get-password.ps1       # Один пароль (PowerShell)
```

## ⚠️ Важливо

**Використовуйте тільки для легальних цілей:**
- Тестування власних мереж
- Відновлення забутих паролів
- Дозволені пентести

**Не використовуйте для:**
- Доступу до чужих мереж без дозволу
- Незаконних дій

## 🔧 Відомі проблеми

1. **"No module named 'comtypes'"** - Встановіть: `pip install comtypes`
2. **"No WiFi adapter found"** - Перевірте, чи WiFi адаптер активний
3. **"Permission denied"** - Запустіть від імені адміністратора
4. **Підключення не працює** - Деякі адаптери потребують Compatibility Mode

## 📄 Ліцензія

MIT License - використовуйте вільно для особистих та комерційних цілей.

## ✅ Тестування

Локально або в CI:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## 🤝 Внесок

Вітаються pull requests та issues!

## 📧 Контакти

Створено для навчальних цілей.
