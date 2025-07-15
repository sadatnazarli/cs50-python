def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date_input = input("Date: ").strip()

            month = 0
            day = 0
            year = 0

            if "/" in date_input:
                parts = date_input.split("/")
                month = int(parts[0])
                day = int(parts[1])
                year = int(parts[2])
            elif "," in date_input:
                parts = date_input.split()
                if len(parts) != 3:
                    continue

                month_name = parts[0]
                day_str = parts[1].replace(",", "")

                if month_name not in months:
                    continue

                month = months.index(month_name) + 1
                day = int(day_str)
                year = int(parts[2])
            else:
                continue

            if not (1 <= month <= 12 and 1 <= day <= 31 and year >= 0):
                continue

            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except ValueError:
            continue
        except EOFError:
            break
        except:
            continue


if __name__ == "__main__":
    main()
