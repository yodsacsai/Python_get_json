class getjson:
    json_data = []
    key = 0
    
    def __init__(self,key,json_data) -> None:
        self.json_data = json_data
        self.key = key
        if key == 1:
            print("เรียกดูข้อมูล JSON ทั้งหมด")
            for data in json_data:
                print('ID: ' ,data['id'])
                print('Name: ' ,data['name'])
                print('Email: ' ,data['email'])
                print('Phone: ' ,data['phone'])
                print('=====================')
        elif key == 2:
            x = int(input('ใส่หมายเลขไอดี(1-10) : '))
            print("ข้อมูล JSON รายการที่ ",x)
            print('ID: ' ,json_data[x-1]['id'])
            print('Name: ' ,json_data[x-1]['name'])
            print('Email: ' ,json_data[x-1]['email'])
            print('Phone: ' ,json_data[x-1]['phone'])
            print('=====================')
        else:
            print('คุณใส่หมายเลขไม่ถูกต้อง')