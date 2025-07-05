def main():
  due = 50
  while due > 0:
    print(f"Amount Due: {due}")
    insert = int(input("Insert Coin: ").strip())
    if insert == 25 or insert == 10 or insert == 5:
      due -= insert
    else:
      continue
    print(f"Change Owed: {-due}")


main()

