NUM_LEN = 256

class MyBigInt:
    def __init__(self, hex_num: str):
        self.arr = [0] * NUM_LEN
        if len(hex_num) > NUM_LEN:
            return 0
        else:
            for i in range(len(hex_num)):
                self.arr[i] = int(hex_num[len(hex_num)-1-i], 16)


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
        inverted_num = MyBigInt("")
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

    @staticmethod
    def xor(first, second):
        new_number = MyBigInt("")
        xored_arr = []
        first_num = MyBigInt(first)
        second_num = MyBigInt(second)
        for i in range(len(first_num.arr)):
            xored_arr.append(first_num.arr[i] ^ second_num.arr[i])
        new_number.arr = xored_arr
        return new_number
   
    @staticmethod
    def bit_or(first, second):
        new_number = MyBigInt("")
        or_arr = []
        first_num = MyBigInt(first)
        second_num = MyBigInt(second)
        for i in range(len(first_num.arr)):
            or_arr.append(first_num.arr[i] | second_num.arr[i])
        new_number.arr = or_arr
        return new_number

    @staticmethod
    def bit_and(first, second):
        new_number = MyBigInt("")
        or_arr = []
        first_num = MyBigInt(first)
        second_num = MyBigInt(second)
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
        for i in range(0, len(bin_str2), 4):
            bin_n = bin_str2[i:i+4]
            num = int(bin_n, 2) 
            res_hex_str += format(num, 'x')
        return res_hex_str

    def shiftR(self, n: int):
        hex_str = self.getHex()
        bin_str = ''.join(['{0:04b}'.format(int(d, 16)) for d in hex_str])
        bin_arr = list(bin_str)
        bin_arr2 = [0] * len(bin_str)
        for i in range(len(bin_arr)-n):
            bin_arr2[i+n] = bin_arr[i]
        s = [str(i) for i in bin_arr2]
        bin_str2 = ''.join(s)
        res_hex_str = ""
        for i in range(0, len(bin_str2), 4):
            bin_n = bin_str2[i:i+4]
            num = int(bin_n, 2) 
            res_hex_str += format(num, 'x')
        return res_hex_str
    
    def __add__(self, other):
        new_num = MyBigInt("")
        carry = 0
        arr = [0]*NUM_LEN
        for i in range(NUM_LEN):
            tmp = self.arr[i] + other.arr[i] + carry
            arr[i] = tmp % 16
            carry = tmp // 16
        new_num.arr = arr 
        return new_num

    def __sub__(self, other):
        new_num = MyBigInt("")
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
    
    @staticmethod 
    def karatsuba_mul(num1, num2):
        print(num1.getHex(), num2.getHex())
        if len(num2.getHex()) == 1: 
            return num1.one_digit_mul(num2.arr[0])

        elif len(num1.getHex()) == 1: 
            return num2.one_digit_mul(num1.arr[0])
        
        num1_len = len(num1.getHex())
        num2_len = len(num2.getHex())
        n = max(num1_len, num2_len)
        half = round(n/2)
        if len(num2.getHex()) == 2 and len(num1.getHex()) != 2 : 
            rem1 = MyBigInt(num1.getHex()[half :])
            rem2 = MyBigInt(num2.getHex()[1])
            num2 = MyBigInt(num2.getHex()[0])
            num1 = MyBigInt(num1.getHex()[: half])

        elif len(num2.getHex()) == 2 and len(num1.getHex()) == 2 : 
            rem2 = MyBigInt(num2.getHex()[1])
            rem1 = MyBigInt(num1.getHex()[1])
            num2 = MyBigInt(num2.getHex()[0])
            num1 = MyBigInt(num1.getHex()[0])
        elif len(num2.getHex()) != 2 and len(num1.getHex()) == 2 : 
            rem1 = MyBigInt(num1.getHex()[1])
            rem2 = MyBigInt(num2.getHex()[half :])
            num2 = MyBigInt(num2.getHex()[: half])
            num1 = MyBigInt(num1.getHex()[0])
        else:
            rem2 = MyBigInt(num2.getHex()[half :])
            rem1 = MyBigInt(num1.getHex()[half :])
            num1 = MyBigInt(num1.getHex()[: half])
            num2 = MyBigInt(num2.getHex()[: half])
        
        ac = MyBigInt.karatsuba_mul(num1, num2)
        bd = MyBigInt.karatsuba_mul(rem1, rem2)
        ad_plus_bc = MyBigInt.karatsuba_mul(num1 + rem1, num2 + rem2) - ac - bd
        
        new_number = MyBigInt("")
        number1 = MyBigInt("")
        number1.arr = [0]*NUM_LEN
        number2 = MyBigInt("")
        number2.arr = [0]*NUM_LEN
        number3 = MyBigInt("")
        number3.arr = [0]*NUM_LEN
        ac_len = len(ac.getHex())
        ad_plus_bc_len = len(ad_plus_bc.getHex())
        bd_len = len(bd.getHex())
        #print("ad_plus_bc", ad_plus_bc.getHex()) 
        #print("nums", num1.getHex(), num2.getHex()) 
        #if len(num1.getHex()) == 1 or len(num2.getHex()) == 1 or len(rem1.getHex()) == 1 or len(rem2.getHex()) == 1:
        #    print("middle", ad_plus_bc.getHex()) 
        #    return ad_plus_bc
        """
        не знаю как пофиксить умножение, до последнего шага вычисления правильные,
        но из-за суммирования разрядов каждый вызов итоговые ac, ad_plus_bc, bd становятся некорректыми
        и при финальном суммировании результат неправильный
        """
        for i in range(ac_len):
            number1.arr[2 * half + i] = ac.arr[i] 

        for i in range(ad_plus_bc_len):
            number2.arr[half + i] = ad_plus_bc.arr[i] 

        for i in range(bd_len):
            number3.arr[i] = bd.arr[i] 
        new_number = number1 + number2 + number3
        return new_number

    def one_digit_mul(self, b): 
        new_num = MyBigInt("") 
        carry = 0
        array = [0]*NUM_LEN
        for i in range (NUM_LEN):
            tmp = self.arr[i] * b
            rem = (tmp % 16 + carry) % 16
            carry = tmp // 16 + (tmp % 16 + carry) // 16
            array[i] = rem 
        new_num.arr = array
        return new_num


if __name__ == '__main__':
    test_xor1 = "51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4"     
    test_xor2 = "403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c"     
    test_xor_res = "1182d8299c0ec40ca8bf3f49362e95e4ecedaf82bfd167988972412095b13db8" 
    print(MyBigInt.xor(test_xor1, test_xor2).getHex() == test_xor_res)

    test_add1 = "36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80"     
    test_add2 = "70983d692f648185febe6d6fa607630ae68649f7e6fc45b94680096c06e4fadb"
    numA = MyBigInt(test_add1)
    numB = MyBigInt(test_add2)
    test_add_res = "a78865c13b14ae4e25e90771b54963ee2d68c0a64d4a8ba7c6f45ee0e9daa65b" 
    print((numA + numB).getHex() == test_add_res)
    
    test_sub1= "33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc"     
    test_sub2= "22e962951cb6cd2ce279ab0e2095825c141d48ef3ca9dabf253e38760b57fe03"
    numA = MyBigInt(test_sub1)
    numB = MyBigInt(test_sub2)
    test_sub_res = "10e570324e6ffdbc6b9c813dec968d9bad134bc0dbb061530934f4e59c2700b9" 
    print((numA - numB).getHex() == test_sub_res)

    test_inv = "eb8fa7e7"
    numA = MyBigInt(test_inv)
    test_inv_res = "14705818"
    print(numA.inv() == test_inv_res)

    test_onemult = "6da3"
    numA = MyBigInt(test_onemult)
    print(numA.one_digit_mul(9).getHex() == "3dabb" )
    
    test_shiftR = "eb8f"
    numA = MyBigInt(test_shiftR)
    print(numA.shiftR(2) == "3ae3")


    #test_onemult = "6da3"
    #test_onemult2 = "523a"
    #numA = MyBigInt(test_onemult)
    #numB = MyBigInt(test_onemult2)
    #print(MyBigInt.karatsuba_mul(numA, numB).getHex())

