import random
import string


def generate_passwords(N, K):
    passwords = set()  # используем множество для хранения уникальных паролей

    while len(passwords) < N:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=K))
        passwords.add(password)

    return passwords


N = int(input("Введите количество паролей: "))
K = int(input("Введите длину пароля: "))

generated_passwords = generate_passwords(N, K)

print(f"{N} различных паролей длиной {K} символов:")
for password in generated_passwords:
    print(password)
