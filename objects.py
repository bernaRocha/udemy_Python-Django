class Hours:
    
    def morning(self):
        print('Good morning')

    def evening(self):
        print('Tired as hell')


def main():
    how_I_feel = Hours()
    how_I_feel.morning()
    how_I_feel.evening()


if __name__ == "__main__":
    main()