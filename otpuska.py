class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        result = []
        
       
        lower_text = str.lower(original_text)   
        
        for letter in lower_text:
            if letter == ' ' or letter == '!' or letter == '.' or letter == ',' or letter == '!' or letter == '-' or letter == '"':
                list.append(result, letter)
            else:
                new_letter_index = str.find(self.alphabet, letter)
                
            
                if (new_letter_index+shift) < 33:
                    new_letter = self.alphabet[new_letter_index+shift]
                    list.append(result, new_letter)
                else:
                    last_letter = (new_letter_index+shift) - (new_letter_index+shift)//33*33
                    new_letter = self.alphabet[last_letter]
                    list.append(result, new_letter)
        return ''.join(result)

    def decipher(self, cipher_text, shift):

        lower_text = str.lower(cipher_text) 

        result = []  
        
        for letter in lower_text:
            if letter == ' ' or letter == '!' or letter == '.' or letter == ',' or letter == '!' or letter == '-' or letter == '"':
                list.append(result, letter)
            else:
                new_letter_index = str.find(self.alphabet, letter)
                
            
                if (new_letter_index-shift) < 33:
                    new_letter = self.alphabet[new_letter_index-shift]
                    list.append(result, new_letter)
                else:
                    last_letter = (new_letter_index-shift) - (new_letter_index-shift)//33*33
                    new_letter = self.alphabet[last_letter]
                    list.append(result, new_letter)
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))