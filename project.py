import csv

def main():
    views = view_count()

    niche = input("\nWhat is the video about?\n Choose 0 for Making money online\n 1 for Digital marketing\n 2 for Personal finance and investment\n 3 for Educational content\n 4 for Tech cars and gadjets\n 5 for Lifestyle\n 6 for Fashion and try on hauls\n 7 for Beauty and makeup\n 8 for Cooking\n 9 for Fitness and bodybuilding\n 10 for Video games\n 11 for Comedy humour challanges and pranks\n 12 for ASMR and oddly satisfying\n 13 for Motivation and spirituality\n 14 for Tralvel\n")
    niche = float(niche_rate(niche))

    print("What are the top three countries that watched your video?")
    rate1 = country_rate1()
    rate2 = country_rate2()
    rate3 = country_rate3()

    country = (float(rate1)+float(rate2)+float(rate3))/3
    avarage_rate = (country+niche)/2

    payment = avarage_rate / 1000 * views
    print(f"\nYour video made around ${"%.2f"%payment}")

def view_count():
    while True:
        try:
            number = int(input("\nHow many views did your video make? "))
            return number
        except ValueError:
            print("That's not a valid number. Please try again.")

def niche_rate(y):
    while True:
        if y.isdigit() == False:
            y = input("It has to be a number!\n")
        elif int(y) < 0 or int(y) > 14:
            y = input("Choose one of the given numbers!\n")
        else:
            with open("niche.csv", "r") as file:
                reader = csv.reader(file, delimiter="$")
                row_number = int(y)
                for index, row in enumerate(reader):
                    if index == row_number:
                        return(row[1])
all_countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia",
    "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
    "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia (Czech Republic)",
    "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor (Timor-Leste)",
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini (fmr. Swaziland)", "Ethiopia",
    "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
    "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia",
    "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
    "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
    "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
    "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
    "Mozambique", "Myanmar (formerly Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua",
    "Niger", "Nigeria", "North Korea", "North Macedonia (formerly Macedonia)", "Norway", "Oman", "Pakistan", "Palau",
    "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
    "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa",
    "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
    "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka",
    "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga",
    "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "Uae",
    "United Kingdom", "Uk", "United States of America", "Usa", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen",
    "Zambia", "Zimbabwe"
]

def country_rate1():
    while True:
        country_name = input("Please enter the 1st country: ").title()
        if country_name in all_countries:
            with open("country.csv", "r") as file:
                reader = csv.reader(file, delimiter="$")
                for row in reader:
                    if row[0] == country_name:
                        return(row[1])
            break
        else:
            print("Please enter a valid country name.")

def country_rate2():
    while True:
        country_name = input("Please enter the 2nd country: ").title()
        if country_name in all_countries:
            with open("country.csv", "r") as file:
                reader = csv.reader(file, delimiter="$")
                for row in reader:
                    if row[0] == country_name:
                        return(row[1])
            break
        else:
            print("Please enter a valid country name.")

def country_rate3():
    while True:
        country_name = input("Please enter the 3rd country: ").title()
        if country_name in all_countries:
            with open("country.csv", "r") as file:
                reader = csv.reader(file, delimiter="$")
                for row in reader:
                    if row[0] == country_name:
                        return(row[1])
            break
        else:
            print("Please enter a valid country name.")

if __name__ == "__main__":
    main()