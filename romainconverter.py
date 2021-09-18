
class romain:
    def __init__(self):
        self.romain = { 
                        1000: 'M',
                        500: 'D',
                        100: 'C',
                        50: 'L',
                        10: 'X',
                        5: 'V',
                        1: 'I' 
                    }   
        self.substruct = {
                        100: 'C',
                        10: 'X',
                        1: 'I'
                    }

        self.number = None

    def convert(self, x):
        self.number = x
        if not self.__valid(x):
            return
        result = ''
        if x in self.romain.keys():
            print(self.romain[x])

        for key, value in self.romain.items():
            if x == 0:
                break
            if x // key > 0:
                for i in range(x // key):
                    result += value
                    x = x % key
            new_x, new_value = self.__check_prev(x, key)
            if new_x != x:
                x = new_x
                result += new_value
            if x == key:
                result += value
                break
        return result

    def __check_prev(self, x, last_key):
        for key, value in self.substruct.items():
            if x == 0:
                break
            if last_key == key:
                continue
            result = x // (last_key - key)
            if result == 1:
                x -= last_key - key
                return x, self.romain[key] + self.romain[last_key]
        return x, ''

    def __valid(self, number):
        if type(number) is int:
            if int(number) > 0:
                return True
            else:
                print(" you should enter a positive number !")
                print("\n__________________________________________________________\n")
                return False
        else:
            print(" you should enter a number !")
            print("\n__________________________________________________________\n")
            return False

    # just for explication
 
    def explication(self, x):
        self.number = x
        print("\n we enter the main function\n")
        print(f" we check first if {x} is a valid number or not")
        print("__________________________________________________________\n")
        if not self.__valid_explication(x):
            return
        print(" Now we are back to the main function\n")
        result = ''
        if x in self.romain.keys():
            print(self.romain[x])
        index = 0
        for key, value in self.romain.items():
            if index == 0:
                print(f' We enter the main loop\n')
                index += 1
            else:
                print(f' We get back to the main loop\n')
            if x == 0:
                print(" If our number becomes 0 we exit the loop and print result")
                print("\n__________________________________________________________\n")
                break
            if x // key > 0:
                print(f" {x} div {key} == {x//key} > 0 ? ==> Yes")
                print(f" So now we add '{value}' {x//key} times ")
                print(f" And we substruct {key * (x//key)} from  {x}")
                for i in range(x // key):
                    result += value
                    x = x % key
                print(f' Number → {x} and chiffre romain → {result}')
                print("\n__________________________________________________________\n")
            else:
                print(f" {x} div {key} > 0 ? # {x // key}  ==> No,\n so we pass")
                print("\n__________________________________________________________\n")

            new_x, new_value = self.__check_prev_explication(x, key, result)
            if new_x != x:
                x = new_x
                result += new_value
                print(f' Number → {x} and chiffre romain → {result}')
                print("\n__________________________________________________________\n")
            if x == key:
                result += value
                break


        print(f'{self.number} en chiffre romain = {result}')

    def __check_prev_explication(self, x, last_key,r):
        print(" We enter the check prev function\n")
        for key, value in self.substruct.items():
            if last_key - key < 1:
                # print(f" if {last_key} - {key} < 1 we pass  # {last_key - key}")
                continue
            result = x // (last_key - key)
            if result == 1:
                print(f" {x} div ( {last_key} - {key}  ) = {result} > 0 ? # {last_key - key}  ==> Yes")
                print(f" So we substruct {last_key - key} from {x}")
                x -= last_key - key
                print(f" And we add {self.romain[key]} before {self.romain[last_key]}")
                return x, self.romain[key] + self.romain[last_key]
            else:
                print(f" {x} div ( {last_key} - {key} ) == {result} > 0 ? # {last_key - key}  ==> No,\n so we pass")
                print("\n__________________________________________________________\n")
        return x, ''

    def __valid_explication(self, number):
        print(" we enter the valid function\n")
        print(f" First we check if '{number}' is a number",end=" ")
        if type(number) is int:
            print(f" ==> yes it's a number\n then we check if {number} is greater then 0",end=" ")
            if int(number) > 0:
                print(f"==> yes so we return True since it's a valid number :)")
                print("__________________________________________________________\n")
                return True
            else:
                print(f"==> No\n so we return False since it's negative number and we print to the user : ")
                print(" you should enter a positive number !")
                print("__________________________________________________________\n")
                return False
        else:
            print(f"==> No\n so we return False since it's not a number and we print to the user : ")
            print(" you should enter a number !")
            print("__________________________________________________________\n")
            return False



