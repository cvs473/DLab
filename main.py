NUM_LEN = 256

class MyBigInt:
    def __init__(self):
        pass

    def setHex(self, hex_num: str): 
        self.arr = [0] * NUM_LEN
        if len(hex_num) > NUM_LEN:
            return 0
        else:
            for i in range(len(hex_num)):
                self.arr[i] = int(hex_num[len(hex_num)-1-i], 16)
            return self.arr 


    def getHex(self):
        self.hex = map(hex, self.arr)
        list_1 = list(self.hex)
        for i in range(len(list_1)):
            list_1[i] = list_1[i].replace('0x', '')
        str_1 = ''.join(list_1)
        str_2 = str_1[::-1]
        return str_2.lstrip('0')
        

    def getArr(self):
        print(self.arr) 

    def inv(self):
        inverted_num = MyBigInt()
        inverted_arr = []
        flag = 0
        for i in range(len(self.arr)):
            if self.arr[(len(self.arr) - 1 - i)] == 0:
                flag += 1
            else: break

        for el in range(len(self.arr) - flag): 
            bit_str = format(self.arr[el], "b").zfill(4)
            inverse_str = ''
            for i in bit_str:
                if i == '0':
                    inverse_str += '1'
                else:
                    inverse_str += '0' 
            inverted_arr.append(int(inverse_str, 2))
        inverted_num.arr = inverted_arr 
        return inverted_num.getHex()

    def len(self):
        return(len(self.arr))

    @staticmethod
    def xor(first, second):
        new_number = MyBigInt()
        xored_arr = []
        first_num = MyBigInt()
        first_num.setHex(first)
        second_num = MyBigInt()
        second_num.setHex(second)
        for i in range(len(first_num.arr)):
            xored_arr.append(first_num.arr[i] ^ second_num.arr[i])
        new_number.arr = xored_arr
        return new_number
   
    @staticmethod
    def bit_or(first, second):
        new_number = MyBigInt()
        or_arr = []
        first_num = MyBigInt()
        first_num.setHex(first)
        second_num = MyBigInt()
        second_num.setHex(second)
        for i in range(len(first_num.arr)):
            or_arr.append(first_num.arr[i] | second_num.arr[i])
        new_number.arr = or_arr
        return new_number

    @staticmethod
    def bit_and(first, second):
        new_number = MyBigInt()
        or_arr = []
        first_num = MyBigInt()
        first_num.setHex(first)
        second_num = MyBigInt()
        second_num.setHex(second)
        for i in range(len(first_num.arr)):
            or_arr.append(first_num.arr[i] & second_num.arr[i])
        new_number.arr = or_arr
        return new_number
    
    def shiftL(self, n: int):
        hex_str = self.getHex()
        bin_str = ''.join(['{0:04b}'.format(int(d, 16)) for d in hex_str])
        print(bin_str)
        bin_arr = list(bin_str)
        bin_arr2 = [0] * len(bin_str)
        for i in range(len(bin_arr)):
            if (i - n) < 0:
                continue
            else:
                bin_arr2[i-n] = bin_arr[i]
        s = [str(i) for i in bin_arr2]
        bin_str2 = ''.join(s)
        res_hex_str = ""
        new_number = MyBigInt()
        for i in range(0, len(bin_str2), 4):
            bin_n = bin_str2[i:i+4]
            num = int(bin_n, 2) 
            res_hex_str += format(num, 'x')
        return res_hex_str

    def shiftR(self, n: int):
        hex_str = self.getHex()
        bin_str = ''.join(['{0:04b}'.format(int(d, 16)) for d in hex_str])
        print(bin_str)
        bin_arr = list(bin_str)
        bin_arr2 = [0] * len(bin_str)
        for i in range(len(bin_arr)-n):
            bin_arr2[i+n] = bin_arr[i]
        s = [str(i) for i in bin_arr2]
        bin_str2 = ''.join(s)
        res_hex_str = ""
        new_number = MyBigInt()
        for i in range(0, len(bin_str2), 4):
            bin_n = bin_str2[i:i+4]
            num = int(bin_n, 2) 
            res_hex_str += format(num, 'x')
        return res_hex_str
    
    def __add__(self, other):
        new_num = MyBigInt()
        carry = 0
        arr = [0]*NUM_LEN
        for i in range(NUM_LEN):
            tmp = self.arr[i] + other.arr[i] + carry
            arr[i] = tmp % 16
            carry = tmp // 16
        new_num.arr = arr 
        return new_num

    def __sub__(self, other):
        new_num = MyBigInt()
        borrow = 0
        arr = [0]*NUM_LEN
        for i in range(NUM_LEN):
            tmp = self.arr[i] - other.arr[i] - borrow
            if tmp >= 0:
                arr[i] = tmp
                borrow = 0
            else:
                arr[i] = tmp + 16
                borrow = 1
        new_num.arr = arr 
        return new_num


if __name__ == '__main__':
    test_xor1 = "51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4"     
    test_xor2 = "403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c"     
    test_xor_res = "1182d8299c0ec40ca8bf3f49362e95e4ecedaf82bfd167988972412095b13db8" 
    print(MyBigInt.xor(test_xor1, test_xor2).getHex() == test_xor_res)

    test_add1 = "36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80"     
    test_add2 = "70983d692f648185febe6d6fa607630ae68649f7e6fc45b94680096c06e4fadb"
    numA = MyBigInt()
    numB = MyBigInt()
    numA.setHex(test_add1)
    numB.setHex(test_add2)
    test_add_res = "a78865c13b14ae4e25e90771b54963ee2d68c0a64d4a8ba7c6f45ee0e9daa65b" 
    print((numA + numB).getHex() == test_add_res)
    
    test_sub1= "33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc"     
    test_sub2= "22e962951cb6cd2ce279ab0e2095825c141d48ef3ca9dabf253e38760b57fe03"
    numA = MyBigInt()
    numB = MyBigInt()
    numA.setHex(test_sub1)
    numB.setHex(test_sub2)
    test_sub_res = "10e570324e6ffdbc6b9c813dec968d9bad134bc0dbb061530934f4e59c2700b9" 
    print((numA - numB).getHex() == test_sub_res)
