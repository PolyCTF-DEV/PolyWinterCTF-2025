from scapy.all import *

# Загружаем модифицированный трафик
packets = rdpcap("office_hacker.pcapng")

# Словарь для хранения частей сообщения и их порядковых номеров
hidden_parts = {}

# Проходим по всем пакетам
for i, packet in enumerate(packets):
    if TCP in packet and Raw in packet and Padding in packet:
        # Получаем данные из пакета
        raw_data = packet[Raw].load.decode(errors="ignore")
        # Ищем части сообщения (например, по формату "Poly", "CTF{", и т.д.)
        hidden_parts[i] = packet[Padding].load.decode(errors="ignore")  # Сохраняем часть с номером пакета

# Сортируем части по номеру пакета и собираем сообщение
hidden_message = "".join([hidden_parts[key] for key in sorted(hidden_parts.keys())])
print(f"Найденное скрытое сообщение: {hidden_message}")
