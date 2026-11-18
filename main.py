from app import app, get_db_connection
from database import init_db

if __name__ == '__main__':
    init_db()
    print("[*] Khởi tạo cơ sở dữ liệu thành công!")
    print("[*] Đang khởi chạy hệ thống SafeGuard AI...")
    app.run(host='0.0.0.0', port=5000, debug=True)
    