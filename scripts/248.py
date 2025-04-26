from utils.totient import inverse_totient
from utils.factorial import factorial

print(inverse_totient(factorial(13))[150_000 - 1])