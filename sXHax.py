import os

sXHax = "sXHax"

try:
   os.mkdir(sXHax)
   print(f"Pasta '{sXHax}' criada com sucesso!")
except FileExistsError:
    print(f"A pasta '{sXHax}' já existe.")
