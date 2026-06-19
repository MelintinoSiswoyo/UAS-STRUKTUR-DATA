#Melintino Siswoyo
#25416255201001
#IF25F

import csv
from collections import deque

# ===== Struktur Data =====
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def remove(self, item):
        current = self.head
        prev = None
        while current:
            if current.item == item:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def display(self):
        current = self.head
        while current:
            print(current.item)
            current = current.next

# ===== Stack untuk History =====
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, action):
        self.stack.append(action)
    
    def pop(self):
        return self.stack.pop() if self.stack else None

# ===== Queue untuk Pertarungan =====
class BattleQueue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, enemy):
        self.queue.append(enemy)
    
    def dequeue(self):
        return self.queue.popleft() if self.queue else None

# ===== Database CSV =====
CSV_FILE = "game_data.csv"

def load_data():
    data = []
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data

def save_data(data):
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ["id", "name", "hp", "xp"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# ===== CRUD =====
def create_character(data):
    char_id = input("Masukkan ID: ")
    name = input("Masukkan Nama: ")
    hp = input("Masukkan HP: ")
    xp = input("Masukkan XP: ")
    data.append({"id": char_id, "name": name, "hp": hp, "xp": xp})
    save_data(data)

def read_characters(data):
    for d in data:
        print(d)

def update_character(data):
    char_id = input("Masukkan ID karakter yang ingin diupdate: ")
    for d in data:
        if d["id"] == char_id:
            d["name"] = input("Nama baru: ")
            d["hp"] = input("HP baru: ")
            d["xp"] = input("XP baru: ")
            save_data(data)
            return
    print("Karakter tidak ditemukan.")

def delete_character(data):
    char_id = input("Masukkan ID karakter yang ingin dihapus: ")
    for d in data:
        if d["id"] == char_id:
            data.remove(d)
            save_data(data)
            return
    print("Karakter tidak ditemukan.")

# ===== Main Menu =====
def main():
    data = load_data()
    inventory = LinkedList()
    history = Stack()
    battle = BattleQueue()

    while True:
        print("\n=== Game Adventure ===")
        print("1. Tambah Karakter")
        print("2. Lihat Karakter")
        print("3. Update Karakter")
        print("4. Hapus Karakter")
        print("5. Tambah Item ke Inventori")
        print("6. Lihat Inventori")
        print("7. Pertarungan Musuh")
        print("8. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            create_character(data)
            history.push("Tambah Karakter")
        elif choice == "2":
            read_characters(data)
        elif choice == "3":
            update_character(data)
            history.push("Update Karakter")
        elif choice == "4":
            delete_character(data)
            history.push("Hapus Karakter")
        elif choice == "5":
            item = input("Masukkan nama item: ")
            inventory.add(item)
            history.push(f"Tambah Item {item}")
        elif choice == "6":
            inventory.display()
        elif choice == "7":
            enemy = input("Masukkan nama musuh: ")
            battle.enqueue(enemy)
            print(f"Musuh {enemy} masuk ke antrian pertarungan.")
            fight = battle.dequeue()
            print(f"Melawan {fight}!")
        elif choice == "8":
            print("Keluar dari game...")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
