class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age < 4:          # 4歳未満は無料
            return 0
        elif self.age < 20:       # 20歳未満
            return 1000
        elif self.age < 65:       # 20歳以上65歳未満
            return 1500
        elif self.age < 75:       # 65歳以上75歳未満
            return 1200
        else:                     # 75歳以上
            return 500

    # 顧客情報をCSV形式で返す
    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    # 顧客情報をタブ区切り形式で返す
    def info_tsv(self):
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

    # 顧客情報をパイプ区切り形式で返す
    def info_pipe(self):
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

# C-1. フルネームを取得できる
print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力
print(michelle.full_name())  # "Michelle Tanner" という値を出力

# C-2. 年齢という概念の追加
print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力
print(michelle.age)  # 3 という値を出力

# C-3. 年齢に応じた入場料
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力
print(michelle.entry_fee())  # 0 という値を出力

# C-4. CSV形式で出力
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力
print(michelle.info_csv())  # "Michelle Tanner,3,0" という値を出力

# C-7. タブ区切り形式で出力
print(ken.info_tsv())  # Ken Tanaka         15      1000
print(tom.info_tsv())  # Tom Ford           57      1500
print(ieyasu.info_tsv())  # Ieyasu Tokugawa 75      500
print(michelle.info_tsv())  # Michelle Tanner 3     0

# C-8. パイプ区切り形式で出力
print(ken.info_pipe())  # Ken Tanaka|15|1000
print(tom.info_pipe())  # Tom Ford|57|1500
print(ieyasu.info_pipe())  # Ieyasu Tokugawa|75|500
print(michelle.info_pipe())  # Michelle Tanner|3|0
