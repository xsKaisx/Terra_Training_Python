class BankAccount:
  def set_details(self):
    self.ten = input('Nhập tên của bạn: ')
    self.sodu = 0
    print ('Tên: {} --- Số dư: {}'.format(self.ten, self.sodu))
    print('')
  def rut_tien(self):
    try:
        self.rut = int(input('Bạn muốn rút bao nhiêu tiền: '))
        if self.rut > self.sodu:
            print('Tài khoản của bạn không có đủ tiền để rút!!!')
        elif self.rut == 0:
            print('Bạn có rút tiền không???')
        else:
            self.sodu = self.sodu - self.rut
            print('{} đã được rút từ tài khoản của bạn. Số dư còn lại của bạn là {}'.format(self.rut, self.sodu))
            print('')
    except:
        print('Nhập lại số!!!')
  def gui_tien(self):
    try:
        self.gui = int(input('Bạn muốn gửi bao nhiều tiền: '))
        if self.gui == 0:
            print('Bạn có gửi tiền không???')  
        else:
            self.sodu = self.sodu + self.gui
            print('{} đã được gửi vào tài khoản của bạn. Số dư còn lại của bạn là {}'.format(self.gui, self.sodu))
            print('')
    except:
        print('Please enter a number')
  def hien_thi(self):
    print('Tên tài khoản: {}'.format(self.ten))
    print('Số dư còn lại của bạn là {}'.format(self.sodu))
    print('')

def start():
  s = BankAccount()
  s.set_details()
  while 1:
    print('Chào {} đã đến với ngân hàng của chúng tôi'.format(s.ten))
    print('''    Nhâp r nếu bạn muốn rút tiền.
    Nhập g nếu bạn muốn gửi tiền.
    Nhập h nếu bạn muốn hiển thị thông tin.
    Nhập q nếu bạn muốn kết thúc giao dịch. ''')
    res = input('Nhập: ')
    if res == 'r':
      s.rut_tien()
    elif res == 'g':
      s.gui_tien()
    elif res == 'h':
      s.hien_thi()
    elif res == 'q':
      break
    else:
      print('Nhập lại giá trị chính xác!!!')

start()
