blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]

def display_inventory(inventory):
    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
    else:
        print("\n--- DANH SÁCH KHO MÁU ---")
        print(f"{'Mã Túi':<7} | {'Người Hiến':<16} | {'Nhóm Máu':<8} | {'Thể Tích':<8} | {'Ngày Hết Hạn'}")
        print("-" * 62)

        total_volume = 0
        for bag in inventory:
            parts = bag.split("-")
            if len(parts) == 6 and parts[3] == "":
                bag_id = parts[0]
                donor = parts[1]
                blood_type = parts[2] + "-"
                volume_str = parts[4]
                expiry = parts[5]
            elif len(parts) == 5:
                bag_id, donor, blood_type, volume_str, expiry = parts
        
            volume = int(volume_str)
            total_volume += volume

            print(f"{bag_id:<7} | {donor:<16} | {blood_type:<8} | {volume} ml   | {expiry}")
        print("-" * 62)
        print(f"Tổng thể tích máu trong kho: {total_volume} ml.")

def add_blood_bag(inventory):
    print("\n--- NHẬP TÚI MÁU MỚI ---")
    bag_id = input("Nhập mã túi máu mới: ").strip().upper()
    if bag_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return
    
    for bag in inventory:
        if bag.split("-")[0] == bag_id:
            print(f"\nLỗi: Mã túi máu {bag_id} đã tồn tại! Vui lòng nhập mã khác.")
            return
        
    donor = input("Nhập tên người hiến: ").strip().title()
    if donor == "":
        print("\nLỗi: Tên người hiến không được để trống!")
        return

    blood_type = input("Nhập nhóm máu: ").strip().upper()

    volume = input("Nhập thể tích (ml): ").strip()
    if not volume.isdigit() or int(volume) <= 0:
        print("\nLỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return
    
    expiry = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()

    new_bag_info = "-".join([bag_id, donor, blood_type, volume, expiry])
    inventory.append(new_bag_info)
    print(f"\nThành công: Đã nhập túi máu {bag_id} vào kho!")

def update_expiry(inventory):
    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")
    bag_id = input("Nhập mã túi máu cần cập nhật: ").strip().upper()
    if bag_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return
    
    found = -1
    for i in range(len(inventory)):
        if inventory[i].split("-")[0] == bag_id:
            found = i
            break

    if found == -1:
        print(f"\nLỗi: Không tìm thấy túi máu {bag_id} trong kho!")
        return
    
    expiry_new = input("Nhập ngày hết hạn mới: ").strip()

    parts = inventory[found].split("-")
    if len(parts) == 6:
        parts[5] = expiry_new  
    else:
        parts[4] = expiry_new  
        
    inventory[found] = "-".join(parts)
    print(f"\nThành công: Đã cập nhật ngày hết hạn cho túi máu {bag_id}!")

def remove_blood_bag(inventory):
    print("\n--- XUẤT / HỦY TÚI MÁU ---")
    bag_id = input("Nhập mã túi máu cần xuất/hủy: ").strip().upper()
    if bag_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return
    
    for bag in inventory:
        if bag.split("-")[0] == bag_id:
            inventory.remove(bag)
            print(f"\nThành công: Đã xuất túi máu {bag_id} khỏi kho!")
            return

    print(f"\nLỗi: Không tìm thấy túi máu {bag_id} trong kho!")

def main():
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
        print("1. Xem danh sách túi máu trong kho")
        print("2. Nhập túi máu mới")
        print("3. Gia hạn / Sửa ngày hết hạn")
        print("4. Xuất / Hủy túi máu")
        print("5. Thoát chương trình")
        print("========================================")
        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_inventory(blood_inventory)
        elif choice == "2":
            add_blood_bag(blood_inventory)
        elif choice == "3":
            update_expiry(blood_inventory)
        elif choice == "4":
            remove_blood_bag(blood_inventory)
        elif choice == "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")

if __name__ == "__main__":
    main()