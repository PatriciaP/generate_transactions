import random
import datetime
import json

# Define the transaction categories
categories = {
    "expense": [
        "Academia",
        "Suplementos",
        "Manipulados",
        "Consultoria",
        "Supermercado",
        "Cinema",
        "Restaurante",
        "Gasolina",
        "Luz",
        "Água",
        "Educação",
        "Farmácia",
        "Transporte",
        "Conta telefônica",
        "Salão",
        "Viagem",
        "PetShop",
        "Entretenimento",
        "Vestuário",
        "Cuidados Pessoais",
        "Aluguel",
        "Manutenção do Lar",
        "Impostos",
        "Seguro",
        "Presentes",
        "Outros Gastos"
    ],
    "income": [
        "Salário",
        "Investimentos",
        "Renda Extra",
        "Reembolso",
        "Aluguel de Imóveis",
        "Bônus",
        "Prêmios",
        "Dividendos",
        "Horas Extras",
        "Vendas",
        "Outras Receitas"
    ]
}

# Generate random transactions
transactions = []
start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2023, 12, 31)
delta = end_date - start_date

transaction_count = 10000  # Values used for tests: 10, 100, 1000, 10000

for _ in range(transaction_count):
    random_date = start_date + datetime.timedelta(days=random.randint(0, delta.days))
    random_category = random.choice(list(categories.keys()))
    random_description = random.choice(categories[random_category])
    random_amount = random.randint(1, 1000)

    transaction = {
        "id": _ + 1,
        "description": random_description,
        "amount": random_amount,
        "date": random_date.strftime("%Y-%m-%d"),
        "type": random_category
    }
    transactions.append(transaction)

# Sort transactions by ascending date
sorted_transactions = sorted(transactions, key=lambda x: x["date"])

# Convert sorted transactions to JSON
transactions_json = json.dumps(sorted_transactions, indent=2, ensure_ascii=False)

# Save transactions to a file
file_name = f"data_{transaction_count}.json"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(transactions_json)

print(f"Transactions saved to {file_name}")
