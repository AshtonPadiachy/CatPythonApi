# 🐾 Cat Breed Facts Searcher

This is a **Cat Breed Facts Searcher** program written in Python. It lets you search for information about various domestic cat breeds by querying the [API Ninjas Cat API](https://api-ninjas.com/api/cats). The program outputs fun facts like the cat’s origin, life expectancy, weight, length, health rating, and more.

---

## 📋 Features

✅ Search facts about popular domestic cat breeds  
✅ Displays breed name, origin, life expectancy, weight (in kg), and length  
✅ Provides a picture link of the cat  
✅ Shows ratings (0-5) for health, intelligence, friendliness, playfulness, and shedding  

---

## 🚀 How to Run

### 1️⃣ Clone or copy the code  
Save the Python script (e.g. `cat_searcher.py`).

### 2️⃣ Set up your environment  
It’s recommended to create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies  

```bash
pip install requests
```

### 4️⃣ Get an API key  
- Sign up at [API Ninjas](https://api-ninjas.com) and get your API key for the Cat API.

### 5️⃣ Run the script  

```bash
python cat_searcher.py
```

You’ll be prompted to type the name of a cat breed, for example:

```
Please type in the name of a domestic cat breed:
siamese
```

---

## ⚠️ Important  
➡ Replace `'yourspecialapikeymustbeputhere'` in the code with your actual API key:

```python
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
```

---

## 🐱 Example Breeds to Try  
- maine coon  
- ragdoll  
- sphynx cat  
- bombay cat  
- devon rex  
- persian  
- birman  
- exotic  
- abyssinian  
- siamese  
- turkish angora  

---

## 📌 Example Output  

```
name : Siamese
origins : Thailand
min life expectancy : 12 years
max life expectancy : 20 years
min weight: 4 kg
max weight: 6 kg
length : 15 inches
link to cat's picture : https://example.com/cat-image.jpg
general health: 4/5
intelligence: 5/5
family friendliness : 5/5
playfulness: 4/5
shedding: 2/5
```

---

## 🛠 Notes  

- The program converts weight from pounds to kilograms.
- The length is shown in inches as returned by the API.
- If the breed isn’t found or there’s an error, the program will print the error code and message (can be uncommented in the code).

---

## 📄 License  

This project is for educational and personal use. Please respect API Ninjas' [terms of use](https://api-ninjas.com/terms).
