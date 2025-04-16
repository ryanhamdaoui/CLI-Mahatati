# 🚌  CLI Mahatati

**CLI Mahatati** is a simple Python CLI tool for searching **live intercity bus departures in Algeria** using an unofficial **SOGRAL Mahatati API**.

You can search by **city ZIP codes or names**, and the tool fetches bus trips for **today and tomorrow**, displaying time, route, license plate, bus name, and price.

---

## ✨ Features

- ✅ Fetches live departure data using the Mahatati API
- 🗕️ Automatically includes both **today and tomorrow’s** trips
- 🔍 Search by **city ZIP codes** via command-line arguments
- 🧠 Built-in mapping from **city names to full 12-digit codes**
- 📆 Clean output with bus time, name, route, license plate, and fare

---

## 💠 Usage

### 1. Using ZIP code arguments

```bash
python script.py <departure_zip> <destination_zip>
```

#### Example:

```bash
python script.py 16000 45002
```

This will search for trips from **Alger** (ZIP: `16000`) to **Mecheria** (ZIP: `45002`).


---

## 📟 Sample Output

```
Bus 1:
  Date          : Wednesday, 17 April 2025
  Time          : 10:00:00
  License Plate : 000010-424-16
  Bus Name      : BOUCHENEB NOUREDDINE
  Route         : BECHAR
  Price         : 1160 DZD
----------------------------------------
```

---

## 📆 Requirements

- Python 3.6+
- `requests` module

Install dependencies with:

```bash
pip install requests
```

---

## 🏩 City Code Reference

City-to-code mappings are based on official ZIP codes. You can expand your internal city dictionary using public resources:

- 📍 [MapsofWorld - Algeria Postal Codes](https://www.mapsofworld.com/postal-codes/country-algeria.html)
- 📍 [Wikipedia - Liste des codes postaux d'Algérie](https://fr.wikipedia.org/wiki/Liste_des_codes_postaux_d%27Alg%C3%A9rie)
- 📍 [DataHub Postal Codes Dataset](https://datahub.io/logistics/postal-codes-dz)

Example ZIP mappings used:

| City      | ZIP Code Fragment | Full Code         |
|-----------|-------------------|-------------------|
| Alger     | 16000             | 213-000016000     |
| Mecheria  | 45002             | 213-000045002     |
| Naama     | 45000             | 213-000045000     |

---

## 📄 License

This is an **unofficial** project and is not affiliated with **SOGRAL** or the **Mahatati** platform.  
For personal or educational use only.

---

## 🚀 Future Ideas

- City name autocompletion
- Interactive terminal UI
- Save favorite routes
- HTML or CSV export

